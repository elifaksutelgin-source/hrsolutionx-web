import re
import os

base_dir = '/Users/cuneytelgin/.gemini/antigravity/scratch/hrsolutionx'

# 1. Fix Mobile Menu Link Color
css_path = os.path.join(base_dir, 'style.css')
with open(css_path, 'r') as f:
    css = f.read()

mobile_link_css = """
    .nav-link {
        color: #ffffff !important;
        font-size: 1.2rem !important;
        margin: 1rem 0 !important;
    }
"""
# Insert inside the media query block
css = css.replace('.nav.open {\n        right: 0 !important;\n    }', '.nav.open {\n        right: 0 !important;\n    }\n' + mobile_link_css)

with open(css_path, 'w') as f:
    f.write(css)


# 2. Fix Sitemap Dates
sitemap_path = os.path.join(base_dir, 'sitemap.xml')
if os.path.exists(sitemap_path):
    with open(sitemap_path, 'r') as f:
        sitemap = f.read()
    sitemap = sitemap.replace('2023-10-07', '2026-10-07')
    with open(sitemap_path, 'w') as f:
        f.write(sitemap)


# 3. Fix 2024 -> 2026 in Content & revert Logo in Schema
def update_html_content(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        html = f.read()
    
    # Fix dates
    html = html.replace('2024 Yönetim', '2026 Yönetim')
    html = html.replace('2024 C-Level', '2026 C-Level')
    
    # Revert Logo
    html = html.replace('https://images.unsplash.com/photo-1560179707-f14e90ef3623?auto=format&fit=crop&w=500&q=80', 'https://www.hrsolutionx.com/assets/images/logo.png')
    
    with open(filepath, 'w') as f:
        f.write(html)

files = ['index.html', 'rapor-yonetim-kurulu.html']
for file in files:
    update_html_content(os.path.join(base_dir, file))

print("Round 4 fixes applied.")
