# lab11.py
# YOUR NAME(S) AND NETID(S) HERE
# DATE COMPLETED HERE
"""Loop functions for lab 11"""


def numberof(seq, v):
    """Returns: number of times v occurs in thelist.
    
    Parameter seq: list to search
    Precondition: seq is a list of ints
    
    Parameter v: value to search for
    Precondition: v is an int"""
    count = 0  # Accumulator
    k = 0      # Loop variable
         
    # IMPLEMENT A WHILE LOOP HERE
    while k<len(seq):
        if v==seq[k]:
            count+=1
        k+=1
    # END WHILE LOOP
    
    # Return result
    return count


def replace_copy(seq,a,b):
    """Returns: a COPY of thelist but with all occurrences of a replaced by b. 
    
    Example: replace([1,2,3,1], 1, 4) is [4,2,3,4].
        
    Parameter seq: list to search
    Precondition: seq is a list of ints
    
    Parameter a: value to search for
    Precondition: a is an int
    
    Parameter b: value to replace
    Precondition: b is an int"""
    copy = []  # Accumulator
    k = 0      # Loop variable
    
    # IMPLEMENT A WHILE LOOP HERE
    while k<len(seq):
        if a==seq[k]:
            copy.append(b)
        else:
            copy.append(seq[k])
        k+=1
    # END WHILE LOOP
    
    # Return result
    return copy


def replace(seq,a,b):
    """MODIFY thelist so that all occurrences of a replaced by b. 
    
    This function should have NO RETURN STATEMENT
    
    Example: if a = [1,2,3,1] then a becomes [4,2,3,4] after the
    function call replace(a,1,4).
        
    Parameter seq: list to search
    Precondition: seq is a list of ints
    
    Parameter a: value to search for
    Precondition: a is an int
    
    Parameter b: value to replace
    Precondition: b is an int"""
    # IMPLEMENT A WHILE LOOP HERE
    k=0
    while k<len(seq):
        if a==seq[k]:
            seq.pop(k)
            seq.insert(k, b)
        else:
            k+=1
    # END WHILE LOOP

# OPTIONAL FUNCTION
def exp(x,err=1e-6):
    """Returns: the value of (e ** x) to with the given margin of error.
    
    Do NOT return (math.E ** x).  This function is more exact that that answer.
    
    The value (e ** x) is given by the Power Series
    
        1 + x + (x ** 2)/2 + (x ** 3)/3! + ... + (x ** n)/ n! + ...
    
    We cannot add up infinite values in a program.  So we APPROXIMATE (e ** x)
    by choosing a value n and stopping at that:
    
        1 + x + (x ** 2)/2 + (x ** 3)/3! + ... + (x ** n)/ n!
    
    The error of this approximation is 
    
        abs( (x ** (n+1))/(n+1)!)
    
    which we want less than err.  So to compute e ** x, we just keep computing
    term = (x ** n)/ n! in a loop until this value is less than our error.  If it 
    is not less than the error, we add it to the accumulator, which we return at 
    the end.
    
    Hint: (x**(n+1))/(n+1)!  == (x**n)/n! * x/(n+1)
    Use this fact to simplify your loop.
    
    Parameter x: the exponent for e ** x
    Precondition: x is a numbers
    
    Parameter err: The margin of error (OPTIONAL: default is e-6)
    Precondition: err > 0 is a number"""
    approx = 0.0  # Approximation of e ** x
    term   = 1.0  # 1 is the first term in the Power Series
    n = 0         # term 1 corresponds to (x ** 0)/0!
    
    # IMPLEMENT A WHILE LOOP HERE
    
    # END WHILE LOOP
    
    # Return result
    return approx