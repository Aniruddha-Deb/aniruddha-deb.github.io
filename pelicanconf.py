#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Aniruddha Deb'
EMAIL_ID = 'aniruddha.deb.2002@gmail.com'
SITENAME = 'Aniruddha Deb'
SITEURL = 'https://www.aniruddhadeb.com'
THEME = 'themes/Flex'
SITELOGO = '/extras/sitelogo.png'

PATH = 'content'
STATIC_PATHS = ['pages', 'articles/2023/res', 'articles/2022/res', 'articles/2021/styles', 'articles/2021/res', 'articles/2020/res', 'extras']
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'Posts'
ARTICLE_EXCLUDES = ['articles/2023/res']
ARTICLE_PATHS = ['articles']
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{slug}.html'
ARTICLE_URL = 'articles/{date:%Y}/{slug}.html'
DEFAULT_METADATA = {
    'status': 'published',
}

EXTRA_PATH_METADATA = {
	'extras/favicon/favicon.ico': {'path': 'favicon.ico'},
	'extras/CNAME': {'path': 'CNAME'}
}

# Adding markdown extensions breaks pygments for some strange reason....
#MARKDOWN = {
#	"extension_configs" : {
#		'markdown.extensions.codehilite' : {},
#		"markdown.extensions.toc": {}
#	}
#}

TIMEZONE = 'Asia/Kolkata'
PYGMENTS_STYLE  = 'monokai'
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
LINKS = [('archives', '/archives.html'), ('categories', '/categories'), ('tags', '/tags'), ('website', 'https://www.cse.iitd.ac.in/~cs1200869')]

# Social widget
SOCIAL = (('github', 'https://www.github.com/Aniruddha-Deb'),
          ('stack-exchange', 'https://stackexchange.com/users/12827944/aniruddha-deb'),
		  ('goodreads-g', 'https://www.goodreads.com/aniruddhadeb'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
