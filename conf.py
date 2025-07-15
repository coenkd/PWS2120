# -- Project information -----------------------------------------------------
project = 'PWS2120 leerlingmateriaal'
author = 'Coen Klein Douwel'
copyright = '2025'
release = '2025'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',
    'sphinx_book_theme',
]

root_doc = 'index'
language = 'nl'

# MyST-extensies
myst_enable_extensions = [
    'amsmath',
    'dollarmath',
    'colon_fence',
]

# -- HTML output -------------------------------------------------------------
html_theme = 'sphinx_book_theme'
html_title = "PWS2120 leerlingmateriaal"
html_logo = "logo.png"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

html_theme_options = {
    "repository_url": "https://github.com/coenkd/Astro-online",
    "use_issues_button": True,
    "use_repository_button": False,
    "use_edit_page_button": False,
    "extra_footer": """
        <div style="text-align: left; margin-top: 1em;">
            <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="noopener noreferrer">
                <img alt="Creative Commons Licentie" src="_static/cc.png" style="height: 40px;" />
            </a>
           
        </div>
    """
}




