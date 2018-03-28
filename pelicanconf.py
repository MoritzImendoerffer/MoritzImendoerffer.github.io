#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Moritz Imendörffer'
SITENAME = 'This is a good day for a good day'
#SITEURL = 'http://MoritzImendoerffer.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('A great resource for mastering python', 'https://github.com/dabeaz/python-cookbook'),
	 ('Scientific lecture notes for Python', 'https://www.scipy-lectures.org/'),
	 ('10 minutes to pandas', 'https://pandas.pydata.org/pandas-docs/stable/10min.html'),
	 ('Pandas without seaborn is like jam without butter', 'https://pandas.pydata.org/pandas-docs/stable/10min.html'),
	 ('A great datascience blog', 'https://www.dataquest.io/blog//'), 
	 ('Pelican, a static site generator', 'http://getpelican.com/'),
         ('Python for microcontrollers', 'https://micropython.org/'),
         ('The race around the world', 'http://volvooceanrace.com'),)
# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins', './pelican-plugins']
PLUGINS = ['ipynb.markup', 'i18n_subsites', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook']
I18N_TEMPLATES_LANG = 'en'

I18N_SUBSITES = {
    'en': {
        'SITENAME': 'This is a good day for a good day',
        }
    }

#TYPOGRIFY = False

#INDEX_SAVE_AS = 'blog.html'
#PAGE_SAVE_AS = '{slug}.html'
#PAGE_URL = '{slug}.html'

#PAGE_ORDER_BY = 'basename'
LOAD_CONTENT_CACHE = False

#THEME = "my_themes/pelican-striped-html5up" # medius, html5-dopetrope, mg, pelican-fh5co-marble
THEME = "pelican-themes/pelican-bootstrap3"
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
BOOTSTRAP_THEME =  'simplex' #'sandstone' #
# Display pages list on the top menu
DISPLAY_PAGES_ON_MENU = True
NOTEBOOK_DIR = 'content'
# Display categories list on the top menu
DISPLAY_CATEGORIES_ON_MENU = True

#FAVICON = 'images/favicon.png'
