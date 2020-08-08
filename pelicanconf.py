#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime

SITEURL = 'http://localhost:8000'  # publishconf.py overrides
AUTHOR = 'West Lane Translator Inc.'
SITENAME = 'West Lane Translator Inc.'
SITETITLE = SITENAME
SITESUBTITLE = 'Serving the Central Oregon Coast since 1959'
SITELOGO = '/images/logo.png'
SITEDESCRIPTION = (
    "Information about West Lane Translator's HDTV and FM translators."
)
COPYRIGHT_NAME = AUTHOR
COPYRIGHT_YEAR = datetime.datetime.today().year
TIMEZONE = 'America/Los_Angeles'

PATH = 'content'
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
STATIC_PATHS = ['images', 'pdfs', 'extra']
DIRECT_TEMPLATES = []
ARTICLE_PATHS = []
ARCHIVES_SAVE_AS = ''
ARTICLE_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
DRAFT_SAVE_AS = ''
INDEX_SAVE_AS = ''
TAG_SAVE_AS = ''
OUTPUT_PATH = '../wlt_output/'

# The site is small, so ensure output is de-crufted.
DELETE_OUTPUT_DIRECTORY = False
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
    ( 'History', '/history.html' ),
    ( 'Governance', '/governance.html' ),
    ( 'Leasing', '/leasing.html' ),
    ( 'Membership', '/membership.html' ),
    ( 'Contact Us', '/contact-us.html' )
)
FOOTERMENUITEMS = (
    ( 'Terms and Conditions', '/terms-and-conditions.html' ),
    ( 'Privacy Policy', '/privacy-policy.html' )
)
ALT_CREDIT=''
ROBOTS = 'index, follow'
PAGES_SORT_ATTRIBUTE = 'menu'
FAVICON = '/images/favicon.ico'
THEME_COLOR = 'light'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True # Uses JavaScript

OG_TYPE = 'website'
JSONLD_TYPE = 'WebPage'

EXTRA_PATH_METADATA = {
    'extra/htaccess': {'path': '.htaccess'},
    'extra/htaccess_About': {'path': 'About/.htaccess'},
    'extra/htaccess_Donate': {'path': 'Donate/.htaccess'},
    'extra/htaccess_EAS': {'path': 'EAS/.htaccess'},
    'extra/htaccess_FAQ': {'path': 'FAQ/.htaccess'},
    'extra/htaccess_FM': {'path': 'FM/.htaccess'},
    'extra/htaccess_HDTV': {'path': 'HDTV/.htaccess'},
    'extra/htaccess_ISS': {'path': 'ISS/.htaccess'},
    'extra/htaccess_Introduction': {'path': 'Introduction/.htaccess'},
    'extra/htaccess_Tides': {'path': 'Tides/.htaccess'},
    'extra/htaccess_Tsunami': {'path': 'Tsunami/.htaccess'},
    'extra/htaccess_WX': {'path': 'WX/.htaccess'},
    'extra/htaccess_WXDisc': {'path': 'WXDisc/.htaccess'},
    'extra/htaccess_Webcam': {'path': 'Webcam/.htaccess'},
    'extra/htaccess_Webcams': {'path': 'Webcams/.htaccess'},
    'extra/htaccess_contact': {'path': 'contact/.htaccess'},
    'extra/htaccess_files': {'path': 'files/.htaccess'},
    'extra/htaccess_pages': {'path': 'pages/.htaccess'},
    'extra/htaccess_search': {'path': 'search/.htaccess'},
}
