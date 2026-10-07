import re
import os
import glob

base_dir = '/Users/cuneytelgin/.gemini/antigravity/scratch/hrsolutionx'
files = glob.glob(os.path.join(base_dir, '*.html'))

old_img_html = r'<img src="assets/images/logo.png" alt="HRSolutionX Logo" style="height: 85px; width: auto; display: block; max-width: 100%;">'
new_img_html = '<img src="assets/images/logo.png" alt="HRSolutionX Logo" style="height: 110px; width: auto; display: block; max-width: 100%; margin: -10px 0;">'

for filepath in files:
    with open(filepath, 'r') as f:
        html = f.read()
    
    html = re.sub(old_img_html, new_img_html, html)

    with open(filepath, 'w') as f:
        f.write(html)

print("Logo resized to 110px in all HTML files.")
