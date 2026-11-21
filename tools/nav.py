"""全ページ共通のグローバルメニューを差し込む。
各HTMLの <!-- GNAV --> 〜 <!-- /GNAV --> を置き換える（無ければ最初の <header>…</header> を置き換える）。
使い方: python3 tools/nav.py
メニュー項目を変えるときは PROGRAMS / LINKS を編集して再実行。
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROGRAMS = [  # (パス, 表示名, 補足)
    ('senyo-fc.html', 'サッカー', 'SENYO F.C.'),
    ('dance.html', 'ダンス', 'SAKAI DANCE ZONE'),
    ('running/', '走り方教室', '阪堺病院SCAの体づくりつき'),
    ('volleyball/', 'バレーボール教室', '小4〜・親子OK'),
    ('shokuiku/', '食育講習会', '講師：小林勉シェフ'),
]
LINKS = [  # トップページ内のセクション
    ('#vision', '私たちの想い'),
    ('#partners', '連携体制'),
    ('#schedule', 'スケジュール'),
    ('#faq', 'よくある質問'),
]

# ページごとの設定: (ファイル, ルートへの相対パス, 右上ボタンのリンク, 右上ボタンの文言, 現在のプログラムのパス)
PAGES = [
    ('index.html', '', '#entry', '体験会に申し込む', None),
    ('senyo-fc.html', '', '#line', '無料体験を申し込む', 'senyo-fc.html'),
    ('dance.html', '', '#line', '無料体験を申し込む', 'dance.html'),
    ('kiyaku.html', '', 'index.html#entry', '体験会に申し込む', None),
    ('running/index.html', '../', '../?program=%E8%B5%B0%E3%82%8A%E6%96%B9%E6%95%99%E5%AE%A4#entry', '体験を申し込む', 'running/'),
    ('volleyball/index.html', '../', '../?program=%E3%83%90%E3%83%AC%E3%83%BC%E3%83%9C%E3%83%BC%E3%83%AB#entry', '体験を申し込む', 'volleyball/'),
    ('shokuiku/index.html', '../', '../?program=%E9%A3%9F%E8%82%B2%E8%AC%9B%E7%BF%92%E4%BC%9A#entry', '参加を申し込む', 'shokuiku/'),
    ('academy/index.html', '../', 'https://iichoshi-academy-sakai-2026.peatix.com', '申し込む（Peatix）', 'academy/'),
]

CSS = '''<style>
.gn{position:fixed;top:0;left:0;right:0;z-index:60;background:rgba(255,255,255,.94);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);border-bottom:1px solid rgba(34,52,107,.1);font-family:"Noto Sans JP",sans-serif}
.gn *{box-sizing:border-box}
.gn-in{max-width:72rem;margin:0 auto;padding:0 16px;height:64px;display:flex;align-items:center;justify-content:space-between;gap:12px}
.gn-logo{display:flex;align-items:center;gap:8px;text-decoration:none;flex-shrink:0}
.gn-logo img{height:34px;width:auto;display:block}
.gn-logo b{display:block;font-family:"Zen Maru Gothic",sans-serif;font-weight:700;color:#22346B;font-size:17px;line-height:1.2}
.gn-logo small{display:block;color:#64748b;font-size:11px;letter-spacing:.04em}
.gn-pc{display:none;align-items:center;gap:22px;font-size:14px;font-weight:500;white-space:nowrap}
.gn-pc>a,.gn-dd>button{color:#22346B;text-decoration:none;background:none;border:0;font:inherit;cursor:pointer;padding:8px 0;display:inline-flex;align-items:center;gap:4px}
.gn-pc>a:hover,.gn-dd>button:hover{color:#F5821F}
.gn-ev{color:#D96D08!important;font-weight:700}
.gn-ev:before{content:"";width:8px;height:8px;border-radius:50%;background:#F5821F;display:inline-block;margin-right:2px}
.gn .gn-cta,.gn-pc>a.gn-cta{display:inline-flex;align-items:center;gap:6px;background:#F5821F;color:#fff!important;font-weight:700;font-size:14px;padding:10px 18px;border-radius:999px;text-decoration:none;box-shadow:0 6px 24px -10px rgba(34,52,107,.28);white-space:nowrap}
.gn .gn-cta:hover{background:#D96D08;color:#fff}
.gn-dd{position:relative}
.gn-dd svg{transition:transform .2s}
.gn-dd.open svg{transform:rotate(180deg)}
.gn-sub{position:absolute;top:100%;left:50%;transform:translateX(-50%);min-width:270px;background:#fff;border:1px solid rgba(34,52,107,.1);border-radius:16px;box-shadow:0 16px 40px -12px rgba(34,52,107,.35);padding:8px;display:none}
.gn-dd.open .gn-sub{display:block}
@media (hover:hover) and (min-width:1024px){.gn-dd:hover .gn-sub{display:block}.gn-dd:hover svg{transform:rotate(180deg)}}
.gn-sub a{display:block;padding:10px 12px;border-radius:10px;color:#22346B;text-decoration:none}
.gn-sub a:hover,.gn-sub a.cur{background:#EEF3FB}
.gn-sub a b{display:block;font-weight:700;font-size:14px}
.gn-sub a span{display:block;font-size:12px;color:#64748b;margin-top:1px}
.gn-sub hr{border:0;border-top:1px solid #eef2f7;margin:6px 4px}
.gn-sub .gn-all{font-size:13px;font-weight:700;color:#D96D08}
.gn-btn{display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;border:0;background:none;color:#22346B;border-radius:10px;cursor:pointer}
.gn-btn:hover{background:#EEF3FB}
.gn-btn .x{display:none}.gn.open .gn-btn .x{display:block}.gn.open .gn-btn .h{display:none}
.gn-sp{display:none;border-top:1px solid rgba(34,52,107,.1);background:#fff;max-height:calc(100vh - 64px);overflow-y:auto}
.gn.open .gn-sp{display:block}
.gn-sp nav{padding:8px 16px 20px;display:flex;flex-direction:column}
.gn-sp a,.gn-sp summary{display:flex;align-items:center;justify-content:space-between;padding:14px 4px;border-bottom:1px solid #f1f5f9;color:#22346B;font-weight:500;font-size:15px;text-decoration:none;cursor:pointer;list-style:none}
.gn-sp summary::-webkit-details-marker{display:none}
.gn-sp details[open] summary svg{transform:rotate(180deg)}
.gn-sp .gn-kids{background:#F8FAFC;border-radius:12px;margin:6px 0 4px;padding:2px 12px}
.gn-sp .gn-kids a{font-size:14px;padding:12px 2px}
.gn-sp .gn-kids a:last-child{border-bottom:0}
.gn-sp .gn-kids a span{font-size:11px;color:#64748b;font-weight:400;margin-left:8px;text-align:right}
.gn-sp .gn-kids a.cur{color:#D96D08;font-weight:700}
.gn-sp .gn-cta{justify-content:center;margin-top:16px;padding:14px;font-size:15px}
@media (min-width:1024px){.gn-pc{display:flex}.gn-btn,.gn-sp,.gn.open .gn-sp{display:none!important}}
@media (max-width:380px){.gn-logo small{display:none}}
@media (min-width:1024px) and (max-width:1199px){.gn-logo small{display:none}.gn-pc{gap:14px;font-size:13px}.gn .gn-cta{padding:9px 14px;font-size:13px}}
</style>'''

ARROW = '<svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M13 7l5 5-5 5M6 12h12"/></svg>'
CHEV = '<svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M6 9l6 6 6-6"/></svg>'

JS = '''<script>
(function(){var g=document.getElementById('gnav');if(!g)return;
var b=g.querySelector('.gn-btn'),d=g.querySelector('.gn-dd'),db=d&&d.querySelector('button');
if(b)b.addEventListener('click',function(){var o=g.classList.toggle('open');b.setAttribute('aria-expanded',o);b.setAttribute('aria-label',o?'メニューを閉じる':'メニューを開く');});
g.querySelectorAll('.gn-sp a').forEach(function(a){a.addEventListener('click',function(){g.classList.remove('open');b&&b.setAttribute('aria-expanded','false');});});
if(db)db.addEventListener('click',function(e){e.stopPropagation();var o=d.classList.toggle('open');db.setAttribute('aria-expanded',o);});
document.addEventListener('click',function(e){if(d&&!d.contains(e.target)){d.classList.remove('open');db&&db.setAttribute('aria-expanded','false');}});
document.addEventListener('keydown',function(e){if(e.key==='Escape'){g.classList.remove('open');d&&d.classList.remove('open');}});
})();
</script>'''


def build(B, cta_href, cta_label, current):
    top = B if B else './'
    sec = (lambda h: h) if (B == '' and current is None and cta_href == '#entry') else (lambda h: top + h)
    ext = cta_href.startswith('http')
    tgt = ' target="_blank" rel="noopener"' if ext else ''
    CUR = ' class="cur" aria-current="page"'
    sub_pc = ''.join(f'<a href="{B}{p}"{CUR if p == current else ""}><b>{n}</b><span>{s}</span></a>' for p, n, s in PROGRAMS)
    sub_sp = ''.join(f'<a href="{B}{p}"{CUR if p == current else ""}>{n}<span>{s}</span></a>' for p, n, s in PROGRAMS)
    links_pc = ''.join(f'<a href="{sec(h)}">{t}</a>' for h, t in LINKS[1:])
    links_sp = ''.join(f'<a href="{sec(h)}">{t}</a>' for h, t in LINKS[1:])
    ev_cur = ' aria-current="page"' if current == 'academy/' else ''
    return f'''<!-- GNAV -->
{CSS}
<header id="gnav" class="gn">
  <div class="gn-in">
    <a href="{top}" class="gn-logo" aria-label="ウマクスクールのトップへ"><img src="{B}img/um.png" alt=""><span><b>ウマクスクール</b><small>堺区の総合型地域スポーツクラブ</small></span></a>
    <nav class="gn-pc" aria-label="グローバルメニュー">
      <a href="{sec(LINKS[0][0])}">{LINKS[0][1]}</a>
      <div class="gn-dd"><button type="button" aria-expanded="false" aria-haspopup="true">プログラム{CHEV}</button>
        <div class="gn-sub">{sub_pc}<hr><a class="gn-all" href="{sec('#programs')}">すべてのプログラムを見る →</a></div>
      </div>
      {links_pc}
      <a class="gn-ev" href="{B}academy/"{ev_cur}>12/13イベント</a>
      <a class="gn-cta" href="{cta_href}"{tgt}>{cta_label}{ARROW}</a>
    </nav>
    <button type="button" class="gn-btn" aria-label="メニューを開く" aria-expanded="false" aria-controls="gnavSp">
      <svg class="h" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" d="M4 7h16M4 12h16M4 17h16"/></svg>
      <svg class="x" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" d="M6 6l12 12M18 6L6 18"/></svg>
    </button>
  </div>
  <div id="gnavSp" class="gn-sp">
    <nav aria-label="メニュー">
      <a href="{B}academy/" style="color:#D96D08;font-weight:700">● 12/13イベント「いい調子ACADEMY in 堺」</a>
      <a href="{sec(LINKS[0][0])}">{LINKS[0][1]}</a>
      <details open><summary>プログラム{CHEV}</summary><div class="gn-kids">{sub_sp}<a href="{sec('#programs')}" style="color:#D96D08;font-weight:700">すべてのプログラムを見る</a></div></details>
      {links_sp}
      <a class="gn-cta" href="{cta_href}"{tgt}>{cta_label}{ARROW}</a>
    </nav>
  </div>
</header>
{JS}
<!-- /GNAV -->'''


def main():
    for f, B, href, label, cur in PAGES:
        p = os.path.join(ROOT, f)
        h = open(p, encoding='utf-8').read()
        block = build(B, href, label, cur)
        if '<!-- GNAV -->' in h:
            h = re.sub(r'<!-- GNAV -->.*?<!-- /GNAV -->', lambda m: block, h, count=1, flags=re.S)
        else:
            h, n = re.subn(r'<header\b.*?</header>', lambda m: block, h, count=1, flags=re.S)
            assert n == 1, f
        open(p, 'w', encoding='utf-8').write(h)
        print('nav ->', f)


if __name__ == '__main__':
    main()
