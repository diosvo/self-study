"""
MODULES

48 - Intro to Modules
>>> import random

49 - from module import Explained
>>> from random import randint

Cons:
Because it's available directly, 
it's going to override any variables that we have of that name.

50 - How to Alias an import (import as)
>>> from random import randint as r

51 - Why you should NEVER import *
>>> from random import *
... from heapq import *
... print(dir())

`dir` will give us a ton of identifiers
"""

"""
52 - How to create a module
53 - sys.path and changing module paths
"""
print('------------------ Lesson 52 -> 54 ------------------')

# Python modules
from os.path import dirname
import sys

# Expand system path
sys.path.append(dirname(__file__) + "/modules/")

# Development modules
import utils

print(utils.sort_range([5, 9, 26]))
