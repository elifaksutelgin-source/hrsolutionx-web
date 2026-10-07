import re
import os
import glob

base_dir = '/Users/cuneytelgin/.gemini/antigravity/scratch/hrsolutionx'
files = glob.glob(os.path.join(base_dir, '*.html'))

old_logo_html = r'<span class="logo-text"><span class="hr-bold">HR</span> SOLUTION</span>\s*<span class="logo-x">X</span>'
old_logo_html_footer = r'<span class="logo-text"><span class="hr-bold">HR</span> SOLUTION</span><span class="logo-x">X</span>'
new_logo_html = '<img src="assets/images/logo.png" alt="HRSolutionX Logo" style="height: 45px; width: auto; display: block;">'

for filepath in files:
    with open(filepath, 'r') as f:
        html = f.read()
    
    # Replace in header/footer
    html = re.sub(old_logo_html, new_logo_html, html)
    html = re.sub(old_logo_html_footer, new_logo_html, html)
    
    # The header logo link in index.html somehow points to cv.html? Let's fix that too.
    html = html.replace('<a href="cv.html" class="logo">', '<a href="index.html" class="logo">')

    with open(filepath, 'w') as f:
        f.write(html)

print("Visual logos updated in all HTML files.")
