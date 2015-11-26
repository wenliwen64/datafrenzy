#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Liwen Wen'
SITENAME = 'DataFrenzy'
SITEURL = 'http://localhost:18000'# if left empty, it will be not possible to go back to homepage by clicking the 'Home' button

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
	('weibo', 'http://www.weibo.com/u/1872791672'), 
	('facebook', 'https://www.facebook.com/liwen.wen.581'),
	('twitter', 'https://twitter.com/liwenPhys'),
	('email', 'mailto:wenliwen64@gmail.com')
	)

DEFAULT_PAGINATION = 10

THEME = 'pelican-themes/elegant'
PLUGIN_PATHS = ['pelican-plugins']

# elegant theme configuration items
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'render_math']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images', 'plots', 'data', ]
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

#RECENT_ARTICLES_COUNT (integer)  
"""
COMMENTS_INTRO ('string')
SITE_LICENSE ('string')
SITE_DESCRIPTION ('string')
EMAIL_SUBSCRIPTION_LABEL ('string')
EMAIL_FIELD_PLACEHOLDER ('string')
SUBSCRIBE_BUTTON_TITLE ('string')
MAILCHIMP_FORM_ACTION ('string')
SITESUBTITLE ('string')
"""
#LANDING_PAGE_ABOUT = ({'title': 'About', 'details':'I am a PhD student at UCLA. I am a enthusastic learner for new things... '})
SITESUBTITLE = 'Collection of study notes on programming, statistics, data science and beyond...'
#PROJECTS ([{},...])
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
#TEMPLATE_PAGES = {'src/books.html': 'dest/books.html',
#                  'src/resume.html': 'dest/resume.html',
#                  'src/contact.html': 'dest/contact.html'}
USE_FOLDER_AS_CATEGORY = False

#

# default metadata
#DEFAULT_METADATA = {'status':'draft',}
