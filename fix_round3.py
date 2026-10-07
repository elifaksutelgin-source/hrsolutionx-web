import re
import os

base_dir = '/Users/cuneytelgin/.gemini/antigravity/scratch/hrsolutionx'

# 1. Fix CSS variables
css_path = os.path.join(base_dir, 'style.css')
with open(css_path, 'r') as f:
    css = f.read()

css = css.replace('var(--color-black)', '#000000')
css = css.replace('var(--color-white)', '#ffffff')

with open(css_path, 'w') as f:
    f.write(css)

# 2. Fix index.html
idx_path = os.path.join(base_dir, 'index.html')
with open(idx_path, 'r') as f:
    idx = f.read()

# Inject title if missing
if '<title>' not in idx:
    idx = idx.replace('<meta name="viewport" content="width=device-width, initial-scale=1.0">', '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Executive Search ve İK Danışmanlığı | HRSolutionX</title>')

# Fix schema logo
idx = idx.replace('"https://hrsolutionx.com/assets/images/logo.png"', '"https://images.unsplash.com/photo-1560179707-f14e90ef3623?auto=format&fit=crop&w=500&q=80"')
idx = idx.replace('"https://www.hrsolutionx.com/assets/images/logo.png"', '"https://images.unsplash.com/photo-1560179707-f14e90ef3623?auto=format&fit=crop&w=500&q=80"')

with open(idx_path, 'w') as f:
    f.write(idx)

print("Round 3 fixes applied.")
