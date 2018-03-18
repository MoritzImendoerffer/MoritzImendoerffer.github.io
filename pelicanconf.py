#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Moritz Imendörffer'
SITENAME = 'This is a good day for a good day'
SITEURL = 'http://MoritzImendoerffer.github.io'

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
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Scipy', 'http://scipy.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = ['./plugins', './pelican-plugins',]
PLUGINS = ['ipynb.markup', 'i18n_subsites', 'tipue_search', 'neighbors']

TYPOGRIFY = False

#INDEX_SAVE_AS = 'blog.html'
#PAGE_SAVE_AS = '{slug}.html'
#PAGE_URL = '{slug}.html'

PAGE_ORDER_BY = 'basename'
LOAD_CONTENT_CACHE = False

THEME = "my_themes/pelican-striped-html5up" # medius, html5-dopetrope, mg, pelican-fh5co-marble

# Display pages list on the top menu
DISPLAY_PAGES_ON_MENU = True

# Display categories list on the top menu
DISPLAY_CATEGORIES_ON_MENU = True

