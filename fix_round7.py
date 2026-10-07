import re
import os
import glob

base_dir = '/Users/cuneytelgin/.gemini/antigravity/scratch/hrsolutionx'

# 1. Clean URLs in Sitemap
sitemap_path = os.path.join(base_dir, 'sitemap.xml')
with open(sitemap_path, 'r') as f:
    sitemap = f.read()

sitemap = sitemap.replace('https://www.hrsolutionx.com/index.html', 'https://www.hrsolutionx.com/')
sitemap = re.sub(r'https://www\.hrsolutionx\.com/([a-zA-Z0-9_-]+)\.html', r'https://www.hrsolutionx.com/\1', sitemap)

with open(sitemap_path, 'w') as f:
    f.write(sitemap)

# 2. Clean URLs in Canonical tags & TR text fix
files = glob.glob(os.path.join(base_dir, '*.html'))
for filepath in files:
    with open(filepath, 'r') as f:
        html = f.read()
    
    # Fix canonicals
    html = html.replace('<link rel="canonical" href="https://www.hrsolutionx.com/index.html" />', '<link rel="canonical" href="https://www.hrsolutionx.com/" />')
    html = re.sub(r'<link rel="canonical" href="https://www\.hrsolutionx\.com/([a-zA-Z0-9_-]+)\.html"\s*/>', r'<link rel="canonical" href="https://www.hrsolutionx.com/\1" />', html)
    
    # Fix TR inline styles completely (if any exist)
    html = re.sub(r'<span class="lang-switch".*?>TR</span>', '<span class="lang-switch">TR</span>', html)
    html = html.replace('class="lang-switch" class="lang-switch"', 'class="lang-switch"')

    with open(filepath, 'w') as f:
        f.write(html)


# 3. CSS Fixes for Hamburger and TR text
css_path = os.path.join(base_dir, 'style.css')
with open(css_path, 'r') as f:
    css = f.read()

# TR Text: Force white when mobile menu is open
if '.nav.open .lang-switch' not in css:
    css += "\n.nav.open .lang-switch { color: #ffffff !important; }\n"
if '.nav.open span' not in css:
    css += "\n.nav.open span { color: #ffffff !important; }\n"
if '.lang-switch' not in css:
    css += "\n.lang-switch { font-weight: 500; cursor: pointer; color: #111111; }\n"

# Hamburger Menu Color: Black normally, White when expanded
# Let's replace any existing .hamburger span background color
css = re.sub(r'\.hamburger\s*span\s*\{[^}]*background:[^}]*\}', '.hamburger span { display: block; width: 25px; height: 3px; margin: 5px auto; transition: all 0.3s ease-in-out; background: #000000; }', css)

# Just to ensure we set the background to #000 normally:
if '.hamburger[aria-expanded="true"] span' not in css:
    css += """
.hamburger span { background-color: #000000 !important; }
.hamburger[aria-expanded="true"] span { background-color: #ffffff !important; }
"""

with open(css_path, 'w') as f:
    f.write(css)

print("Round 7 fixes applied: Clean URL canonicals, Hamburger colors, TR mobile color.")
