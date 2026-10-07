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
