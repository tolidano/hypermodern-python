"""Sphinx configuration."""
from datetime import datetime


project = "Hypermodern Python"
author = "Claudio Jolowicz"
copyright = f"{datetime.now().year}, {author}"
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]
