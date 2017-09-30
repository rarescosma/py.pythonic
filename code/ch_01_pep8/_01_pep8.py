# ******** Part 1 - Imports **************************
# BAD: import sys, os, multiprocessing
# BAD: from statistics import *

# GOOD
import collections
import os
import multiprocessing
import sys
from statistics import mean
from os import path, chmod, chown

# But multiple symbols are OK

#  Imports should be grouped in the following order:
#
#     standard library imports
#     related third party imports
#     local application/library specific imports
#
# You should put a blank line between each group of imports.

# There meaningless lines are here to prevent PyCharm from warning about
# unused imports and such. We want to see real warnings only. In a
# legitimate app, those other warnings would be useful but not here.
s = sys
o = os
m = multiprocessing
zp = path
zm = chmod
zo = chown
sm = mean
c = collections


# ******** Part 2 - code layout **************************
class AClass:
    def m1(self):
        pass

    def m2(self):
        pass

    def m3(self):
        pass


def some_method(a1, a2, a3):
    """
    some_method returns the larger of a1 or a2
    if a3 is True, then the smaller of a1 or a2 is returned

    :param a1: First item to compare
    :param a2: Second item to compare
    :param a3: Should reverse
    :return: a1 or a2
    """
    smaller = a1
    larger = a2
    if a1 > a2:
        smaller = a2
        larger = a1

    return [smaller if a3 else larger]

print(some_method(3, 1, True))


def other_method():
    pass


def other_method2():
    pass


def other_method3():
    pass


st = "Text"


# Use 4 spaces per indentation level.
# spaces, never tabs
def method():
    four_spaces_indented = True
    more_vars = 1

    return four_spaces_indented + more_vars


# Limit all lines to a maximum of 79 characters.
text = "This is a string which is longer than 79 characters. This is not encouraged but will execute and run OK."

# blank lines
# Surround top-level function and class definitions with two blank lines.
# Method definitions inside a class are surrounded by a single blank line.
# Use blank lines in functions, sparingly, to indicate logical sections.

# ******** Part 3 - Naming conventions **************************

# Modules should have short, all-lowercase names. Underscores can be used
# in the module name if it improves readability.

# Class names should normally use the CapWords convention.

# Because exceptions should be classes, the class naming convention
# applies here. However, you should use the suffix "Error"

# Function names should be lowercase, with words separated by
# underscores as necessary to improve readability.

# Arguments
# Always use self for the first argument to instance methods.
# Always use cls for the first argument to class methods.

# If a function argument's name clashes with a reserved keyword,
# it is generally better to append a single trailing underscore rather
# than use an abbreviation or spelling corruption. Thus class_ is better than class

# Constants are usually defined on a module level and written in all capital
# letters with underscores separating words. Examples include MAX_OVERFLOW and
# TOTAL.
