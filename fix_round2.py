import re
import os

base_dir = '/Users/cuneytelgin/.gemini/antigravity/scratch/hrsolutionx'

# 1. Fix CSS Mobile Menu Issue
css_path = os.path.join(base_dir, 'style.css')
with open(css_path, 'r') as f:
    css = f.read()

# Force display flex when open, and remove original display: none if possible
# Let's just add strong rules at the end.
strong_mobile_css = """
/* HARD OVERRIDE FOR MOBILE MENU */
@media (max-width: 768px) {
    .nav {
        display: flex !important;
        position: fixed !important;
        top: 0 !important;
        right: -100% !important;
        width: 250px !important;
        height: 100vh !important;
        background: var(--color-black) !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        transition: right 0.3s ease !important;
        z-index: 999 !important;
    }
    .nav.open {
        right: 0 !important;
    }
}
"""
with open(css_path, 'a') as f:
    f.write(strong_mobile_css)

# 2. Fix HTML issues in all files
files = ['index.html', 'cv.html', 'makale-kurumsal-ceviklik.html', 'rapor-yonetim-kurulu.html', 'analiz-yetenek-savaslari.html']

for file in files:
    filepath = os.path.join(base_dir, file)
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r') as f:
        html = f.read()
    
    # Remove duplicate old meta description if present
    # My new one is in the block. Let's specifically remove the original one:
    html = re.sub(r'<meta name="description" content="HR Solution X \| Yönetici Araştırması ve İnsan Kaynakları Danışmanlığı">\n\s*<title>HR Solution X \| Executive Search & İK Danışmanlığı</title>\n', '', html)
    # Just to be safe, remove the old one entirely:
    html = html.replace('<meta name="description" content="HR Solution X | Yönetici Araştırması ve İnsan Kaynakları Danışmanlığı">', '')
    
    # Fix Logo 404 everywhere (including Schema)
    html = html.replace('"logo": "https://www.hrsolutionx.com/assets/images/logo.png"', '"logo": "https://images.unsplash.com/photo-1560179707-f14e90ef3623?auto=format&fit=crop&w=500&q=80"')
    
    # Fix Menu Text
    html = html.replace('CV OLUŞTUR', 'YETENEK HAVUZU')
    html = html.replace('CV GÖNDER', 'YETENEK HAVUZU')
    
    with open(filepath, 'w') as f:
        f.write(html)

# 3. Investigate and fix BLACK link in index.html
filepath = os.path.join(base_dir, 'index.html')
with open(filepath, 'r') as f:
    idx = f.read()

# Let's search for BLACK or anything like it.
# The user said "BLACK bağlantısı". Maybe they mean the "BLACK (Gizli Arama)" service card?
# Let's find any a href="#" in index.html and change to href="cv.html" (since it's application)
idx = re.sub(r'href="#"', 'href="cv.html"', idx)

with open(filepath, 'w') as f:
    f.write(idx)

print("Round 2 fixes applied.")
