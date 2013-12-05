#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re

pattern = re.compile('"javascript:if\(confirm\(%27.*%27\)\)window\.location=%27(.*table_detail.*)%27"')


if __name__ == "__main__":

	path = "."
	if len(sys.argv) > 1:
		path = sys.argv[1]
	
	for abs_path, dir_name, filenames in os.walk(path):
		for filename in filenames:
			with open(abs_path + filename, "r") as f:
				html = f.read()
				result = pattern.findall(html)
				print result

