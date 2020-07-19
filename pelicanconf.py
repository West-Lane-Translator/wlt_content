#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime

AUTHOR = 'West Lane Translator Inc.'
SITENAME = 'West Lane Translator Inc.'
SITESUBTITLE = 'Serving the Central Coast since 1959'
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

THEME = '../pelican-themes/Flex'                      # +Nav always on screen L:MIT
SITETITLE = SITENAME
SITELOGO = '../images/logo.png'
COPYRIGHT_NAME = AUTHOR
COPYRIGHT_YEAR = datetime.datetime.today().year
FAVICON = '../extra/faviconico'

THEME_COLOR = 'dark'
BROWER_COLOR = '#E0E0FF'

# THEME = "../pelican-themes/notebook"                  # +Nav always on screen L:Retain copyright

# THEME = "../pelican-themes/bootstrap2"                # +Good, header problem? L:Apache
# THEME = "../pelican-themes/blueidea"                  # +Good L:MIT
# THEME = "../pelican-themes/dev-random"                # +I like it L:WTFPL
# THEME = "../pelican-themes/elegant"                   # +It *is* elegant L:MIT
# THEME = "../pelican-themes/taman"                     # +Maybe L:MIT
# THEME = "../pelican-themes/tuxlite_tbs"               # +Maybe L:WTFPL
# THEME = "../pelican-themes/tuxlite_zf"                # +Maybe L:MIT
# THEME = "../pelican-themes/voidy-bootstrap"           # +Nice L:MIT
# THEME = "../pelican-themes/zurb-F5-basic"             # +Nice L:WTFPL
# THEME = "../pelican-themes/bootlex"                   # +Nice, but narrow L:Apache
# THEME = "../pelican-themes/MinimalXY"                 # +Nice. L:MIT
# THEME = "../pelican-themes/bricks"                    # +Nifty scrolling L:WTFPL
# THEME = "../pelican-themes/built-texts"               # +Really close L:MIT
# THEME = "../pelican-themes/cebong"                    # +Similar to blueidea L:WTFPL
# THEME = "../pelican-themes/medius"                    # +Worth a closer look L:MIT

# THEME = "../pelican-themes/notmyidea-cms"             # -L:Not found
# THEME = "../pelican-themes/simple-bootstrap"          # -L:Not found
# THEME = "../pelican-themes/aboutwilson"               # -L:Not found
# THEME = "../pelican-themes/backdrop"                  # -L:GPL
# THEME = "../pelican-themes/plumage"                   # -L:GPL

# THEME = "../pelican-themes/Nuja"                      # -NFG
# THEME = "../pelican-themes/Responsive-Pelican"        # -NFG
# THEME = "../pelican-themes/apricot"                   # -NFG
# THEME = "../pelican-themes/bricabrac"                 # -NFG
# THEME = "../pelican-themes/burrito"                   # -NFG
# THEME = "../pelican-themes/buruma"                    # -NFG
# THEME = "../pelican-themes/eevee"                     # -NFG
# THEME = "../pelican-themes/foundation-default-colours"# -NFG
# THEME = "../pelican-themes/free-agent"                # -NFG
# THEME = "../pelican-themes/irfan"                     # -NFG
# THEME = "../pelican-themes/lab"                       # -NFG
# THEME = "../pelican-themes/minimalX"                  # -NFG
# THEME = "../pelican-themes/ops"                       # -NFG
# THEME = "../pelican-themes/pelican-bootstrap3"        # -NFG
# THEME = "../pelican-themes/pelican-fh5co-marble"      # -NFG
# THEME = "../pelican-themes/pelican-twitchy"           # -NFG
# THEME = "../pelican-themes/pjport"                    # -NFG
# THEME = "../pelican-themes/sora"                      # -NFG
# THEME = "../pelican-themes/syte"                      # -NFG
# THEME = "../pelican-themes/twenty-html5up"            # -NFG
# THEME = "../pelican-themes/uikit"                     # -NFG
# THEME = "../pelican-themes/yapeme"                    # -NFG
# THEME = "../pelican-themes/SOB"                       # -amateur
# THEME = "../pelican-themes/brownstone"                # -awkward navigation
# THEME = "../pelican-themes/maggner-pelican"           # -bad layout
# THEME = "../pelican-themes/brutalist"                 # -blog centric
# THEME = "../pelican-themes/clean-blog"                # -blog centric and ugly
# THEME = "../pelican-themes/bootstrap"                 # -bootstrap2 better
# THEME = "../pelican-themes/BT3-Flat"                  # -boring
# THEME = "../pelican-themes/alchemy"                   # -boring
# THEME = "../pelican-themes/bulrush"                   # -boring
# THEME = "../pelican-themes/chunk"                     # -boring
# THEME = "../pelican-themes/nice-blog"                 # -boring
# THEME = "../pelican-themes/pelicanthemes-generator"   # -boring
# THEME = "../pelican-themes/waterspill"                # -boring
# THEME = "../pelican-themes/waterspill-en"             # -boring
# THEME = "../pelican-themes/sneakyidea"                # -broken blueidea
# THEME = "../pelican-themes/subtle"                    # -broken blueidea
# THEME = "../pelican-themes/html5-dopetrope"           # -dense, no navigation
# THEME = "../pelican-themes/notmyidea-cms-fr"          # -french
# THEME = "../pelican-themes/svbhack"                   # -inelegant
# THEME = "../pelican-themes/blue-penguin"              # -narrow
# THEME = "../pelican-themes/mnmlist"                   # -nav at bottom
# THEME = "../pelican-themes/monospace"                 # -nav at bottom
# THEME = "../pelican-themes/nmnlist"                   # -nav at bottom
# THEME = "../pelican-themes/bootstrap2-dark"           # -neon!
# THEME = "../pelican-themes/dev-random2"               # -no
# THEME = "../pelican-themes/franticworld"              # -no
# THEME = "../pelican-themes/graymill"                  # -no
# THEME = "../pelican-themes/materialistic"             # -no
# THEME = "../pelican-themes/relapse"                   # -no
# THEME = "../pelican-themes/Casper2Pelican"            # -no navigation
# THEME = "../pelican-themes/Just-Read"                 # -no navigation
# THEME = "../pelican-themes/SoMA"                      # -no navigation
# THEME = "../pelican-themes/SoMA2"                     # -no navigation
# THEME = "../pelican-themes/attila"                    # -no navigation
# THEME = "../pelican-themes/bluegrasshopper"           # -no navigation
# THEME = "../pelican-themes/chameleon"                 # -no navigation
# THEME = "../pelican-themes/cid"                       # -no navigation
# THEME = "../pelican-themes/dev-random3"               # -no navigation
# THEME = "../pelican-themes/fresh"                     # -no navigation
# THEME = "../pelican-themes/genus"                     # -no navigation
# THEME = "../pelican-themes/hyde"                      # -no navigation
# THEME = "../pelican-themes/iris"                      # -no navigation
# THEME = "../pelican-themes/jesuislibre"               # -no navigation
# THEME = "../pelican-themes/jojo"                      # -no navigation
# THEME = "../pelican-themes/lannisport"                # -no navigation
# THEME = "../pelican-themes/lazystrap"                 # -no navigation
# THEME = "../pelican-themes/lovers"                    # -no navigation
# THEME = "../pelican-themes/martin-pelican"            # -no navigation
# THEME = "../pelican-themes/martyalchin"               # -no navigation
# THEME = "../pelican-themes/material"                  # -no navigation
# THEME = "../pelican-themes/medio"                     # -no navigation
# THEME = "../pelican-themes/mediumfox"                 # -no navigation
# THEME = "../pelican-themes/mg"                        # -no navigation
# THEME = "../pelican-themes/nest"                      # -no navigation
# THEME = "../pelican-themes/nikhil-theme"              # -no navigation
# THEME = "../pelican-themes/niu-x2"                    # -no navigation
# THEME = "../pelican-themes/octopress"                 # -no navigation
# THEME = "../pelican-themes/pelican-blue"              # -no navigation
# THEME = "../pelican-themes/pelican-cait"              # -no navigation
# THEME = "../pelican-themes/pelican-hss"               # -no navigation
# THEME = "../pelican-themes/pelican-mockingbird"       # -no navigation
# THEME = "../pelican-themes/pelican-simplegrey"        # -no navigation
# THEME = "../pelican-themes/pelican-sober"             # -no navigation
# THEME = "../pelican-themes/pelican-striped-html5up"   # -no navigation
# THEME = "../pelican-themes/photowall"                 # -no navigation
# THEME = "../pelican-themes/pujangga"                  # -no navigation
# THEME = "../pelican-themes/pure"                      # -no navigation
# THEME = "../pelican-themes/resume"                    # -no navigation
# THEME = "../pelican-themes/semantic-ui"               # -no navigation
# THEME = "../pelican-themes/smoothie"                  # -no navigation
# THEME = "../pelican-themes/storm"                     # -no navigation
# THEME = "../pelican-themes/sundown"                   # -no navigation
# THEME = "../pelican-themes/svbtle"                    # -no navigation
# THEME = "../pelican-themes/voce"                      # -no navigation
# THEME = "../pelican-themes/w3-personal-blog"          # -no navigation
# THEME = "../pelican-themes/water-iris"                # -no navigation
# THEME = "../pelican-themes/crowsfoot"                 # -no!
# THEME = "../pelican-themes/gum"                       # -not a good fit
# THEME = "../pelican-themes/neat"                      # -not neat
# THEME = "../pelican-themes/bold"                      # -ransomware?
# THEME = "../pelican-themes/basic"                     # -too far off
# THEME = "../pelican-themes/lightweight"               # -too far off
# THEME = "../pelican-themes/new-bootstrap2"            # -weird layout
