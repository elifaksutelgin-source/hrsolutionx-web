import re
import os
import glob

base_dir = '/Users/cuneytelgin/.gemini/antigravity/scratch/hrsolutionx'
files = glob.glob(os.path.join(base_dir, '*.html'))

for filepath in files:
    with open(filepath, 'r') as f:
        html = f.read()
    
    # Replace index.html#anchor with /#anchor
    html = re.sub(r'href="index\.html(#.*?)"', r'href="/\1"', html)
    # Replace index.html with /
    html = html.replace('href="index.html"', 'href="/"')
    
    # Replace other .html links
    html = html.replace('href="cv.html"', 'href="cv"')
    html = html.replace('href="gizlilik-politikasi.html"', 'href="gizlilik-politikasi"')
    html = html.replace('href="kullanim-sartlari.html"', 'href="kullanim-sartlari"')
    html = html.replace('href="rapor-yonetim-kurulu.html"', 'href="rapor-yonetim-kurulu"')
    html = html.replace('href="makale-kurumsal-ceviklik.html"', 'href="makale-kurumsal-ceviklik"')
    html = html.replace('href="analiz-yetenek-savaslari.html"', 'href="analiz-yetenek-savaslari"')

    with open(filepath, 'w') as f:
        f.write(html)

print("Round 9 fixes applied: All internal links are now extensionless.")
