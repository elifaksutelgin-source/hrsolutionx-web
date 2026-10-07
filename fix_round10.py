import re
import os
import glob

base_dir = '/Users/cuneytelgin/.gemini/antigravity/scratch/hrsolutionx'
files = glob.glob(os.path.join(base_dir, '*.html'))

# Optimized Font URL (Reduced weights, added display=swap)
old_fonts_regex = r'<link href="https://fonts\.googleapis\.com/css2\?family=[^"]+" rel="stylesheet">'
new_fonts = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&family=Montserrat:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">'

# Make sure preconnects exist
preconnects = """<link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
"""

for filepath in files:
    with open(filepath, 'r') as f:
        html = f.read()
    
    # 1. Optimize Fonts
    html = re.sub(old_fonts_regex, new_fonts, html)
    
    # Ensure preconnect is there
    if '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' not in html:
        html = html.replace('<meta charset="UTF-8">', '<meta charset="UTF-8">\n    ' + preconnects.strip())
    
    # 2. Add lazy loading to images (except logo)
    # Find all <img> tags
    imgs = re.findall(r'<img [^>]+>', html)
    for img in imgs:
        if 'logo.png' not in img and 'loading="lazy"' not in img:
            new_img = img.replace('<img ', '<img loading="lazy" ')
            html = html.replace(img, new_img)
            
    # 3. Add defer to script.js if it's not there
    html = html.replace('<script src="script.js"></script>', '<script src="script.js" defer></script>')
    # Fix double defer if script was run twice
    html = html.replace('<script src="script.js" defer defer></script>', '<script src="script.js" defer></script>')

    with open(filepath, 'w') as f:
        f.write(html)

print("Round 10 fixes applied: Fonts optimized, lazy loading added, scripts deferred.")
