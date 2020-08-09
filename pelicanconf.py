#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime
import inspect
import pathlib

# The Pelican settings are documented here:
#   https://docs.getpelican.com/en/stable/settings.html
# and the Flex theme's settings are documented here:
#   https://github.com/alexandrevicenzi/Flex/wiki/Custom-Settings

# I personally found it a pain to have a separate pelicanconf.py and
# publishconf.py mainly because it wasn't possible to use SITEURL in other
# things such as FAVICON and SITELOGO.  I instead just symlink pelicanconf.py
# to publishconf.py and use this little bit of ugliness to set a variable so
# the code can figure out if it is publishing or not:
PUBLISHING = __file__.endswith('publishconf.py')

# Pelican general site settings
SITEURL = 'https://westlanetv.org' if PUBLISHING else 'http://localhost:8000'
SITENAME = 'West Lane Translator Inc.'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

# The Flex theme can accommodate our non-blog site well and is MIT license
THEME = '../Flex'

# Flex general site settings
SITETITLE = SITENAME
SITESUBTITLE = 'Serving the Central Oregon Coast since 1959'
SITEDESCRIPTION = \
    "Information about West Lane Translator's HDTV and FM translators."
AUTHOR = 'West Lane Translator Inc.'
COPYRIGHT_NAME = AUTHOR
COPYRIGHT_YEAR = datetime.datetime.today().year
ROBOTS = 'index, follow'
FAVICON = SITEURL + '/images/favicon.ico'
SITELOGO = SITEURL + '/images/logo.png'
# Flex Dark Mode settings per:
#   https://github.com/alexandrevicenzi/Flex/wiki/Dark-Mode
THEME_COLOR = 'light'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True  # Uses JavaScript

# Enable some Markdown extensions.  The list of available extensions and
# documentation for them is available here:
#   https://python-markdown.github.io/extensions/
# For completeness, the basic Markdown syntax is documented here:
#   https://daringfireball.net/projects/markdown/syntax
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

# Tell Pelican where things come from and go to.
PATH = 'content'  # Keep content separate from how to build.
PAGE_PATHS = ['pages']  # Where to look in content subdirectory for our pages.
STATIC_PATHS = ['images', 'pdfs', 'extra']  # Copy things from these to output.
OUTPUT_PATH = '../wlt_output/'  # Where to put the output.
PAGE_URL = '{slug}.html'  # Output the HTML at the root instead of in pages/
PAGE_SAVE_AS = '{slug}.html'

# Configuring the menus is currently somewhat hacky.  The menu at the top of
# the page is enabled with MAIN_MENU and defined with MENUITEMS:
MAIN_MENU = True
MENUITEMS = (
    ( 'History', SITEURL + '/history.html' ),
    ( 'Governance', SITEURL + '/governance.html' ),
    ( 'Leasing', SITEURL + '/leasing.html' ),
    ( 'Membership', SITEURL + '/membership.html' ),
    ( 'Contact Us', SITEURL + '/contact-us.html' )
)
# The left side menu contains all the Markdown pages except for ones that have
# 'Status: Hidden' attribute in their metadata.  This means that any page that
# appears in the top or bottom menu should have that attribute in their
# Markdown so they don't appear in the left side menu as well.  To get the
# menu items in the preferred order, the new custom Menu attribute was put in
# the Markdown files.  Tell Flex to sort by that new attribute:
PAGES_SORT_ATTRIBUTE = 'menu'
# The menu at the bottom of the page is enabled with local changes to Flex:
FOOTERMENUITEMS = (
    ( 'Terms and Conditions', SITEURL + '/terms-and-conditions.html' ),
    ( 'Privacy Policy', SITEURL + '/privacy-policy.html' )
)

# I don't feel compelled to tell the world our site was built with
# Pelican and Flex.  This relies on local changes to Flex.
ALT_CREDIT=''

# Tell the world via the JSON-LD and Open Graph types that we are a
# website and not a blog.  These rely on local changes to Flex.
OG_TYPE = 'website'
JSONLD_TYPE = 'WebPage'

# This is a simple website and not a blog so disable all the bloggy stuff
DIRECT_TEMPLATES = []
ARCHIVES_SAVE_AS = ''
ARTICLE_PATHS = []
ARTICLE_SAVE_AS = ''
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
AUTHOR_SAVE_AS = ''
CATEGORY_FEED_ATOM = None
CATEGORY_SAVE_AS = ''
DEFAULT_PAGINATION = False
DISPLAY_CATEGORIES_ON_MENU = False
DRAFT_SAVE_AS = ''
FEED_ALL_ATOM = None
INDEX_SAVE_AS = ''
TAG_SAVE_AS = ''
TRANSLATION_FEED_ATOM = None

# The site is small, so rebuild it from scratch every time.
DELETE_OUTPUT_DIRECTORY = False
CACHE_CONTENT = False
LOAD_CONTENT_CACHE = False

# We want redirects of URLs from the old site to go to the new site
# URLs.  This is done with .htaccess files in subdirectories on the
# website as needed.  The source for these files is
# content/extra/htaccess* but we need Pelican to copy them to the
# right place in the output.  This is done via EXTRA_PATH_METADATA.
# Instead of building that manually, the following code automatically
# builds EXTRA_PATH_METADATA from the list of extra/htaccess* files.
# As an example, extra/htaccess_About will end up in About/.htaccess
# in the output.
EXTRA_PATH_METADATA = {}
path_path = pathlib.Path(PATH)
extra_path = path_path / "extra"
for hta in extra_path.glob('htaccess*'):
    rel_hta = pathlib.Path(*hta.parts[-2:])
    hta_loc = hta.name[len('htaccess'):]
    if not hta_loc:
        hta_loc = '.htaccess'
    else:
        assert hta_loc[0] == '_'
        hta_loc = hta_loc[1:] + '/.htaccess'
    EXTRA_PATH_METADATA[str(rel_hta)] = {'path': hta_loc}
