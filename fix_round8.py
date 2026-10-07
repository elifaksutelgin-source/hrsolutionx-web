import re
import os
import glob

base_dir = '/Users/cuneytelgin/.gemini/antigravity/scratch/hrsolutionx'

css_path = os.path.join(base_dir, 'style.css')
with open(css_path, 'r') as f:
    css = f.read()

# Force TR Text explicitly
if '.nav-lang {' in css:
    css = css.replace('.nav-lang {', '.nav-lang {\n    color: #111111;\n    cursor: pointer;\n')

css += """
/* HARD OVERRIDE FOR MOBILE NAV LANG AND HAMBURGER */
@media (max-width: 768px) {
    .header .nav-lang {
        color: #ffffff !important;
        font-size: 1.2rem !important;
        margin: 1rem 0 !important;
        z-index: 1001 !important;
    }
    
    .hamburger {
        z-index: 1002 !important;
    }
    .hamburger span {
        background-color: #000000 !important;
    }
    .hamburger[aria-expanded="true"] span {
        background-color: #ffffff !important;
    }
}
"""

with open(css_path, 'w') as f:
    f.write(css)

print("Round 8 fixes applied: TR text explicitly fixed for mobile and Hamburger z-index forced.")
