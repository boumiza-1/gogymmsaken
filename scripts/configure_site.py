#!/usr/bin/env python3
"""Configure the public URL for Google SEO (canonical, sitemap, OG tags).
Examples:
  python scripts/configure_site.py https://username.github.io/go-gym-msaken/
  python scripts/configure_site.py https://www.monsite.tn/
"""
import argparse,json,re
from pathlib import Path
from urllib.parse import urlparse
from xml.sax.saxutils import escape

ROOT=Path(__file__).resolve().parents[1]
PAGES=[ROOT/'index.html', ROOT/'la-salle.html', ROOT/'activites.html',ROOT/'abonnements.html', ROOT/'galerie.html',ROOT/'contact.html',ROOT/'blog/index.html',ROOT/'blog/bien-debuter-musculation-msaken.html',ROOT/'blog/cardio-ou-musculation.html',ROOT/'blog/pourquoi-cours-collectifs.html']

def main():
    p=argparse.ArgumentParser(description='Prepare GO GYM site for its real domain URL')
    p.add_argument('url',help='Actual public root URL, including repository path on GitHub Pages if any')
    args=p.parse_args()
    base=args.url.strip().rstrip('/')+'/'
    u=urlparse(base)
    if u.scheme!='https' or not u.hostname or 'username' in base.lower() or 'example.' in base.lower():
        p.error('Use your real, publicly accessible HTTPS website URL, not an example or placeholder.')
    for file in PAGES:
        text=file.read_text(encoding='utf-8')
        rel=file.relative_to(ROOT).as_posix()
        url=base+('' if rel=='index.html' else rel)
        image=base+'assets/images/'+('hero-ai.webp' if rel=='index.html' else 'facade-go-gym.webp')
        # Idempotence: remove previous SEO tags before adding the current domain.
        text=re.sub(r'<link rel="canonical"[^>]*>', '', text)
        text=re.sub(r'<meta property="og:(?:url|image)"[^>]*>', '', text)
        text=re.sub(r'<meta name="twitter:image"[^>]*>', '', text)
        insert=f'<link rel="canonical" href="{url}"><meta property="og:url" content="{url}"><meta property="og:image" content="{image}"><meta name="twitter:image" content="{image}">'
        text=text.replace('</head>',insert+'</head>',1)
        def fix_ld(m):
            try:
                obj=json.loads(m.group(1))
                if obj.get('@type')=='ExerciseGym': obj['url']=base;obj['image']=base+'assets/images/facade-go-gym.webp'
                if obj.get('@type')=='BlogPosting': obj['mainEntityOfPage']=url
                return '<script type="application/ld+json">'+json.dumps(obj,ensure_ascii=False)+'</script>'
            except (ValueError,TypeError):return m.group(0)
        text=re.sub(r'<script type="application/ld\+json">(.*?)</script>',fix_ld,text,flags=re.S)
        file.write_text(text,encoding='utf-8')
    sitemap='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for file in PAGES:
        rel=file.relative_to(ROOT).as_posix()
        target=base+('' if rel=='index.html' else rel)
        sitemap+='  <url><loc>'+escape(target)+'</loc></url>\n'
    sitemap+='</urlset>\n'
    (ROOT/'sitemap.xml').write_text(sitemap,encoding='utf-8')
    (ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: '+base+'sitemap.xml\n',encoding='utf-8')
    print('SEO configured for',base,'- 10 pages + sitemap.xml generated')
if __name__=='__main__':main()
