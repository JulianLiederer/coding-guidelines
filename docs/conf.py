project = '@@PROJECT-NAME@@'
copyright = 'ZEIT ONLINE'

source_suffix = '.rst'
master_doc = 'index'

html_theme = "sphinx_zon_theme"
html_theme_options = {
    'editme_link': (
        'https://github.com/zeitonline/@@REPO-NAME@@/edit/master/docs/{page}')
}
html_last_updated_fmt = '%b %d, %Y'
