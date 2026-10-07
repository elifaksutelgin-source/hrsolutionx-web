import re
import os
import glob
import json

base_dir = '/Users/cuneytelgin/.gemini/antigravity/scratch/hrsolutionx'

# 1. Fix Mobile Menu 'TR' Color
css_path = os.path.join(base_dir, 'style.css')
with open(css_path, 'r') as f:
    css = f.read()

# Make sure lang-switch is white on mobile
if '.lang-switch' not in css.split('@media (max-width: 768px)')[-1]:
    css = css.replace('.nav a {', '.nav a,\n    .lang-switch {')
    # Also just in case, inject it forcefully
    css = css.replace('.nav.open {', '.nav.open {\n    }\n    .nav.open .lang-switch { color: #ffffff !important; }\n    .nav.open {')

with open(css_path, 'w') as f:
    f.write(css)


# 2. Fix Schema URL in all HTML files
files = glob.glob(os.path.join(base_dir, '*.html'))
for filepath in files:
    with open(filepath, 'r') as f:
        html = f.read()
    
    # Fix inline color of lang-switch causing issues
    html = html.replace('style="color: var(--black); font-weight: 500; cursor: pointer;"', 'class="lang-switch"')
    # Fix schema URL
    html = html.replace('"url": "https://hrsolutionx.com/"', '"url": "https://www.hrsolutionx.com/"')
    html = html.replace('"url": "https://hrsolutionx.com"', '"url": "https://www.hrsolutionx.com"')

    with open(filepath, 'w') as f:
        f.write(html)

# 3. Fix robots.txt
robots_path = os.path.join(base_dir, 'robots.txt')
if os.path.exists(robots_path):
    with open(robots_path, 'r') as f:
        robots = f.read()
    robots = robots.replace('https://hrsolutionx.com/sitemap.xml', 'https://www.hrsolutionx.com/sitemap.xml')
    with open(robots_path, 'w') as f:
        f.write(robots)

# 4. Create vercel.json for 301 Redirects and Clean URLs
vercel_path = os.path.join(base_dir, 'vercel.json')
vercel_config = {
  "cleanUrls": True,
  "trailingSlash": False,
  "redirects": [
    {
      "source": "/index.html",
      "destination": "/",
      "permanent": True
    }
  ]
}
with open(vercel_path, 'w') as f:
    json.dump(vercel_config, f, indent=2)

print("Round 6 fixes applied, including vercel.json for redirects.")
