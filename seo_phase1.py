import re

base_dir = '/Users/cuneytelgin/.gemini/antigravity/scratch/hrsolutionx'

# 1. Create robots.txt
with open(f"{base_dir}/robots.txt", "w") as f:
    f.write("""User-agent: *
Allow: /

Sitemap: https://hrsolutionx.com/sitemap.xml
""")

# 2. Create sitemap.xml
with open(f"{base_dir}/sitemap.xml", "w") as f:
    f.write("""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://hrsolutionx.com/</loc>
    <lastmod>2023-10-07</lastmod>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://hrsolutionx.com/cv.html</loc>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://hrsolutionx.com/rapor-yonetim-kurulu.html</loc>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://hrsolutionx.com/makale-kurumsal-ceviklik.html</loc>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://hrsolutionx.com/analiz-yetenek-savaslari.html</loc>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://hrsolutionx.com/gizlilik-politikasi.html</loc>
    <priority>0.5</priority>
  </url>
  <url>
    <loc>https://hrsolutionx.com/kullanim-sartlari.html</loc>
    <priority>0.5</priority>
  </url>
</urlset>
""")

# 3. Inject SEO Tags into index.html
seo_tags = """
    <!-- ================= SEO & META TAGS ================= -->
    <meta name="description" content="HRSolutionX, Türkiye ve küresel pazarda Üst Düzey Yönetici Seçimi (Executive Search), C-Level İşe Alım ve Yönetim Kurulu Danışmanlığı yapan premium İK firmasıdır.">
    <meta name="keywords" content="Executive Search, Üst Düzey Yönetici Seçimi, C-Level İşe Alım, Headhunter Türkiye, İnsan Kaynakları Danışmanlığı, Yönetim Kurulu Danışmanlığı, Liderlik">
    <link rel="canonical" href="https://hrsolutionx.com/" />
    
    <!-- Open Graph (LinkedIn / Facebook / WhatsApp) -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://hrsolutionx.com/">
    <meta property="og:title" content="HRSolutionX | Premium Executive Search & C-Level İşe Alım">
    <meta property="og:description" content="Kurumların DNA'sını değiştiren liderleri buluyoruz. Üst düzey yönetici seçimi ve stratejik İK danışmanlığı alanında gizlilik odaklı premium hizmet.">
    <meta property="og:image" content="https://hrsolutionx.com/assets/images/og-image.jpg">
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="https://hrsolutionx.com/">
    <meta property="twitter:title" content="HRSolutionX | Premium Executive Search">
    <meta property="twitter:description" content="Kurumların DNA'sını değiştiren liderleri buluyoruz.">
    <meta property="twitter:image" content="https://hrsolutionx.com/assets/images/og-image.jpg">

    <!-- Schema.org Structured Data (Google Kurum Kimliği) -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Organization",
      "name": "HRSolutionX",
      "url": "https://hrsolutionx.com/",
      "logo": "https://hrsolutionx.com/assets/images/logo.png",
      "description": "Premium Executive Search and C-Level Recruitment Consultancy in Turkey.",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Istanbul",
        "addressCountry": "TR"
      },
      "contactPoint": {
        "@type": "ContactPoint",
        "contactType": "customer service",
        "email": "info@hrsolutionx.com"
      }
    }
    </script>
    <!-- =================================================== -->
"""

with open(f"{base_dir}/index.html", "r") as f:
    content = f.read()

# Only inject if not already there
if "<!-- ================= SEO & META TAGS ================= -->" not in content:
    content = content.replace("</head>", seo_tags + "\n</head>")
    with open(f"{base_dir}/index.html", "w") as f:
        f.write(content)

print("SEO Phase 1 files created and index.html updated.")
