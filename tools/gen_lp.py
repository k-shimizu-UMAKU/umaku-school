import os, urllib.parse
ROOT = '/home/claude/umaku-school'
BASE = 'https://k-shimizu-umaku.github.io/umaku-school/'

def entry(prog):
    return '../?program=' + urllib.parse.quote(prog) + '#entry'

ARROW = '<svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 7l5 5-5 5M6 12h12"/></svg>'

def page(slug, title, desc, accent, accent_dark, soft, prog, body, B='../', css='index.tw.css', cta=None, cta_label=None, cta_section=None, url=None, title_full=None):
    cta = cta or entry(prog).replace('../', B if B else './', 1)
    cta_label = cta_label or f'{prog}を申し込む'
    url = url or f'{BASE}{slug}/'
    if cta_section is None:
        cta_section = f'''<!-- 申込 -->
<section class="py-12 md:py-20 bg-ac-soft">
  <div class="max-w-3xl mx-auto px-4 text-center">
    <h2 class="font-display font-black text-kon text-2xl md:text-3xl">体験・お問い合わせはこちらから</h2>
    <p class="mt-3 text-sm md:text-base">ウマクスクールのお申し込みフォームに移動します。<br class="hidden sm:inline">「{prog}」にチェックが入った状態で開きます。日程などが決まり次第、ご連絡します。</p>
    <a href="{cta}" class="mt-6 w-full sm:w-auto inline-flex items-center justify-center gap-2 bg-kon hover:bg-kon-deep text-white font-display font-bold text-lg px-8 py-4 rounded-full shadow-card transition-colors">
      申し込みフォームへ {ARROW}
    </a>
    <p class="mt-4 text-xs text-slate-500">メールでのお問い合わせ：<span class="select-all font-bold text-kon">Umaku.school@gmail.com</span></p>
  </div>
</section>
'''
    tfull = title_full or f'{title}｜ウマクスクール'
    return f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{tfull}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{tfull}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Zen+Maru+Gothic:wght@500;700;900&family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css}">
<script type="text/tailwind-config">
tailwind.config = {{
  theme: {{ extend: {{
    colors: {{
      kon:  {{ light:'#EEF3FB', DEFAULT:'#22346B', deep:'#161F45' }},
      vita: {{ orange:'#F5821F', dark:'#D96D08', green:'#3E9B4F', greenlight:'#E9F5EB', yellow:'#F9B915' }},
      ac:   {{ DEFAULT:'{accent}', dark:'{accent_dark}', soft:'{soft}' }},
    }},
    fontFamily: {{ display:['"Zen Maru Gothic"','sans-serif'], body:['"Noto Sans JP"','sans-serif'] }},
    boxShadow: {{ card:'0 6px 24px -10px rgba(34,52,107,.28)' }},
  }} }}
}}
</script>
<style>
  html {{ scroll-behavior:smooth; scroll-padding-top:5rem; }}
  .lane {{ background-image: repeating-linear-gradient(90deg, rgba(255,255,255,.18) 0 2px, transparent 2px 64px); }}
  .dots {{ background-image: radial-gradient(rgba(34,52,107,.10) 1.5px, transparent 1.5px); background-size:18px 18px; }}
  @media (prefers-reduced-motion: reduce) {{ html {{ scroll-behavior:auto; }} }}
</style>
</head>
<body class="font-body text-[15px] md:text-base text-slate-700 bg-white antialiased">

<header class="fixed top-0 inset-x-0 z-50 bg-white/90 backdrop-blur border-b border-kon/10">
  <div class="max-w-5xl mx-auto px-4 h-16 flex items-center justify-between gap-3">
    <a href="{B or './'}" class="flex items-center gap-2 shrink-0" aria-label="ウマクスクールのトップへ">
      <img src="{B}img/um.png" alt="ウマクスクール" class="h-8 w-auto">
      <span class="hidden sm:inline font-display font-bold text-kon">ウマクスクール</span>
    </a>
    <a href="{cta}" class="hidden md:inline-flex items-center gap-1.5 bg-ac hover:bg-ac-dark text-white font-bold text-sm px-4 py-2.5 rounded-full shadow-card transition-colors">
      {cta_label} {ARROW}
    </a>
  </div>
</header>

<main>
{body}

{cta_section}
</main>

<!-- スマホ用 固定申込バー -->
<div class="md:hidden fixed inset-x-0 bottom-0 z-50 bg-white/95 backdrop-blur border-t border-kon/10 px-4 pt-2.5" style="padding-bottom:max(.625rem,env(safe-area-inset-bottom))">
  <a href="{cta}" class="flex items-center justify-center gap-2 w-full bg-vita-orange active:bg-vita-dark text-white font-display font-bold text-base py-3.5 rounded-full shadow-card">{cta_label} {ARROW}</a>
</div>

<footer class="bg-kon-deep text-white/80 text-sm pb-24 md:pb-0">
  <div class="max-w-5xl mx-auto px-5 py-8 flex flex-col sm:flex-row gap-3 justify-between leading-relaxed">
    <p>運営：ウマクスクール設立準備委員会</p>
    <p><a href="{B or './'}#programs" class="underline underline-offset-4">ほかのプログラムを見る</a>　｜　<a href="{B or './'}" class="underline underline-offset-4">ウマクスクールのトップへ</a></p>
  </div>
</footer>
</body>
</html>
'''


def photo_hero(img, alt, badge, badge_cls, title, catch, lead, buttons, credit='', pos='center', extra=''):
    btns=''
    for href,label,primary in buttons:
        if primary:
            btns+=f'<a href="{href}" class="inline-flex items-center justify-center gap-2 bg-vita-orange hover:bg-vita-dark text-white font-bold px-6 py-3.5 rounded-full shadow-card transition-colors">{label} {ARROW}</a>'
        else:
            btns+=f'<a href="{href}" class="inline-flex items-center justify-center gap-2 bg-white/10 hover:bg-white/20 border border-white/30 font-bold px-6 py-3.5 rounded-full transition-colors">{label}</a>'
    cr=f'<p class="mt-5 text-xs text-white/60">{credit}</p>' if credit else ''
    return f'''<section class="relative pt-16 overflow-hidden bg-kon-deep">
  <div class="relative md:absolute md:inset-0">
    <img src="{img}" alt="{alt}" class="w-full aspect-[4/3] md:aspect-auto md:h-full object-cover" style="object-position:{pos}">
    <div class="absolute inset-x-0 bottom-0 h-1/3 bg-gradient-to-t from-kon-deep to-transparent md:h-full md:inset-0 md:bg-gradient-to-r md:from-kon-deep md:via-kon-deep/75 md:to-transparent" aria-hidden="true"></div>
  </div>
  <div class="relative max-w-5xl mx-auto px-4 -mt-6 pb-10 md:mt-0 md:pt-28 md:pb-24 text-white">
    <div class="md:max-w-xl">
      <p class="inline-block {badge_cls} text-xs font-bold px-3 py-1 rounded-full">{badge}</p>
      <h1 class="mt-4 font-display font-black text-[2.4rem] md:text-6xl leading-tight">{title}</h1>
      <p class="mt-3 font-display font-bold text-lg md:text-2xl text-vita-yellow">{catch}</p>
      <p class="mt-4 leading-relaxed text-white/90">{lead}</p>
      {extra}
      <div class="mt-6 flex flex-col sm:flex-row gap-3">{btns}</div>
      {cr}
    </div>
  </div>
</section>
'''

PEXELS='写真：Pexels（フリー素材）'

def h2(en, ja, color='text-ac'):
    return f'<p class="font-display font-bold {color} tracking-widest text-xs">{en}</p><h2 class="mt-1 font-display font-black text-kon text-2xl md:text-3xl">{ja}</h2>'

def facts(rows):
    out = ''
    for k, v in rows:
        out += f'<div class="grid grid-cols-[5.5rem_1fr] sm:grid-cols-[6.5rem_1fr] gap-3 py-3.5 border-b border-kon/10 last:border-0"><dt class="font-bold text-kon text-sm">{k}</dt><dd class="text-sm leading-relaxed min-w-0">{v}</dd></div>'
    return f'<dl class="mt-6 bg-white rounded-2xl shadow-card px-5 md:px-7 py-2">{out}</dl>'

TBD = '<span class="inline-block text-xs font-bold bg-vita-yellow/25 text-kon px-2 py-0.5 rounded">決まり次第お知らせ</span>'

def faq(items):
    return ''.join(f'<details class="bg-white rounded-2xl shadow-card p-5"><summary class="font-bold text-kon cursor-pointer py-1">{q}</summary><p class="mt-2 text-sm leading-relaxed">{a}</p></details>' for q, a in items)

def steps(items):
    out = ''
    for i, (t, d) in enumerate(items, 1):
        out += f'<li class="relative bg-white rounded-2xl shadow-card p-5 pl-16"><span class="absolute left-5 top-5 w-8 h-8 rounded-full bg-ac text-white font-display font-black grid place-items-center">{i}</span><p class="font-bold text-kon">{t}</p><p class="mt-1 text-sm leading-relaxed">{d}</p></li>'
    return f'<ol class="mt-6 grid gap-3">{out}</ol>'

# ---------------- 走り方教室 ----------------
run_body = f'''
{photo_hero('../img/run_hero.jpg','トラックを走る子どもたち','小学生中心・中学生歓迎','bg-vita-yellow text-kon','走り方教室','速く走れる「体」と、速く走る「コツ」。','前半は阪堺病院SCAのスタッフによる体づくり、後半は陸上の指導員による走り方の技術。運動会はもちろん、どんなスポーツにもつながる「走る土台」をつくります。',[(entry('走り方教室'),'体験を申し込む',True),('#coach','指導するのは',False)],PEXELS,'40% center')}

<section class="py-12 md:py-20 dots">
  <div class="max-w-5xl mx-auto px-4">
    {h2('POINT','この教室の3つのポイント')}
    <div class="mt-6 grid md:grid-cols-3 gap-4">
      <div class="bg-white rounded-2xl shadow-card p-6"><p class="font-display font-black text-ac text-3xl">01</p><p class="mt-2 font-bold text-kon">医療のプロと「体づくり」</p><p class="mt-2 text-sm leading-relaxed">阪堺病院SCAのスタッフが、ケガをしにくい体の使い方や、走るための柔軟性・バランスを指導します。</p></div>
      <div class="bg-white rounded-2xl shadow-card p-6"><p class="font-display font-black text-ac text-3xl">02</p><p class="mt-2 font-bold text-kon">陸上指導員が「走りの技術」</p><p class="mt-2 text-sm leading-relaxed">姿勢・腕振り・足の運び・スタートなど、速く走るためのコツを、一人ひとりの走りを見ながら伝えます。</p></div>
      <div class="bg-white rounded-2xl shadow-card p-6"><p class="font-display font-black text-ac text-3xl">03</p><p class="mt-2 font-bold text-kon">伸びが「見える」</p><p class="mt-2 text-sm leading-relaxed">測った記録は成長記録アプリ「のびしろノート」に残します。前回からの伸びが、子どもにも保護者にも分かります。</p></div>
    </div>
  </div>
</section>

<section class="py-12 md:py-20 bg-white">
  <div class="max-w-3xl mx-auto px-4">
    {h2('PROGRAM','1回の流れ（例）')}
    <p class="mt-3 text-sm text-slate-500">内容は参加者の学年・人数に合わせて調整します。</p>
    {steps([
      ('あいさつ・ウォームアップ','その日のテーマを共有し、体を温めます。'),
      ('体づくり（阪堺病院SCA）','柔軟性・バランス・体幹など、走るための体の準備。ケガ予防の考え方も学びます。'),
      ('走りの基本（陸上指導員）','姿勢・腕振り・足の運びを、ドリルで一つずつ身につけます。'),
      ('スタート・加速の練習','運動会やかけっこで差がつく、スタートと加速のコツ。'),
      ('記録・ふりかえり','タイムなどを測って、のびしろノートに記録。次回までの課題を確認します。'),
    ])}
  </div>
</section>

<section id="coach" class="py-12 md:py-20 bg-kon-light">
  <div class="max-w-5xl mx-auto px-4">
    {h2('COACH','指導するのは')}
    <div class="mt-6 grid md:grid-cols-2 gap-5">
      <div class="bg-white rounded-2xl shadow-card p-6 flex gap-5 items-start">
        <img src="../img/coach_kibe.jpg" alt="岐部あゆか指導員" class="w-24 h-32 rounded-xl object-cover bg-black shrink-0">
        <div class="min-w-0"><p class="text-xs font-bold text-ac">走りの技術</p><p class="mt-1 font-display font-black text-kon text-xl">岐部 あゆか</p><p class="text-sm text-slate-500">ウマクスクール 陸上指導員</p><p class="mt-3 text-sm leading-relaxed">走り方教室のメイン指導員。子どもたち一人ひとりの走りを見て、速く走るためのコツを伝えます。</p></div>
      </div>
      <div class="bg-white rounded-2xl shadow-card p-6 flex gap-5 items-start">
        <div class="w-24 h-32 rounded-xl bg-kon text-white grid place-items-center shrink-0 font-display font-black text-2xl">SCA</div>
        <div class="min-w-0"><p class="text-xs font-bold text-ac">体づくり</p><p class="mt-1 font-display font-black text-kon text-xl">阪堺病院 SCA</p><p class="text-sm text-slate-500">連携パートナー</p><p class="mt-3 text-sm leading-relaxed">医療機関のスタッフが、体づくりとケガの予防を担当。体力測定と成長の記録にも関わります。</p></div>
      </div>
    </div>
  </div>
</section>

<section class="py-12 md:py-20 bg-white">
  <div class="max-w-3xl mx-auto px-4">
    {h2('INFO','開催概要')}
    {facts([
      ('対象','小学生中心（中学生も歓迎）'),
      ('体験会','<span class="font-bold text-kon">2027年1月開催予定</span>　日程・会場は'+TBD),
      ('参加費',TBD),
      ('持ち物','運動しやすい服装・運動靴・飲み物'),
      ('指導','岐部あゆか指導員（陸上）／阪堺病院SCA（体づくり）'),
    ])}
  </div>
</section>

<section class="py-12 md:py-20 dots">
  <div class="max-w-3xl mx-auto px-4">
    {h2('FAQ','よくある質問')}
    <div class="mt-6 grid gap-3">{faq([
      ('足が遅くても参加できますか？','もちろんです。「今より速く走れるようになりたい」という気持ちがあれば大丈夫です。走り方は練習で変わります。'),
      ('ほかのスポーツをしていても参加できますか？','はい。走る力はサッカー・野球・バスケットボールなど、多くのスポーツの土台になります。'),
      ('のびしろノートとは何ですか？','ウマクスクールの成長記録アプリです。測定した記録を残し、伸びをグラフなどで確認できます。保護者の方には記録カードをお届けする予定です。'),
    ])}</div>
  </div>
</section>
'''

# ---------------- 食育講習会 ----------------
shoku_body = f'''
<section class="relative pt-16 overflow-hidden bg-kon-deep">
  <div class="relative md:absolute md:inset-0">
    <img src="../img/shokuiku_lecture.jpg" alt="帝塚山学院大学で「アスリートの『勝ち』を創る食事」を講義する小林勉シェフ" class="w-full aspect-[4/3] md:aspect-auto md:h-full object-cover object-[80%_center] md:object-[right_center]">
    <div class="absolute inset-x-0 bottom-0 h-1/3 bg-gradient-to-t from-kon-deep to-transparent md:h-full md:inset-0 md:bg-gradient-to-r md:from-kon-deep md:via-kon-deep/75 md:to-transparent" aria-hidden="true"></div>
  </div>
  <div class="relative max-w-5xl mx-auto px-4 -mt-6 pb-10 md:mt-0 md:pt-28 md:pb-24 text-white">
    <div class="md:max-w-xl">
      <p class="inline-block bg-vita-green text-white text-xs font-bold px-3 py-1 rounded-full">親子・ジュニアアスリート向け</p>
      <h1 class="mt-4 font-display font-black text-[2.4rem] md:text-6xl leading-tight">食育講習会</h1>
      <p class="mt-3 font-display font-bold text-lg md:text-2xl text-vita-yellow">強い体は、毎日のごはんから。</p>
      <p class="mt-4 leading-relaxed text-white/90">元・在ケニア日本大使公邸料理長で、アスリートの食事サポートも手がける<span class="font-bold text-white">小林勉シェフ</span>が講師。成長期の子どもとスポーツをがんばる子に向けて、家庭でできる「食」のコツを親子で学びます。</p>
      <div class="mt-6 flex flex-col sm:flex-row gap-3">
        <a href="{entry('食育講習会')}" class="inline-flex items-center justify-center gap-2 bg-vita-orange hover:bg-vita-dark text-white font-bold px-6 py-3.5 rounded-full shadow-card transition-colors">参加を申し込む {ARROW}</a>
        <a href="#chef" class="inline-flex items-center justify-center gap-2 bg-white/10 hover:bg-white/20 border border-white/30 font-bold px-6 py-3.5 rounded-full transition-colors">講師のプロフィール</a>
      </div>
      <p class="mt-5 text-xs text-white/60">写真：帝塚山学院大学での小林勉シェフの講義</p>
    </div>
  </div>
</section>

<section class="py-12 md:py-20 bg-white">
  <div class="max-w-5xl mx-auto px-4">
    {h2('THEME','学べること（予定）','text-vita-dark')}
    <div class="mt-6 grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
      <div class="rounded-2xl bg-orange-50 p-5"><p class="text-2xl" aria-hidden="true">🍚</p><p class="mt-2 font-bold text-kon">成長期のごはん</p><p class="mt-1 text-sm leading-relaxed">主食・主菜・副菜をそろえる考え方と、たんぱく質のとり方。</p></div>
      <div class="rounded-2xl bg-vita-greenlight p-5"><p class="text-2xl" aria-hidden="true">🍙</p><p class="mt-2 font-bold text-kon">練習前後の補食</p><p class="mt-1 text-sm leading-relaxed">いつ・何を食べるといいか。おにぎりやバナナなど身近な食材で。</p></div>
      <div class="rounded-2xl bg-kon-light p-5"><p class="text-2xl" aria-hidden="true">🥗</p><p class="mt-2 font-bold text-kon">朝ごはんのひと工夫</p><p class="mt-1 text-sm leading-relaxed">忙しい朝でも続けやすい、簡単で栄養のとれる組み合わせ。</p></div>
      <div class="rounded-2xl bg-yellow-50 p-5"><p class="text-2xl" aria-hidden="true">👨‍🍳</p><p class="mt-2 font-bold text-kon">シェフのプロの技</p><p class="mt-1 text-sm leading-relaxed">家庭のキッチンで使える、おいしく仕上げる調理のコツ。</p></div>
    </div>
    <p class="mt-4 text-xs text-slate-500">※内容・形式（講義／調理デモなど）は回ごとに調整します。</p>
  </div>
</section>

<section id="chef" class="py-12 md:py-20 bg-[#FFF5EA]">
  <div class="max-w-5xl mx-auto px-4">
    {h2('CHEF','講師プロフィール','text-vita-dark')}
    <div class="mt-6 bg-white rounded-3xl shadow-card p-6 md:p-8 grid md:grid-cols-[220px_1fr] gap-6 md:gap-8 items-start">
      <img src="../img/chef_kobayashi.jpg" alt="小林勉シェフ" class="w-44 md:w-full mx-auto rounded-2xl aspect-[3/4] object-cover object-top">
      <div class="min-w-0">
        <p class="text-sm font-bold text-vita-dark">ウマク株式会社 フードコンサルタント</p>
        <p class="mt-1 font-display font-black text-kon text-2xl md:text-3xl">小林 勉 <span class="text-base text-slate-500 font-bold">Tsutomu Kobayashi</span></p>
        <ul class="mt-5 space-y-3 text-sm leading-relaxed border-l-2 border-vita-orange/40 pl-5">
          <li>奈良のレストランや大阪のホテルで修業し、24歳で心斎橋のレストラン「Ottona」料理長に。ピッツェリアや日本料理店の料理長も経験。</li>
          <li>29歳でイタリアへ。ミラノの一つ星「Innocenti Evasioni」、トスカーナの二つ星「Da Caino」などで修業。</li>
          <li>31歳で<span class="font-bold text-kon">在ケニア日本大使公邸料理長</span>に。各国の要人を寿司・天ぷら・イタリア料理などでもてなし、3年の任期を終えて帰国。</li>
          <li>2016年、心斎橋にトスカーナ州マレンマ地方の料理に特化したレストラン「Enogastronomico Pitigliano」を開業。2017年 Hanako 関西イタリアン部門グランプリ。</li>
          <li>現在はウマク株式会社で、アスリートの食事サポートやレストランのコンサルティングを担当。</li>
        </ul>
        <div class="mt-5 flex flex-wrap gap-2">
          <span class="text-xs font-bold bg-vita-greenlight text-vita-green px-3 py-1.5 rounded-full">アスリートフードマイスター®</span>
          <span class="text-xs font-bold bg-vita-greenlight text-vita-green px-3 py-1.5 rounded-full">スポーツフードマイスター®</span>
          <span class="text-xs font-bold bg-orange-50 text-vita-dark px-3 py-1.5 rounded-full">著書『極上！神ワザレシピ』（徳間書店）</span>
          <span class="text-xs font-bold bg-kon-light text-kon px-3 py-1.5 rounded-full">テレビ・ラジオ・雑誌出演多数</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="py-12 md:py-20 bg-white">
  <div class="max-w-3xl mx-auto px-4">
    {h2('INFO','開催概要','text-vita-dark')}
    {facts([
      ('対象','親子、スポーツをがんばる子ども（ジュニアアスリート）とその保護者'),
      ('日程・会場',TBD),
      ('参加費',TBD),
      ('講師','小林勉シェフ（ウマク株式会社）'),
      ('アレルギー','試食がある回は、事前にアレルギーの有無をうかがいます。'),
    ])}
  </div>
</section>

<section class="py-12 md:py-20 bg-[#FFF5EA]">
  <div class="max-w-3xl mx-auto px-4">
    {h2('FAQ','よくある質問','text-vita-dark')}
    <div class="mt-6 grid gap-3">{faq([
      ('保護者だけの参加もできますか？','はい。毎日のごはんを作る保護者の方だけのご参加も歓迎です。'),
      ('スポーツをしていなくても参加できますか？','もちろんです。成長期の子どもに大切な食事の考え方は、スポーツをしていない子にも役立ちます。'),
      ('料理が苦手でも大丈夫ですか？','大丈夫です。家庭で無理なく続けられる、簡単な工夫を中心にお伝えします。'),
    ])}</div>
  </div>
</section>
'''

# ---------------- バレーボール教室 ----------------
vb_body = f'''
{photo_hero('../img/volleyball_hero.jpg','体育館の床に置かれたバレーボール','小学4年生〜・親子OK','bg-vita-yellow text-kon','バレーボール教室','はじめての「トス」から、いっしょに。','ボールに触るのがはじめてでも大丈夫。小学生用のやわらかいボール（4号球）に慣れるところから始めます。保護者の方もいっしょに参加できる親子の枠もあります。',[(entry('バレーボール'),'体験を申し込む',True)],PEXELS,'center','<div class="mt-5 inline-flex flex-wrap items-baseline gap-x-4 gap-y-1 bg-white text-kon rounded-2xl shadow-card px-5 py-3"><span class="text-xs font-bold">初回（予定）</span><span class="font-display font-black text-2xl">2027.1.9<span class="text-base">（土）</span> 午前</span></div>')}

<section class="py-12 md:py-20 dots">
  <div class="max-w-5xl mx-auto px-4">
    {h2('POINT','こんな人におすすめ','text-[#2A9BD0]')}
    <div class="mt-6 grid md:grid-cols-3 gap-4">
      <div class="bg-white rounded-2xl shadow-card p-6"><p class="font-bold text-kon">バレーボールをやってみたい</p><p class="mt-2 text-sm leading-relaxed">中学の部活の前に、基本を楽しく体験しておきたい子に。</p></div>
      <div class="bg-white rounded-2xl shadow-card p-6"><p class="font-bold text-kon">チームで楽しみたい</p><p class="mt-2 text-sm leading-relaxed">声をかけ合ってボールをつなぐ楽しさを、仲間といっしょに。</p></div>
      <div class="bg-white rounded-2xl shadow-card p-6"><p class="font-bold text-kon">親子で体を動かしたい</p><p class="mt-2 text-sm leading-relaxed">保護者の方も参加できる親子の枠で、休日にいっしょに運動を。</p></div>
    </div>
  </div>
</section>

<section class="py-12 md:py-20 bg-white">
  <div class="max-w-3xl mx-auto px-4">
    {h2('STEP','こんなふうに上達していきます','text-[#2A9BD0]')}
    <p class="mt-3 text-sm text-slate-500">参加者のレベルに合わせて進めます。</p>
    {steps([
      ('ボールに慣れる','投げる・受ける・はずませるなど、ボールと仲良くなる遊びから。'),
      ('パス（アンダー・オーバー）','手の形と体の向きを覚えて、ねらったところへボールを返す練習。'),
      ('サーブ','下から打つサーブで、ネットの向こうへ届ける楽しさを。'),
      ('ミニゲーム','少人数のゲームで、ボールをつなぐ楽しさを体験します。'),
    ])}
  </div>
</section>

<section class="py-12 md:py-20 bg-kon-light">
  <div class="max-w-3xl mx-auto px-4">
    {h2('INFO','開催概要','text-[#2A9BD0]')}
    {facts([
      ('対象','小学4年生以上（保護者の方との親子参加もOK）'),
      ('初回','<span class="font-bold text-kon">2027年1月9日（土）午前</span>（予定）'),
      ('時間・会場',TBD),
      ('参加費',TBD),
      ('使用ボール','4号球（小学生用）'),
      ('持ち物','運動しやすい服装・飲み物（シューズは会場決定後にお知らせします）'),
    ])}
  </div>
</section>

<section class="py-12 md:py-20 dots">
  <div class="max-w-3xl mx-auto px-4">
    {h2('FAQ','よくある質問','text-[#2A9BD0]')}
    <div class="mt-6 grid gap-3">{faq([
      ('まったくの初心者でも大丈夫ですか？','大丈夫です。ボールに慣れるところから始めるので、はじめての方も安心してご参加ください。'),
      ('保護者も参加できますか？','はい。親子でいっしょに参加できる枠があります。見学だけでも歓迎です。'),
      ('小学3年生以下は参加できますか？','対象は小学4年生以上です。きょうだいでの参加などはご相談ください。'),
    ])}</div>
  </div>
</section>
'''


def line_section(qr, note):
    return f'''<!-- LINE -->
<section id="line" class="py-12 md:py-20 bg-ac-soft">
  <div class="max-w-3xl mx-auto px-4 text-center">
    <h2 class="font-display font-black text-kon text-2xl md:text-3xl">詳しい内容・体験申込は<br>LINE公式アカウントへ</h2>
    <p class="mt-3 text-sm md:text-base">{note}</p>
    <div class="mt-6 inline-block bg-white rounded-3xl shadow-card p-6">
      <img src="img/{qr}" alt="LINE公式アカウント QRコード" class="w-44 h-44 mx-auto">
      <p class="mt-3 font-bold text-kon">QRコードから友だち追加</p>
      <p class="mt-1 text-xs text-slate-500">反応しない場合は LINE ID「<span class="select-all font-bold">@419ggvnf</span>」で検索してください</p>
    </div>
    <p class="mt-6 text-sm">ウマクスクールの<a href="index.html#entry" class="font-bold text-kon underline underline-offset-4">お申し込みフォーム</a>からもご相談いただけます。</p>
  </div>
</section>
'''

def gallery(imgs):
    return ''.join(f'<figure class="min-w-0"><img src="img/{f}" alt="{a}" class="w-full aspect-[4/3] object-cover rounded-2xl shadow-card" loading="lazy"></figure>' for f,a in imgs)

senyo_body = f'''
{photo_hero('img/senyo_hero.jpg','J-GREEN堺での練習風景','堺区の中学生','bg-[#D7262C] text-white','SENYO F.C.','部活とスクール、楽しく両立！レベルUP！','泉陽フットボールクリニック。サッカー専門指導員が、一人ひとりのレベルに合わせて「楽しさ」と「上達」の両方を引き出します。無料体験 受付中。',[('#line','無料体験を申し込む',True),('#info','スケジュール・会費',False)],'','center 60%','<div class="mt-4 flex items-center gap-3"><img src="img/senyo_emblem.png" alt="SENYO F.C. エンブレム" class="w-12 h-12 rounded-full bg-white p-0.5"><span class="text-sm font-bold">泉陽フットボールクリニック</span></div>')}

<section class="py-12 md:py-20 dots">
  <div class="max-w-5xl mx-auto px-4">
    {h2('POINT','協調性やコミュニケーション能力を身につけられるサッカー育成で、楽しく成長しよう！')}
    <div class="mt-6 grid md:grid-cols-3 gap-4">
      <div class="bg-white rounded-2xl shadow-card p-6"><p class="font-display font-black text-ac text-3xl">01</p><p class="mt-2 font-bold text-kon">部活と両立できる</p><p class="mt-2 text-sm leading-relaxed">平日夕方の練習だから、部活のあとでも通いやすい。部活動の地域移行にも対応した、新しいかたちのスクールです。</p></div>
      <div class="bg-white rounded-2xl shadow-card p-6"><p class="font-display font-black text-ac text-3xl">02</p><p class="mt-2 font-bold text-kon">専門指導員のコーチング</p><p class="mt-2 text-sm leading-relaxed">サッカー専門指導員が、一人ひとりのレベルに合わせて「楽しさ」と「上達」の両方を引き出します。</p></div>
      <div class="bg-white rounded-2xl shadow-card p-6"><p class="font-display font-black text-ac text-3xl">03</p><p class="mt-2 font-bold text-kon">土日の特別プログラム</p><p class="mt-2 text-sm leading-relaxed">合同チーム（中体連）活動、SENYO F.C.トレーニング、泉陽高校サッカー部の活動参加など、実戦の場も用意しています。</p></div>
    </div>
  </div>
</section>

<section class="py-12 md:py-20 bg-white">
  <div class="max-w-5xl mx-auto px-4">
    {h2('GALLERY','練習の様子')}
    <div class="mt-6 grid sm:grid-cols-3 gap-3">{gallery([('senyo_photo1.jpg','練習の様子'),('senyo_photo2.jpg','チーム集合写真'),('senyo_photo3.jpg','練習の様子')])}</div>
  </div>
</section>

<section id="info" class="py-12 md:py-20 bg-kon-light">
  <div class="max-w-3xl mx-auto px-4">
    {h2('INFO','スケジュール・会費')}
    {facts([
      ('対象','堺区の中学生'),
      ('練習日','火曜 16:45〜18:30<br>水曜 16:20〜18:20<br>金曜 16:45〜18:30<br>土日 月2〜3回（特別プログラム）'),
      ('場所','J-GREEN堺／泉陽高校内'),
      ('年会費','<span class="font-display font-black text-kon text-xl">2,500</span>円'),
      ('月謝','<span class="font-display font-black text-kon text-xl">2,000</span>円'),
      ('その他','遠征費など別途必要な場合があります。'),
    ])}
    <p class="mt-4 text-sm bg-white rounded-2xl shadow-card p-4"><span class="font-bold text-ac">無料体験会 受付中</span>　最新の体験会日程は、LINE公式アカウントでご案内しています。</p>
  </div>
</section>
'''

dance_body = f'''
{photo_hero('img/dance_photo1.jpg','SAKAI DANCE ZONEのレッスンの様子','小中学生・未経験OK','bg-[#8B2FC9] text-white','SAKAI DANCE ZONE','小中学生のダンス未経験も大歓迎！','SAKAIのキッズダンススクール（HIP HOP）。プロダンサーのMiria先生が、はじめの一歩から楽しく教えます。無料体験 受付中！（定員に達し次第、終了します）',[('#line','無料体験を申し込む',True),('#coach','講師を見る',False)],'写真：実際のレッスンの様子','center 55%','<div class="mt-4 flex items-center gap-3"><img src="img/dance_logo.jpg" alt="SAKAI DANCE ZONE ロゴ" class="w-12 h-12 rounded-full object-cover bg-white"><span class="text-sm font-bold">サカイダンスゾーン</span></div>')}

<section class="py-12 md:py-20 bg-white">
  <div class="max-w-3xl mx-auto px-4">
    {h2('INFO','レッスン概要')}
    {facts([
      ('レッスン','金曜 17:50〜18:40'),
      ('場所','堺市立市小学校 または 関西大学 堺キャンパス'),
      ('料金','1ヶ月体験チケット <span class="font-display font-black text-kon text-xl">3,000</span>円'),
      ('イベント','ダンスイベントや大会への参加もできます！'),
    ])}
  </div>
</section>

<section class="py-12 md:py-20 dots">
  <div class="max-w-5xl mx-auto px-4">
    {h2('LEVEL','レベルに合った指導で安心')}
    <div class="mt-6 grid md:grid-cols-2 gap-4">
      <div class="bg-white rounded-2xl shadow-card p-6"><p class="font-bold text-kon text-lg">ダンス未経験レベル 🔰</p><p class="mt-2 text-sm leading-relaxed">安心！大歓迎OK。はじめの一歩から、楽しく基礎を身につけます。</p></div>
      <div class="bg-white rounded-2xl shadow-card p-6"><p class="font-bold text-kon text-lg">少しダンス経験レベル 👍</p><p class="mt-2 text-sm leading-relaxed">もっとダンスを知りたい子へ。表現の幅をぐんぐん広げます。</p></div>
    </div>
  </div>
</section>

<section id="coach" class="py-12 md:py-20 bg-ac-soft">
  <div class="max-w-5xl mx-auto px-4">
    {h2('INSTRUCTOR','講師')}
    <div class="mt-6 bg-white rounded-3xl shadow-card p-6 md:p-8 grid sm:grid-cols-[160px_1fr] gap-6 items-start">
      <img src="img/dance_miria.png" alt="Miria先生" class="w-36 sm:w-full mx-auto rounded-2xl">
      <div class="min-w-0">
        <p class="text-sm font-bold text-ac">プロダンサー</p>
        <p class="mt-1 font-display font-black text-kon text-2xl">Miria 先生</p>
        <ul class="mt-4 space-y-2 text-sm leading-relaxed border-l-2 border-ac/40 pl-5">
          <li>全日本高等学校チームダンス選手権（小編成部門）決勝大会出場</li>
          <li>ダンスONEプロジェクト'21 日本テレビ「スッキリ！」出演</li>
          <li>堺ブレイザーズ公式チアパフォーマー 2022-2025</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="py-12 md:py-20 bg-white">
  <div class="max-w-5xl mx-auto px-4">
    {h2('GALLERY','レッスンの様子')}
    <video class="mt-6 w-full rounded-2xl shadow-card bg-black" autoplay muted loop playsinline controls poster="img/dance_poster.jpg"><source src="dance-movie.mp4" type="video/mp4"></video>
    <div class="mt-3 grid grid-cols-3 gap-3">{gallery([('dance_old_hero.jpg','イベントで踊る子どもたち'),('dance_photo2.jpg','Miria先生と子どもたち'),('dance_photo3.jpg','保護者の方も見学できます')])}</div>
    <p class="mt-3 text-sm text-slate-500">保護者の方の見学も歓迎です。</p>
  </div>
</section>
'''

pages = [
    ('running', '走り方教室', '阪堺病院SCAの体づくりと、岐部あゆか指導員による走り方の技術を一緒に学ぶ、ウマクスクールの走り方教室。小学生中心・中学生歓迎。体験会は2027年1月開催予定。', '#22346B', '#161F45', '#EEF3FB', '走り方教室', run_body),
    ('shokuiku', '食育講習会', '元・在ケニア日本大使公邸料理長の小林勉シェフが講師。成長期の子どもとジュニアアスリートのための食事のコツを親子で学ぶ、ウマクスクールの食育講習会。', '#F5821F', '#D96D08', '#FFF5EA', '食育講習会', shoku_body),
    ('volleyball', 'バレーボール教室', '小学4年生から参加できる、ウマクスクールのバレーボール教室。初心者・親子参加OK、4号球で基本から。初回は2027年1月9日（土）午前の予定。', '#2A9BD0', '#1E7FAD', '#E8F5FC', 'バレーボール', vb_body),
]
ROOT_PAGES = [
    ('senyo-fc.html','SENYO F.C.','部活とスクール、楽しく両立！レベルUP！堺区の中学生対象のサッカースクール SENYO F.C.（泉陽フットボールクリニック）。無料体験受付中。','#D7262C','#B01E23','#FDECEC','サッカー',senyo_body,'SENYO F.C.（泉陽フットボールクリニック）｜ウマクスクール',line_section('senyo_line_qr.png','SENYO F.C. のLINE公式アカウントで、体験会の日程をご案内しています。')),
    ('dance.html','SAKAI DANCE ZONE','SAKAIのキッズダンススクール。小中学生のダンス未経験も大歓迎！無料体験受付中。','#8B2FC9','#6E22A3','#F4ECFB','ダンス',dance_body,'SAKAI DANCE ZONE（サカイダンスゾーン）｜ウマクスクール',line_section('umaku_line_qr.png','「ウマクスクール」LINE公式アカウントで友だち登録してください。')),
]
for fn,title,desc,a,ad,soft,prog,body,tfull,lsec in ROOT_PAGES:
    html=page(fn[:-5],title,desc,a,ad,soft,prog,body,B='',css=fn[:-5]+'.tw.css',cta='#line',cta_label='無料体験を申し込む',cta_section=lsec,url=BASE+fn,title_full=tfull)
    open(f'{ROOT}/{fn}','w').write(html); print('wrote',fn)
for slug, title, desc, a, ad, soft, prog, body in pages:
    os.makedirs(f'{ROOT}/{slug}', exist_ok=True)
    with open(f'{ROOT}/{slug}/index.html', 'w') as f:
        f.write(page(slug, title, desc, a, ad, soft, prog, body))
    print('wrote', slug)
