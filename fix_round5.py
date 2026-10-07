import re
import os
import glob

base_dir = '/Users/cuneytelgin/.gemini/antigravity/scratch/hrsolutionx'

# 1. Fix Mobile Menu 'TR' Color
css_path = os.path.join(base_dir, 'style.css')
with open(css_path, 'r') as f:
    css = f.read()

# Make sure ANY link in the mobile nav is white
css = css.replace('.nav-link {', '.nav-link,\n    .nav a {')

with open(css_path, 'w') as f:
    f.write(css)

# 2. Fix HTML issues
files = glob.glob(os.path.join(base_dir, '*.html'))

privacy_html = """
                <div style="margin-bottom: 1.5rem; display: flex; align-items: flex-start; gap: 10px;">
                    <input type="checkbox" id="privacy" name="Gizlilik Onayı" required style="margin-top: 3px;">
                    <label for="privacy" style="font-size: 11px; color: var(--mid-gray); line-height: 1.5;">
                        Kişisel verilerimin <a href="gizlilik-politikasi.html" style="color: var(--black); text-decoration: underline;">Gizlilik Politikası</a> kapsamında işlenmesini, saklanmasını ve yönetici araştırma süreçlerinde değerlendirilmesini onaylıyorum. *
                    </label>
                </div>
                <button type="submit"
"""

for filepath in files:
    with open(filepath, 'r') as f:
        html = f.read()
    
    # Fix Footer CV Oluştur -> Yetenek Havuzu
    html = html.replace('CV Oluştur', 'Yetenek Havuzu')
    html = html.replace('CV OLUŞTUR', 'YETENEK HAVUZU')
    
    # Add Privacy Policy to CV page
    if 'cv.html' in filepath:
        if 'Gizlilik Politikası' not in html:
            html = html.replace('<button type="submit"', privacy_html)

    with open(filepath, 'w') as f:
        f.write(html)

print("Round 5 fixes applied.")
