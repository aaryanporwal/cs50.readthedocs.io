import time

extensions = [
    "recommonmark",
    "sphinx_markdown_tables",
    "sphinx_tabs.tabs",
    "sphinxcontrib.httpdomain"
]

html_css_files = ["https://cs50.readthedocs.io/_static/custom.css?" + str(round(time.time()))]
html_js_files = ["https://cs50.readthedocs.io/_static/custom.js?" + str(round(time.time()))]
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "display_version": False,
    "prev_next_buttons_location": False,
    "sticky_navigation": False
}
html_title = "CS50 Docs"

project = "CS50 Docs"
