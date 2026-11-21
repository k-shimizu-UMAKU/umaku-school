"""Tailwind を静的CSSに書き出す（CDNを使わない）。
各HTMLの <script type="text/tailwind-config"> の設定を読み、同じ場所に *.tw.css を出力。
使い方: python3 tools/build_css.py   （要 Node / npx）
"""
import re, subprocess, os, tempfile, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pages = [p for p in glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True) if '/.git/' not in p and '/tools/' not in p]
tmp = tempfile.mkdtemp()
inp = os.path.join(tmp, 'in.css'); open(inp, 'w').write('@tailwind base;@tailwind components;@tailwind utilities;')
for p in pages:
    h = open(p, encoding='utf-8').read()
    m = re.search(r'<script type="text/tailwind-config">\s*tailwind\.config\s*=\s*(\{.*?\})\s*;?\s*</script>', h, re.S)
    if not m: continue
    cfg = os.path.join(tmp, 'cfg_' + str(abs(hash(p))) + '.js')
    open(cfg, 'w').write('module.exports=Object.assign(' + m.group(1) + ',{content:[' + repr(p) + ']})')
    out = p[:-5] + '.tw.css'
    subprocess.run(['npx', '--yes', 'tailwindcss@3.4.17', '-c', cfg, '-i', inp, '-o', out, '--minify'], check=True, capture_output=True, cwd=tmp)
    print(os.path.relpath(out, ROOT), os.path.getsize(out))
