#!/usr/bin/python
#
# https://wikidocs.net/82

f = open('/usr/share/doc/python2.7/README.Debian')
for i in range(1,7):
    print '{}: {}'.format(i, f.readline()),

print '...'

lines = f.readlines()
import sys
sys.stdout.writelines('last line is : {}'.format(lines[-1:]))
print