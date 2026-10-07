import re
import os

base_dir = '/Users/cuneytelgin/.gemini/antigravity/scratch/hrsolutionx'
files_to_check = ['index.html', 'cv.html', 'makale-kurumsal-ceviklik.html', 'rapor-yonetim-kurulu.html', 'analiz-yetenek-savaslari.html']

# 1. Fix Canonical & OG Images in all files
for file in files_to_check:
    filepath = os.path.join(base_dir, file)
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Fix canonicals to www
    content = re.sub(r'href="https://hrsolutionx.com(.*?)"', r'href="https://www.hrsolutionx.com\1"', content)
    content = re.sub(r'content="https://hrsolutionx.com(.*?)"', r'content="https://www.hrsolutionx.com\1"', content)
    
    # Fix OG image 404
    content = content.replace('https://www.hrsolutionx.com/assets/images/og-image.jpg', 'https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1200&q=80')
    
    # Fix Logo 404 in index.html schema
    content = content.replace('https://www.hrsolutionx.com/assets/images/logo.png', 'https://images.unsplash.com/photo-1560179707-f14e90ef3623?auto=format&fit=crop&w=500&q=80')

    # 2. Fix BLACK CTA href="#"
    if file == 'index.html':
        content = content.replace('<a href="#" class="btn-primary">Hemen İletişime Geçin</a>', '<a href="#iletisim" class="btn-primary">Hemen İletişime Geçin</a>')

    with open(filepath, 'w') as f:
        f.write(content)

# 3. Fix Sitemap www consistency
sitemap_path = os.path.join(base_dir, 'sitemap.xml')
if os.path.exists(sitemap_path):
    with open(sitemap_path, 'r') as f:
        sitemap = f.read()
    sitemap = sitemap.replace('https://hrsolutionx.com', 'https://www.hrsolutionx.com')
    with open(sitemap_path, 'w') as f:
        f.write(sitemap)

# 4. Mobile Menu JS & CSS Fix in index.html
with open(os.path.join(base_dir, 'index.html'), 'r') as f:
    idx = f.read()

# Check if hamburger exists
if 'class="hamburger"' not in idx:
    # Inject hamburger button into header
    header_repl = """            <a href="cv.html" class="nav-link btn-cv">CV GÖNDER</a>
            </nav>
            <button class="hamburger" aria-label="Menü" aria-expanded="false" aria-controls="mobile-nav">
                <span></span><span></span><span></span>
            </button>"""
    idx = re.sub(r'            <a href="cv\.html" class="nav-link btn-cv">CV GÖNDER</a>\n            </nav>', header_repl, idx)
    with open(os.path.join(base_dir, 'index.html'), 'w') as f:
        f.write(idx)

# CSS for hamburger
with open(os.path.join(base_dir, 'style.css'), 'a') as f:
    f.write("""
/* Mobile Menu Fixes */
.hamburger {
    display: none;
    flex-direction: column;
    justify-content: space-around;
    width: 30px;
    height: 25px;
    background: transparent;
    border: none;
    cursor: pointer;
    z-index: 1000;
}
.hamburger span {
    width: 100%;
    height: 2px;
    background: var(--color-white);
    transition: all 0.3s linear;
}
@media (max-width: 768px) {
    .hamburger { display: flex; }
    .nav {
        position: fixed;
        top: 0; right: -100%;
        width: 250px; height: 100vh;
        background: var(--color-black);
        flex-direction: column;
        justify-content: center;
        align-items: center;
        transition: right 0.3s ease;
        z-index: 999;
    }
    .nav.open { right: 0; }
    .header-scrolled .hamburger span { background: var(--color-black); }
    .nav.open ~ .hamburger span { background: var(--color-white); }
}
""")

# JS for hamburger
with open(os.path.join(base_dir, 'script.js'), 'a') as f:
    f.write("""
// Mobile Menu Toggle
const hamburger = document.querySelector('.hamburger');
const nav = document.querySelector('.nav');
if (hamburger && nav) {
    hamburger.addEventListener('click', () => {
        nav.classList.toggle('open');
        const isOpen = nav.classList.contains('open');
        hamburger.setAttribute('aria-expanded', isOpen);
    });
}
""")

print("Critical fixes applied.")
