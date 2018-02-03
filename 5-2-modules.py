#!/usr/bin/python
#
# https://wikidocs.net/78

import os

for key in os.environ:
    print key, '=', os.environ[key]
