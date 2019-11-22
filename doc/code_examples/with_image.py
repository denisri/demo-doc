'''
Example with image
==================

Another illustration.
'''

from __future__ import print_function
from sample_module.mod1 import Class1
from matplotlib import pyplot

c = Class1()
r = c.a_method(1., 2., 3)
print(r)

pyplot.plot([1,2,3], [2.5, 0.5, 4.6])

