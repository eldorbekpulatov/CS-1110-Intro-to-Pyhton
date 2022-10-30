# lab07.py
# Eldor Bekpulatov (eb654)
# Initial skeleton by W. White (WMW2)
# October 7, 2015
"""Functions for Lab 7"""


def lesser_than(thelist,value):
    """Returns:  number of elements in thelist strictly less than value
    
    Example:  lesser_than([5, 9, 1, 7], 6) evaluates to 2
    
    Parameter thelist: the list to check (WHICH SHOULD NOT BE MODIFIED)
    Precondition: thelist is a list of ints
    
    Parameter value:  the value to compare to the list
    Precondition:  value is an int"""
    
    num=0
    for x in thelist:
        if value>x:
            num+=1
    return num


def uniques(thelist):
    """Returns: The number of unique elements in the list. 
    
    Example: unique([5, 9, 5, 7]) evaluates to 3
    Example: unique([5, 5, 1, 'a', 5, 'a']) evaluates to 3
    
    Parameter thelist: the list to check (WHICH SHOULD NOT BE MODIFIED)
    Precondition: thelist is a list."""
    y=[]
    for x in thelist:
        if x not in y:
            y.append(x)
    return len(y)


def clamp(thelist,minn,maxx):
    """Modifies the list so that every element is between min and max.
    
    Any number in the list less than min is replaced with min.  Any number
    in the list greater than max is replaced with max. Any number between
    min and max is left unchanged.
    
    This is a PROCEDURE. It modified thelist, but does not return a new list.
    
    Example: if thelist is [-1, 1, 3, 5], then clamp(thelist,0,4) changes
    thelist to have [0,1,3,4] as its contents.
    
    Parameter thelist: the list to modify
    Precondition: thelist is a list of numbers (float or int)
    
    Parameter min: the minimum value for the list
    Precondition: min <= max is a number
    
    Parameter max: the maximum value for the list
    Precondition: max >= min is a number"""
    
    for x in thelist:
        if x<minn:
            thelist[thelist.index(x)]=minn
        
        if x>maxx:
            thelist[thelist.index(x)]=maxx
    return thelist
        