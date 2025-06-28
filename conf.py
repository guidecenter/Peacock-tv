# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here if needed.

# -- Project information -----------------------------------------------------

project = 'Sign In to Peacock TV'
copyright = '2025, Peacock'
author = 'Peacock'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- HTML output settings ----------------------------------------------------

# Title shown in browser tab and top of HTML pages
html_title = "How to Sign In to Peacock TV via PeacockTV.com/tv – Step-by-Step Guide"

# Short title for navigation bars
html_short_title = "Peacock TV Sign‑In Guide"

# Favicon (put favicon.ico in root or _static folder)
html_favicon = 'favicon.ico'

# Choose a theme if desired
# html_theme = 'sphinx_rtd_theme'

# Hide "View page source"
html_show_sourcelink = False

# Allow raw HTML blocks inside RST files (for buttons, styling, etc.)
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}

# Allow raw HTML directive
raw_enabled = True

# Include custom template path (e.g., for layout overrides)
templates_path = ['_templates']
# html_static_path = ['_static']  # Uncomment if you have static assets

# Patterns to ignore when scanning source files
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
