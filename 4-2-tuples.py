#!/usr/bin/python
#
# https://wikidocs.net/71

a = 10
b = 20
temp = a
a = b
b = temp
print a, b

c = 30
d = 40
c, d = d, c
print c, d

def magu_print(x, y, *rest):
    print x, y, rest
magu_print(1,2,3,5,6,7,9,10)


