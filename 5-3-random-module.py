#!/usr/bin/python
#
# https://wikidocs.net/79

import random

print 'random.random() = {}'.format(random.random())
print 'random.randrange(1,7) = {}'.format(random.randrange(1,7))
print 'random.rangrange(1,7) = {}'.format(random.randrange(1,7))
print 'range(1,7) = {}'.format(range(1,7))

abc = ['a','b','c','d','e']
random.shuffle(abc)
print 'random.shuffle(abc) = {}'.format(abc)
random.shuffle(abc)
print 'random.shuffle(abc) = {}'.format(abc)

abc = ['e','d','a','c','b']
print 'random.choice(abc) = {}'.format(random.choice(abc))
print 'random.choice(abc) = {}'.format(random.choice(abc))

print 'random.choice([True, False]) = {}'.format(random.choice([True, False]))
print 'random.choice([True, False]) = {}'.format(random.choice([True, False]))