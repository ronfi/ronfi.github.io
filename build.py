#!/usr/bin/env python3
"""ronfi.github.io 组织首页:三份公开研究的索引。中英各一页。
用法:python3 build.py"""
import datetime, html as H
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BUILT = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')

# 每个项目一条;accent 用各自站点的强调色,让索引与目标页视觉上对得上
SITES = [
 dict(key='tidemark', accent='#2E9C89', url='https://ronfi.github.io/tidemark/', repo='https://github.com/ronfi/tidemark',
      name='Tidemark', name_zh='Tidemark · 潮位线',
      tag_zh='档位,不是点位;记分,不是嘴炮。', tag_en='Bands, not points. Scored, not spun.',
      desc_zh='对主流币下一轮牛市高点的推测,以<b>档位区间 + 偏斜方向</b>发布 —— 预注册、带证伪条件、触发后不得回改。另有比特币周期图、链上储备前 10 所的每日净流量,以及九个标的的情绪六维面板。',
      desc_en='Estimates for the next bull-market high of major coins, published as <b>a range plus a skew direction</b> — pre-registered, with falsification conditions, never revised after they trigger. Plus a Bitcoin cycle chart, daily net flow across the top 10 exchanges by on-chain reserves, and a six-dimension sentiment panel for nine assets.',
      meta_zh='每日更新 · 记分账本 append-only', meta_en='updated daily · append-only scorecard'),
 dict(key='cex-reserves', accent='#1D4E89', url='https://ronfi.github.io/cex-reserves/', repo='https://github.com/ronfi/cex-reserves',
      name='CEX Reserves', name_zh='头部交易所储备核查',
      tag_zh='读链,不读公告。', tag_en='Read the chain, not the announcement.',
      desc_zh='头部交易所公布地址的 <b>BTC / ETH / Tron 链上直读</b>,与各所官方 PoR 页面逐项对照;聚合器口径规则写明,差异按同一套读法标出并附核验方法。每个数字都能用仓库脚本复现。',
      desc_en='<b>Direct on-chain reads</b> of the published BTC / ETH / Tron addresses of major exchanges, set against each venue\'s own proof-of-reserves page; aggregator caliber rules are stated, and every difference is flagged by one uniform reading with its verification method. Every number is reproducible with the repository scripts.',
      meta_zh='每周一 00:00 UTC 更新 · 脚本与地址清单公开', meta_en='updated Mondays 00:00 UTC · scripts and address lists public'),
 dict(key='us-debt', accent='#1B4D3E', url='https://ronfi.github.io/us-debt/', repo='https://github.com/ronfi/us-debt',
      name='US Debt', name_zh='美国国债:40 万亿之后',
      tag_zh='机制,不是日期;判据,不是叫喊。', tag_en='Mechanisms, not dates. Criteria, not noise.',
      desc_zh='$40 万亿之后,债务会以什么形态解决。把口径钉死(总债务 ≠ 公众持有 ≠ 可流通),把机制拆开(1946-1980 金融抑制的分解,与它今天缺哪个零件),把判据<b>预先登记</b> —— 六个触发器判定源钉死、触发后不回改。',
      desc_en='In what form does the debt get resolved after $40 trillion. It pins down the measures (total debt ≠ debt held by the public ≠ marketable), takes the mechanism apart (the decomposition of 1946-1980 financial repression, and which part its modern replica is missing), and <b>pre-registers the criteria</b> — six triggers with fixed adjudication sources, never revised after they fire.',
      meta_zh='源稿刷新时同步 · 历次版本存档', meta_en='synced when the source is refreshed · version archive'),
]

T = {
 'zh': dict(lang='zh-CN', out='index.html', url='https://ronfi.github.io/', other='en/', switch_on='中文', switch_off='English',
   title='ronfi · 公开研究索引',
   head='三份公开维护的研究',
   lede='加密市场与宏观的三份长期研究。共同点不是题材,是<b>做法</b>:结论以可证伪的形式发布,数字标注来源等级,判据在事前登记、事后不回改。',
   method='共同的做法',
   rules=[('每个数字带来源等级', '✅ 一手 / 🔶 一手+自算 / ⚠ 单一来源 / ❌ 已证伪。⚠ 项只用于画窗口,不用于下判定。'),
          ('判据事前登记,事后不回改', '阈值与判定源在登记时钉死,并回填登记当日读数 —— 出生即触发的指标没有预警能力。'),
          ('错误留在原处', '被推翻的论断不删除改写,而是连同正确读法一起留在正文里。'),
          ('旧版本可访问', '不回改的可信度 = 旧版本还能被打开。每次刷新存一份当时的页面。'),
          ('脚本与数据公开', '每个数字都能用仓库里的脚本自己跑一遍。')],
   view='打开', src='源码', foot='内容 CC BY-NC-ND 4.0 · 脚本 MIT · 均不构成投资建议',
   built='索引生成'),
 'en': dict(lang='en', out='en/index.html', url='https://ronfi.github.io/en/', other='../', switch_on='English', switch_off='中文',
   title='ronfi · index of public research',
   head='Three publicly maintained research projects',
   lede='Three long-running projects across crypto markets and macro. What they share is not a subject but a <b>method</b>: conclusions are published in falsifiable form, every figure carries a source grade, and the criteria are registered in advance and never revised afterwards.',
   method='The method they share',
   rules=[('Every figure carries a source grade', '✅ primary / 🔶 primary + own calculation / ⚠ single source / ❌ falsified. A ⚠ item sizes a window; it never settles one.'),
          ('Criteria registered in advance, never revised after', 'Thresholds and adjudication sources are fixed at registration and back-filled with that day\'s reading — an indicator that triggers on its birthday has no early-warning value.'),
          ('Mistakes stay where they were made', 'A claim that gets overturned is not quietly rewritten; it stays in the text alongside the correct reading.'),
          ('Old versions stay reachable', 'Credibility without retroactive edits = the old version still opens. A copy of each page is archived at every refresh.'),
          ('Scripts and data are public', 'Every number can be re-run from the scripts in the repository.')],
   view='Open', src='Source', foot='Content CC BY-NC-ND 4.0 · scripts MIT · none of it is investment advice',
   built='Index built'),
}

CSS = """
:root{--paper:#FAF9F6;--panel:#F2F1EC;--rule:#DFDDD5;--ink:#2A2A26;--ink-em:#111110;--ink2:#6E6D66;--accent:#2E3A59}
@media(prefers-color-scheme:dark){:root:not([data-theme=light]){--paper:#141414;--panel:#1B1B1A;--rule:#2E2E2C;--ink:#C9C8C2;--ink-em:#F3F2EE;--ink2:#8B8A83;--accent:#9FB0D4}}
:root[data-theme=dark]{--paper:#141414;--panel:#1B1B1A;--rule:#2E2E2C;--ink:#C9C8C2;--ink-em:#F3F2EE;--ink2:#8B8A83;--accent:#9FB0D4}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.75 "Noto Sans SC","PingFang SC","Hiragino Sans GB",system-ui,sans-serif;font-variant-numeric:tabular-nums}
html[lang=en] body{font-family:"Noto Sans",system-ui,-apple-system,"Segoe UI",sans-serif}
a{color:var(--accent);text-decoration:none}
.wrap{max-width:820px;margin:0 auto;padding:56px 24px 64px}
.top{display:flex;align-items:flex-start;gap:16px;flex-wrap:wrap;margin-bottom:34px}
h1{flex:1 1 auto;margin:0;font:600 30px/1.3 "Noto Serif SC","Songti SC",serif;color:var(--ink-em);letter-spacing:.2px;text-wrap:balance}
html[lang=en] h1{font-family:"Noto Serif",Georgia,serif}
.lang{flex:0 0 auto;display:inline-flex;border:1px solid var(--rule);border-radius:5px;overflow:hidden;font:600 12.5px/1 "JetBrains Mono",ui-monospace,monospace;margin-top:6px}
.lang a,.lang span{padding:7px 12px;color:var(--ink2)}
.lang a:hover{background:var(--panel);color:var(--ink-em)}
.lang .on{background:var(--accent);color:var(--paper)}
.lede{color:var(--ink2);font-size:15.5px;margin:0 0 40px;max-width:62ch}
.lede b{color:var(--ink);font-weight:600}
.card{display:block;border:1px solid var(--rule);border-left:3px solid var(--c);border-radius:3px;background:var(--panel);padding:20px 22px;margin:0 0 16px;transition:border-color .14s,transform .14s}
.card:hover{border-color:var(--c);transform:translateY(-1px)}
.card .n{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap}
.card h2{margin:0;font:600 20px/1.35 "Noto Serif SC","Songti SC",serif;color:var(--ink-em)}
html[lang=en] .card h2{font-family:"Noto Serif",Georgia,serif}
.card .tag{color:var(--c);font-size:13px;font-weight:600}
.card p{margin:.7em 0 0;font-size:14.5px;line-height:1.75}
.card p b{color:var(--ink-em)}
.card .meta{margin-top:12px;display:flex;gap:8px 16px;flex-wrap:wrap;align-items:center;font:12px/1 "JetBrains Mono",ui-monospace,monospace;color:var(--ink2)}
.card .go{color:var(--c);font-weight:600}
h3{margin:44px 0 14px;font:600 15px/1.4 "Noto Sans SC",sans-serif;color:var(--ink-em);padding-top:16px;border-top:1px solid var(--rule)}
html[lang=en] h3{font-family:inherit}
dl{margin:0;display:grid;grid-template-columns:minmax(0,15em) minmax(0,1fr);gap:10px 22px;font-size:14px}
dt{color:var(--ink-em);font-weight:600}
dd{margin:0;color:var(--ink2)}
footer{margin-top:44px;padding-top:16px;border-top:1px solid var(--rule);color:var(--ink2);font-size:12.5px;display:flex;gap:8px 20px;flex-wrap:wrap}
@media(max-width:600px){.wrap{padding:34px 18px 48px}h1{font-size:25px}dl{grid-template-columns:1fr;gap:2px 0}dd{margin-bottom:10px}}
"""

def build(lang):
    t = T[lang]; o = T['en' if lang == 'zh' else 'zh']
    cards = ''
    for s in SITES:
        nm = s['name_zh'] if lang == 'zh' else s['name']
        cards += (f'<a class="card" style="--c:{s["accent"]}" href="{s["url"]}">'
                  f'<div class="n"><h2>{nm}</h2><span class="tag">{s["tag_zh"] if lang=="zh" else s["tag_en"]}</span></div>'
                  f'<p>{s["desc_zh"] if lang=="zh" else s["desc_en"]}</p>'
                  f'<div class="meta"><span class="go">{t["view"]} →</span><span>{s["meta_zh"] if lang=="zh" else s["meta_en"]}</span></div></a>')
    rules = ''.join(f'<dt>{a}</dt><dd>{b}</dd>' for a, b in t['rules'])
    srcs = ' · '.join(f'<a href="{s["repo"]}">{s["name"]}</a>' for s in SITES)
    switch = (f'<span class="on">{t["switch_on"]}</span><a href="{t["other"]}">{t["switch_off"]}</a>' if lang == 'zh'
              else f'<a href="{t["other"]}">{t["switch_off"]}</a><span class="on">{t["switch_on"]}</span>')
    html = f"""<!DOCTYPE html><html lang="{t['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{H.escape(t['title'])}</title>
<meta name="description" content="{H.escape(t['lede'].replace('<b>','').replace('</b>',''))}">
<link rel="canonical" href="{t['url']}">
<link rel="alternate" hreflang="{t['lang']}" href="{t['url']}"><link rel="alternate" hreflang="{o['lang']}" href="{o['url']}"><link rel="alternate" hreflang="x-default" href="{T['zh']['url']}">
<meta property="og:type" content="website"><meta property="og:title" content="{H.escape(t['title'])}"><meta property="og:url" content="{t['url']}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@600&family=Noto+Serif:wght@600&family=Noto+Sans+SC:wght@400;600&family=Noto+Sans:wght@400;600&family=JetBrains+Mono:wght@500;600&display=swap">
<style>{CSS}</style></head><body>
<div class="wrap">
<div class="top"><h1>{t['head']}</h1><nav class="lang" aria-label="language">{switch}</nav></div>
<p class="lede">{t['lede']}</p>
{cards}
<h3>{t['method']}</h3>
<dl>{rules}</dl>
<footer><span>{t['src']}: {srcs}</span><span>{t['foot']}</span><span>{t['built']} {BUILT}</span></footer>
</div></body></html>"""
    p = ROOT / t['out']; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(html, encoding='utf8')
    print(t['out'], len(html), 'chars')

for l in T:
    build(l)
(ROOT / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://ronfi.github.io/sitemap.xml\n')
(ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    + ''.join(f'<url><loc>{T[l]["url"]}</loc><lastmod>{BUILT}</lastmod><priority>{"1.0" if l=="zh" else "0.9"}</priority></url>' for l in T)
    + ''.join(f'<url><loc>{s["url"]}</loc><priority>0.8</priority></url>' for s in SITES) + '</urlset>')
print('robots.txt / sitemap.xml ok')
