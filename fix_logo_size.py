import re
import os
import glob

base_dir = '/Users/cuneytelgin/.gemini/antigravity/scratch/hrsolutionx'

# 1. Add powerful CSS for the logo
css_path = os.path.join(base_dir, 'style.css')
with open(css_path, 'r') as f:
    css = f.read()

if '.brand-logo' not in css:
    logo_css = """
/* HARD OVERRIDE FOR LOGO SIZE */
.logo {
    display: flex;
    align-items: center;
    height: 70px; /* Header'i biraz daha genisletelim */
}
.brand-logo {
    width: 280px !important;
    max-width: none !important;
    height: auto !important;
    transform: scale(1.3) !important;
    transform-origin: left center !important;
}
@media (max-width: 768px) {
    .brand-logo {
        width: 200px !important;
        transform: scale(1.2) !important;
    }
}
"""
    with open(css_path, 'a') as f:
        f.write(logo_css)


# 2. Update HTML to use the new class
files = glob.glob(os.path.join(base_dir, '*.html'))
for filepath in files:
    with open(filepath, 'r') as f:
        html = f.read()
    
    # Replace the current inline styled image with the clean class
    html = re.sub(r'<img src="assets/images/logo\.png" alt="HRSolutionX Logo" style=".*?">', '<img src="assets/images/logo.png" alt="HRSolutionX Logo" class="brand-logo">', html)
    # Also catch the older one if it somehow reverted
    html = re.sub(r'<img src="assets/images/logo\.png" alt="HRSolutionX Logo" style="height: 45px.*?">', '<img src="assets/images/logo.png" alt="HRSolutionX Logo" class="brand-logo">', html)
    html = re.sub(r'<img src="assets/images/logo\.png" alt="HRSolutionX Logo" style="height: 85px.*?">', '<img src="assets/images/logo.png" alt="HRSolutionX Logo" class="brand-logo">', html)

    with open(filepath, 'w') as f:
        f.write(html)

print("Logo size aggressively overridden with CSS.")
