# funcs.py
# Walker M. White (wmw2), Lillian Lee (ljl2)
# September 6, 2016
"""Functions for handling Strings

This module provides a few functions for manipulating strings.

These functions all have errors, and you must test them to find the errors.
This module is intended to prepare you for the first assignment.
"""


def has_a_vowel(s):
    """Returns: True if s has at least one vowel (a, e, i, o, or u)
    
    This function does not count y as a vowel.
    
    Parameter s: a string to check
    Precondition: s is a non-empty string with all lower case letters
    
    This function may include intentional errors."""
    return 'a' in s and 'e' in s and 'i' in s and 'o' in s and 'u' in s


def replace_first(word,a,b):
    """Returns: a copy of word with the FIRST instance of a replaced by b
    
    Example: replace_first('crane','a','o') returns 'crone'
    Example: replace_first('poll','l','o') returns 'pool'
    
    Parameter word: The string to copy and replace
    Precondition: word is a string
    
    Parameter a: The substring to find in word
    Precondition: a is a valid substring of word

    Parameter b: The substring to use in place of a
    Precondition: b is a string
    """
    pos = word.rfind(a)
    before = word[:pos]
    after  = word[pos+1:]
    result = before+b+after
    return result