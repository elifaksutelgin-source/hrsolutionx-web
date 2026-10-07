import re
import os
import glob

base_dir = '/Users/cuneytelgin/.gemini/antigravity/scratch/hrsolutionx'

# 1. Clean up the aggressive CSS from style.css
css_path = os.path.join(base_dir, 'style.css')
with open(css_path, 'r') as f:
    css = f.read()

# We need to remove the block that starts with /* HARD OVERRIDE FOR LOGO SIZE */
css = re.sub(r'/\* HARD OVERRIDE FOR LOGO SIZE \*/.*?@media \(max-width: 768px\) \{.*?\}', '', css, flags=re.DOTALL)
# Just in case there are trailing braces or it didn't match perfectly
css = re.sub(r'\.brand-logo \{.*?\}', '', css, flags=re.DOTALL)

with open(css_path, 'w') as f:
    f.write(css)


# 2. Revert the logo in all HTML files back to the text-based one
files = glob.glob(os.path.join(base_dir, '*.html'))

text_logo = '<span class="logo-text"><span class="hr-bold">HR</span> SOLUTION</span><span class="logo-x">X</span>'

for filepath in files:
    with open(filepath, 'r') as f:
        html = f.read()
    
    # Replace the img tag with the text spans
    html = re.sub(r'<img src="assets/images/logo\.png" alt="HRSolutionX Logo" class="brand-logo">', text_logo, html)
    # Catch any inline styled ones just in case
    html = re.sub(r'<img src="assets/images/logo\.png" alt="HRSolutionX Logo" style=".*?">', text_logo, html)

    with open(filepath, 'w') as f:
        f.write(html)

print("Logo reverted to original high-quality text version.")
