import re

base_dir = '/Users/cuneytelgin/.gemini/antigravity/scratch/hrsolutionx'

# 1. Update index.html
with open(f"{base_dir}/index.html", "r") as f:
    html_content = f.read()

old_cta = """    <section class="contact-cta" id="iletisim">
        <div class="container contact-container">
            <h2>İnsan kaynağı stratejinizi <em>yeniden tanımlamaya</em> hazır mısınız?</h2>
            <p>Kıdemli danışmanlarımızla kurumunuza özel ihtiyaçları değerlendirmek için iletişime geçin.</p>
            <div class="contact-links">
                <a href="mailto:info@hrsolutionx.com">info@hrsolutionx.com</a>
                <a href="tel:+905000000000">+90 5XX XXX XX XX</a>
            </div>
        </div>
    </section>"""

new_cta = """    <section class="contact-cta" id="iletisim">
        <div class="container contact-container">
            <h2>İnsan kaynağı stratejinizi <em>yeniden tanımlamaya</em> hazır mısınız?</h2>
            <p>Kıdemli danışmanlarımızla kurumunuza özel ihtiyaçları değerlendirmek için formumuzu doldurabilir veya bize direkt yazabilirsiniz.</p>
            
            <form action="https://formspree.io/f/moejejbg" method="POST" class="minimal-contact-form">
                <div class="form-group">
                    <input type="text" name="İsim" placeholder="Adınız Soyadınız" required>
                </div>
                <div class="form-group">
                    <input type="email" name="Email" placeholder="Kurumsal E-Posta Adresiniz" required>
                </div>
                <div class="form-group">
                    <textarea name="Mesaj" rows="3" placeholder="Mesajınız veya talebiniz..." required></textarea>
                </div>
                <button type="submit" class="btn-primary">Talebi Gönder</button>
            </form>

            <div class="contact-links" style="margin-top: 3rem;">
                <a href="mailto:info@hrsolutionx.com">info@hrsolutionx.com</a>
            </div>
        </div>
    </section>"""

if old_cta in html_content:
    html_content = html_content.replace(old_cta, new_cta)
    with open(f"{base_dir}/index.html", "w") as f:
        f.write(html_content)
    print("index.html updated successfully.")
else:
    print("Could not find the exact CTA block. Updating via regex...")
    # fallback
    html_content = re.sub(r'<section class="contact-cta" id="iletisim">.*?</section>', new_cta, html_content, flags=re.DOTALL)
    with open(f"{base_dir}/index.html", "w") as f:
        f.write(html_content)
    print("index.html updated via regex.")

# 2. Add CSS to style.css
with open(f"{base_dir}/style.css", "r") as f:
    css_content = f.read()

if ".minimal-contact-form" not in css_content:
    form_css = """
/* ========== CONTACT FORM ========== */
.minimal-contact-form {
    max-width: 600px;
    margin: 3rem auto 0;
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    text-align: left;
}

.minimal-contact-form .form-group input,
.minimal-contact-form .form-group textarea {
    width: 100%;
    padding: 1rem 1.5rem;
    background-color: transparent;
    border: 1px solid rgba(255, 255, 255, 0.3);
    color: var(--color-white);
    font-family: inherit;
    font-size: 1rem;
    outline: none;
    transition: border-color 0.3s ease;
}

.minimal-contact-form .form-group input:focus,
.minimal-contact-form .form-group textarea:focus {
    border-color: var(--color-white);
}

.minimal-contact-form .form-group input::placeholder,
.minimal-contact-form .form-group textarea::placeholder {
    color: rgba(255, 255, 255, 0.5);
}

.minimal-contact-form button {
    align-self: flex-start;
    padding: 1rem 2.5rem;
    border: none;
    cursor: pointer;
    font-size: 1rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}
"""
    with open(f"{base_dir}/style.css", "a") as f:
        f.write(form_css)
    print("style.css updated successfully.")
else:
    print("CSS already exists.")

