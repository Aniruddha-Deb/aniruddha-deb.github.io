#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Aniruddha Deb'
SITENAME = 'Aniruddha Deb'
SITEURL = '/'
THEME = 'themes/Flex'
SITELOGO = '/extras/favicon/android-chrome-192x192.png'

PATH = 'content'
STATIC_PATHS = ['articles/2020/res', 'extras/favicon']
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'Posts'
ARTICLE_PATHS = ['articles'] # Any way of auto-adding year dates ?
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{slug}.html'
ARTICLE_URL = 'articles/{date:%Y}/{slug}.html'

EXTRA_PATH_METADATA = {
	'extras/favicon/favicon.ico': {'path': 'favicon.ico'}
}

TIMEZONE = 'Asia/Kolkata'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = []

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
