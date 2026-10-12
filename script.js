// ========== HEADER SCROLL EFFECT ==========
const header = document.getElementById('header');
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});

// ========== SMOOTH SCROLL ==========
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});

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

// Display submission states only after the form service confirms acceptance.
document.querySelectorAll('form[data-managed-form]').forEach(form => {
  form.addEventListener('submit', async event => {
    event.preventDefault();
    const button = form.querySelector('button[type="submit"]');
    const status = form.querySelector('.form-status');
    const english = document.documentElement.lang === 'en';
    const candidate = form.dataset.kind === 'candidate';
    if (!form.reportValidity() || button.disabled) return;
    const label = button.textContent;
    button.disabled = true;
    button.textContent = english ? 'Sending…' : 'Gönderiliyor…';
    status.textContent = '';
    try {
      const response = await fetch(form.action, {method:'POST',body:new FormData(form),headers:{Accept:'application/json'}});
      if (!response.ok) throw new Error('Form was not accepted');
      form.reset();
      status.textContent = english
        ? (candidate ? 'Your profile has been received. We may contact you about a relevant opportunity. Submission does not guarantee an interview or placement.' : 'Your enquiry has been received. Thank you for sharing your needs.')
        : (candidate ? 'Profiliniz alındı. Uygun bir fırsat oluşursa sizinle iletişime geçilebilir. Başvuru, görüşme veya işe yerleştirme garantisi değildir.' : 'Görüşme talebiniz alındı. İhtiyacınızı paylaştığınız için teşekkür ederiz.');
    } catch (error) {
      status.textContent = english ? 'We could not confirm delivery. Please try again or email info@hrsolutionx.com.' : 'Teslimatı doğrulayamadık. Lütfen yeniden deneyin veya info@hrsolutionx.com adresine yazın.';
    } finally { button.disabled = false; button.textContent = label; }
  });
});
