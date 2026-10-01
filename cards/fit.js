// カードに収まるように段の幅と文字サイズを調整し、溢れたアビリティを裏面へ送る。
function fits(e){ return e.scrollHeight <= e.clientHeight + 0.6; }

var BASE_MM = 2.5;   // card.css の .colL/.colR/.cols と合わせること
// el の文字サイズを floor（1.0 に対する比）まで二分探索で縮める。
// check を渡すとそれで収まりを判定する（既定は el 自身）。
// el は要素か要素の配列（配列なら全部に同じサイズを当てる。.colL/.colR は各自 font-size を
// mm で持っているので、親の .cols を縮めても効かない）。
function shrink(el, floor, check){
  var els = Array.isArray(el) ? el : [el];
  check = check || function(){ return els.every(fits); };
  var lo = floor, hi = 1.0, best = floor;
  function set(x){ els.forEach(function(e){ e.style.fontSize = (x * BASE_MM).toFixed(3) + 'mm'; }); }
  function ok(x){ set(x); return check(); }
  if (ok(1.0)) { set(1.0); return 1; }
  for (var i = 0; i < 14; i++){
    var m = (lo + hi) / 2;
    if (ok(m)) { best = m; lo = m; } else { hi = m; }
  }
  set(best);
  return best;
}

document.querySelectorAll('.card.front').forEach(function(card){
  var i = card.dataset.i;
  var L = card.querySelector('.colL'), R = card.querySelector('.colR');
  var abox = document.getElementById('ab' + i);
  var pc = abox ? abox.querySelector('.pc') : null;
  var spill = document.getElementById('sp' + i), spc = document.getElementById('spc' + i);
  var moved = 0;

  // 右段（アビリティ）から末尾のブロックを裏面へ送る
  function spillUntilFits(){
    if (!pc || !spc) return;
    while (!fits(R)){
      var blocks = pc.querySelectorAll(':scope > .abgrp');
      if (blocks.length <= 1) break;
      spc.insertBefore(blocks[blocks.length - 1], spc.firstChild);
      moved++;
    }
  }

  // 1) アビリティが入りきるまで右段を広げる（左段が溢れない範囲で）
  var wide = ['66mm', '74mm', '82mm', '90mm'], best = wide[0];
  for (var k = 0; k < wide.length; k++){
    R.style.flexBasis = wide[k]; best = wide[k];
    if (fits(R)) break;
    if (!fits(L)) break;
  }
  R.style.flexBasis = best;

  // 2) 左段（武器表）が溢れるなら、まず文字を少し縮めて収まるか試す
  if (!fits(L)) shrink(L, 0.78);

  // 3) それでも溢れるなら、右段を狭めて幅を回す。
  //    狭めた分あふれるアビリティは裏面へ送る。
  if (!fits(L)){
    var narrow = ['62mm', '58mm', '54mm', '50mm', '46mm'];
    for (var j = 0; j < narrow.length; j++){
      R.style.flexBasis = narrow[j];
      spillUntilFits();
      if (fits(L)) break;
    }
  }

  // 4) それでも入らない分は裏面へ
  spillUntilFits();

  if (moved){
    var m = document.createElement('p');
    m.className = 'contd';
    m.textContent = '→ つづきは裏面へ / continued on the back';
    pc.appendChild(m);
  } else if (spill){
    spill.remove();
  }
  shrink(L, 0.5); shrink(R, 0.5);
});

// 裏面: .cols 自体は overflow:hidden の段に阻まれて溢れを検出できないので、両段で判定する。
// 文字を縮める前に、段の幅の配分・パネルの段間移動・オプション欄の 2 段組みで収めることを試みる。
document.querySelectorAll('.card.back').forEach(function(c){
  var cols = c.querySelector('.cols'), L = cols.querySelector('.colL'), R = cols.querySelector('.colR');
  var opt = L.querySelector(':scope > .panel.wargear > .pc');   // ウォーギア・オプション欄（無いユニットは欄ごと省略）
  function both(){ return fits(L) && fits(R); }
  function set(x){ [L, R].forEach(function(e){ e.style.fontSize = (x * BASE_MM).toFixed(3) + 'mm'; }); }

  // from 段の末尾のパネル (sel) を、to 段が溢れない範囲で to 段の末尾へ移す
  function moveTo(from, to, sel){
    var mv = Array.prototype.slice.call(from.querySelectorAll(':scope > ' + sel));
    for (var j = mv.length - 1; j >= 0 && !fits(from); j--){
      var nxt = mv[j].nextSibling;
      to.appendChild(mv[j]);
      if (!fits(to)) { from.insertBefore(mv[j], nxt); break; }
    }
  }
  function layout(){
    // 1) 右段（ユニット構成・合流先）が溢れるなら、左段が溢れない範囲で右段を広げる
    R.style.flexBasis = '72mm';
    if (opt) opt.classList.remove('two');
    if (!fits(R)){
      var wide = ['84mm', '96mm', '108mm', '120mm'], best = '72mm';
      for (var k = 0; k < wide.length; k++){
        R.style.flexBasis = wide[k];
        if (!fits(L)) { R.style.flexBasis = best; break; }
        best = wide[k];
        if (fits(R)) break;
      }
    }
    // 2) それでも溢れるなら、合流先・ポイント補足のパネルを左段の末尾へ
    if (!fits(R)) moveTo(R, L, '.panel.movable');
    // 3) 左段（ウォーギア・オプション）が溢れるなら、右段が収まる範囲で右段を狭めて幅を回し、
    //    表面から送られたアビリティを右段の末尾へ移し、最後にオプション欄を 2 段組みにする
    if (!fits(L) && fits(R)){
      var narrow = ['64mm', '56mm', '48mm'], prev = R.style.flexBasis;
      for (var n = 0; n < narrow.length && !fits(L); n++){
        R.style.flexBasis = narrow[n];
        if (!fits(R)) { R.style.flexBasis = prev; break; }
        prev = narrow[n];
      }
    }
    if (!fits(L)) moveTo(L, R, '.panel.spill');
    if (!fits(L) && opt){
      opt.classList.add('two');
      if (fits(L)) moveTo(L, R, '.panel.spill');
    }
    return both();
  }
  // 左段が空（オプションも裏送りのアビリティも無い）なら右段を全幅に
  if (!L.children.length){
    L.remove(); R.style.flex = '1 1 auto';
    shrink([R], 0.5, function(){ return fits(R); });
  } else {
    // 文字サイズを少しずつ落としながら、収まる配置を探す
    var scales = [1.0, 0.92, 0.85, 0.78, 0.72, 0.66, 0.6], done = false;
    for (var i = 0; i < scales.length && !done; i++){ set(scales[i]); done = layout(); }
    if (!done) shrink([L, R], 0.5, both);
  }

  var m = c.querySelector('.memo');
  if (m && m.getBoundingClientRect().height < 55) m.remove();
});
document.body.dataset.ready = '1';
