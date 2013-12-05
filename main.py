#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import urllib2

pattern = re.compile('''"javascript:if\(confirm\(.*\)\)window\.location=(?:'|%27)(.*table_detail.*)(?:'|%27)"''')

def download_file(url, path = "./"):

	with open(path + url.split('/')[-1], "w") as f:
		f.write(urllib2.urlopen(url).read())

if __name__ == "__main__":

	path = "./"
	if len(sys.argv) > 1:
		path = sys.argv[1]
	
	for abs_path, dir_name, filenames in os.walk(path):
		print abs_path
		for filename in filenames:
			with open(abs_path + "/" + filename, "r") as f:
				html = f.read()
				result = pattern.findall(html)
				for url in result:
					print "Downloading", url, "...",
					download_file(url, abs_path)
					print "done"
