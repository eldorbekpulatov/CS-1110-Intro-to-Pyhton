# lab12.py
# YOUR NAME(S) AND NETID(S) HERE
# DATE COMPLETED HERE
"""Loop invariant functions"""


def num_space_runs(s):
    """Returns: The number of runs of spaces in the string s.
    
    A run is a collection of adjacent spaces.  We need a non-space character
    in-between to break up runs.
    
    Example: num_space_runs('  a  f   g    ') returns 4
             num_space_runs('a  f   g') returns 2
             num_space_runs('  a  bc   d') returns 3
    
    Parameter s: The string to parse
    Precondition: s is a nonempty string with letters and spaces"""
    # PUT THE INITIALIZATION CODE HERE
    n=0
    i=0

    if s[0]==" ":
        n+=1
    # invariant: s[0..i] contains n runs of spaces
    # PUT THE WHILE LOOP HERE
    while i<=len(s)-2:
        if s[i]!=" " and s[i+1]==" ":
            n+=1
        i+=1
    # post: s[0..len(s)-1] contains n runs of spaces
    # PUT THE RETURN STATEMENT HERE
    return n

def split(s):
    """Returns: Returns a list of works (separated by spaces) in s
    
    Words are indicated by spaces; there is always a space after each word.
    
    Example: split('a b c d ') returns ['a','b','c','d']
             split('a ') returns ['a']
    
    Parameter s: The string to parse
    Precondition: s is a nonempty string with no adjacent spaces.  There is 
    no space at the beginning, but there is a single space at the end"""
    # PUT THE INITIALIZATION CODE HERE
    result=[]
    pos=0
    word=""

    # invariant: result contains the words in s[0..pos-1], and s[pos-1] is a space
    # PUT THE WHILE LOOP HERE
    while pos!=len(s):
        if s[pos] !=" ":
            word=word+s[pos]   
        else:
            result.append(word)
            word=''
        pos+=1
    # post: result contains the words in s[0..len(s)-1], and s[len(s)-1] is a space
    # PUT THE RETURN STATEMENT HERE
    return result