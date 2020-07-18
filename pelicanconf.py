#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'West Lane Translator Inc.'
SITENAME = 'West Lane Translator Inc.'
SITESUBTITLE = 'Serving the Central Coast since 1959'
SITEURL = ''
TIMEZONE = 'America/Los_Angeles'

PATH = 'content'
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images', 'pdfs']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
DIRECT_TEMPLATES = []
ARTICLE_PATHS = []
ARCHIVES_SAVE_AS = ''
ARTICLE_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
DRAFT_SAVE_AS = ''
INDEX_SAVE_AS = ''
TAG_SAVE_AS = ''
OUTPUT_PATH = 'output/'

PAGE_ORDER_BY = 'title'

# The site is small, so ensure output is de-crufted.
DELETE_OUTPUT_DIRECTORY = True
CACHE_CONTENT = False
LOAD_CONTENT_CACHE = False

DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = False
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# We don't need any of this
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
FEED_ALL_ATOM = None
TRANSLATION_FEED_ATOM = None

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.attr_list': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.smarty': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}

THEME = "simple"
# THEME = "../pelican-themes/blueidea"
# THEME = "../pelican-themes/eevee"
# THEME = "../pelican-themes/materialistic"
# THEME = "../pelican-themes/pelican-bootstrap3"
