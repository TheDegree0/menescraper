'''
MeneScraper is a big data project that monitors the social interactions of Meneame.
Copyright (C) 2015  Arnau Villoslada

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
'''

# -*- coding: utf-8 -*-

# Scrapy settings for meneame project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'meneame'

SPIDER_MODULES = ['meneame.spiders']
NEWSPIDER_MODULE = 'meneame.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'meneame (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'meneame.pipelines.MeneamePipeline': 100,
}

import sys
sys.path.append('CONFIGURE-ME: path-to-project-directory')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'menescraper.settings'
