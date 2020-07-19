#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime

AUTHOR = 'West Lane Translator Inc.'
SITENAME = 'West Lane Translator Inc.'
SITEURL = ''
TIMEZONE = 'America/Los_Angeles'

PATH = 'content'
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images', 'pdfs']
# EXTRA_PATH_METADATA = {
#     'extra/favicon.ico': {'path': 'favicon.ico'}
# }
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

THEME = '../Flex'
MAIN_MENU = True
MENUITEMS = (
    ( 'History', '/pages/history.html' ),
    ( 'Governance', '/pages/governance.html' ),
    ( 'Leasing', '/pages/leasing.html' ),
    ( 'Membership', '/pages/membership.html' ),
    ( 'Contact Us', '/pages/contact-us.html' )
)
FOOTERMENUITEMS = (
    ( 'Terms and Conditions', '/pages/terms-and-conditions.html' ),
    ( 'Privacy Policy', '/pages/privacy-policy.html' )
)
SITETITLE = SITENAME
SITESUBTITLE = 'Serving the Central Coast since 1959'
SITELOGO = SITEURL + '/images/logo.png'
SITEDESCRIPTION = (
    "Information about West Lane Translator's HDTV and FM translators."
)
SITEURL = 'http://localhost:8000'  # publishconf.py overrides
COPYRIGHT_NAME = AUTHOR
COPYRIGHT_YEAR = datetime.datetime.today().year
ROBOTS = 'index, follow'
PAGES_SORT_ATTRIBUTE = 'menu'
FAVICON = SITEURL + '/images/favicon.ico'
THEME_COLOR = 'light'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True # Uses JavaScript

# THEME = '../pelican-themes/Flex'              # +Nav always on screen L:MIT
# THEME = "../pelican-themes/notebook"          # +Nav always on screen L:Retain copyright
# THEME = "../pelican-themes/bootstrap2"        # +Good, header problem? L:Apache
# THEME = "../pelican-themes/blueidea"          # +Good L:MIT
# THEME = "../pelican-themes/dev-random"        # +I like it L:WTFPL
# THEME = "../pelican-themes/elegant"           # +It *is* elegant L:MIT
# THEME = "../pelican-themes/taman"             # +Maybe L:MIT
# THEME = "../pelican-themes/tuxlite_tbs"       # +Maybe L:WTFPL
# THEME = "../pelican-themes/tuxlite_zf"        # +Maybe L:MIT
# THEME = "../pelican-themes/voidy-bootstrap"   # +Nice L:MIT
# THEME = "../pelican-themes/zurb-F5-basic"     # +Nice L:WTFPL
# THEME = "../pelican-themes/bootlex"           # +Nice, but narrow L:Apache
# THEME = "../pelican-themes/MinimalXY"         # +Nice. L:MIT
# THEME = "../pelican-themes/bricks"            # +Nifty scrolling L:WTFPL
# THEME = "../pelican-themes/built-texts"       # +Really close L:MIT
# THEME = "../pelican-themes/cebong"            # +Similar to blueidea L:WTFPL
# THEME = "../pelican-themes/medius"            # +Worth a closer look L:MIT
