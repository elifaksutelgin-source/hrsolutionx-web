import re

base_dir = '/Users/cuneytelgin/.gemini/antigravity/scratch/hrsolutionx'

def inject_seo_tags(filename, title, description, url):
    with open(f"{base_dir}/{filename}", "r") as f:
        html = f.read()

    # Remove existing title and meta viewport/charset to cleanly inject new block
    html = re.sub(r'<title>.*?</title>', '', html, flags=re.DOTALL)
    html = re.sub(r'<meta charset="UTF-8">', '', html)
    html = re.sub(r'<meta name="viewport".*?>', '', html)
    
    seo_block = f"""
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{url}" />
    
    <!-- Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="{url}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="https://www.hrsolutionx.com/assets/images/og-image.jpg">
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:title" content="{title}">
    <meta property="twitter:description" content="{description}">
    """

    # Inject right after <head>
    html = re.sub(r'<head>', f"<head>\n{seo_block}", html)
    
    # Check for images and add alt tags if they are missing
    # Example: insight images might be divs with background, so alt is not needed there.
    
    with open(f"{base_dir}/{filename}", "w") as f:
        f.write(html)
    print(f"Injected SEO tags into {filename}")

inject_seo_tags(
    "makale-kurumsal-ceviklik.html", 
    "Kurumsal Çeviklikte İK'nın Rolü | HRSolutionX Executive Search", 
    "C-Level İşe Alım ve İnsan Kaynakları stratejilerinde kurumsal çevikliğin önemi. Headhunter perspektifiyle HRSolutionX makalesi.",
    "https://www.hrsolutionx.com/makale-kurumsal-ceviklik.html"
)

inject_seo_tags(
    "rapor-yonetim-kurulu.html", 
    "2024 Yönetim Kurulu & C-Level Trend Raporu | HRSolutionX", 
    "Yönetim Kurulu Danışmanlığı ve 2024 C-Level yönetici atama trendleri. HRSolutionX Türkiye Executive Search pazar araştırması.",
    "https://www.hrsolutionx.com/rapor-yonetim-kurulu.html"
)

inject_seo_tags(
    "analiz-yetenek-savaslari.html", 
    "Global Yetenek Savaşları ve Beyin Avcısı Stratejileri | HRSolutionX", 
    "Global pazarda üst düzey yetenekleri elde tutma stratejileri. Beyin avcısı (Headhunter Türkiye) perspektifinden yetenek savaşları analizi.",
    "https://www.hrsolutionx.com/analiz-yetenek-savaslari.html"
)


# 2. Update index.html - Inject high value keywords into H2/H3
with open(f"{base_dir}/index.html", "r") as f:
    idx_html = f.read()

# Enhance main About subtitle
idx_html = idx_html.replace(
    '<h2>HAKKIMIZDA</h2>',
    '<h2>HAKKIMIZDA | HEADHUNTER & EXECUTIVE SEARCH</h2>'
)
idx_html = idx_html.replace(
    'bugün uzmanlık alanımız olan her stratejik cephede',
    'bugün Executive Search (Beyin Avcısı) ve C-Level atamalar olmak üzere uzmanlık alanımız olan her stratejik cephede'
)

# Enhance Strategy section
idx_html = idx_html.replace(
    '<p>Kurumunuzu geleceğe taşıyacak stratejik insan kaynakları çözümleri.</p>',
    '<p>Kurumunuzu geleceğe taşıyacak stratejik insan kaynakları, beyin avcısı (headhunter) ve C-Level işe alım çözümleri.</p>'
)

# Image alt tags fix
idx_html = re.sub(r'<img src="assets/images/logo.png" alt="Logo">', r'<img src="assets/images/logo.png" alt="HRSolutionX Executive Search Türkiye Logo">', idx_html)
idx_html = re.sub(r'<img src="assets/images/logo.png" class="logo-image" alt="HRSolutionX">', r'<img src="assets/images/logo.png" class="logo-image" alt="HRSolutionX Yönetim Kurulu Danışmanlığı">', idx_html)

with open(f"{base_dir}/index.html", "w") as f:
    f.write(idx_html)
print("Updated index.html keywords and alt tags.")
