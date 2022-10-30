# lab13.py
# YOUR NAME(S) AND NETID(S) HERE
# DATE COMPLETED HERE
"""Loop invariant functions"""


def swap(b,i,j):
    """Swaps the values b[i] and b[j]
    
    Parameter b: The list to swap inside
    Precondition: b is a list of anything
    
    Parameter i: The first position to swap
    Precondition: i is an int in 0..len(b)-1
    
    Parameter j: The second position to swap
    Precondition: j is an int in 0..len(b)-1
    """
    tmp = b[i]
    b[i] = b[j]
    b[j] = tmp


#### PART 1A ####

def minpos1(b,h,k):
    """Returns: the POSITION of the minimum value of the list b[h..k]
    
    This function does NOT modify the list b.
    
    Parameter b: The list to search for the minimum
    Precondition: b is a list of integers
    
    Parameter h: The place to start in the list
    Precondition: h is an int in 0..len(b)-1, h <= k
    
    Parameter k: The place to finish in the list
    Precondition: k is an int in 0..len(b)-1, h <= k
    """
    # PUT THE INITIALIZATION CODE HERE
    
    # inv: b[x] is minimum of b[w+1..k]
    # PUT THE WHILE LOOP HERE
    
    # post: b[x] is minimum of b[h..k]
    # PUT THE RETURN STATEMENT HERE


def minpos2(b,h,k):
    """Returns: the POSITION of the minimum value of the list b[h..k]
    
    This function does NOT modify the list b.
    
    Parameter b: The list to search for the minimum
    Precondition: b is a list of integers
    
    Parameter h: The place to start in the list
    Precondition: h is an int in 0..len(b)-1, h <= k
    
    Parameter k: The place to finish in the list
    Precondition: k is an int in 0..len(b)-1, h <= k
    """
    # PUT THE INITIALIZATION CODE HERE
    
    # inv: b[x] is minimum of b[h..r-1]
    # PUT THE WHILE LOOP HERE
    
    # post: b[x] is minimum of b[h..k]
    # PUT THE RETURN STATEMENT HERE


#### PART 1B ####

def fixedpartition1(b):
    """Returns: a position k indicating that the list b is partitioned about 6
    
    This function modifies the list b.  It modifies it so that everything in b[0..k]
    is <= 6 and everything in b[k+1..] is > 6.  When done with this modification,
    it returns the value k.
    
    Parameter b: The list to partition
    Precondition: b is a nonempty list of integers
    """
    # PUT THE INITIALIZATION CODE HERE
    
    # inv: b[0..k] <= 6 and b[t..] > 6
    # PUT THE WHILE LOOP HERE
    
    # post: b[0..k] <= 6 and b[k+1..] > 6
    # PUT THE RETURN STATEMENT HERE


def fixedpartition2(b):
    """Returns: a position k indicating that the list b is partitioned about 6
    
    This function modifies the list b.  It modifies it so that everything in b[0..k]
    is <= 6 and everything in b[k+1..] is > 6.  When done with this modification,
    it returns the value k.
    
    Parameter b: The list to partition
    Precondition: b is a nonempty list of integers
    """
    # PUT THE INITIALIZATION CODE HERE
    
    # inv: b[0..s-1] <= 6 and b[k+1..] > 6
    # PUT THE WHILE LOOP HERE
    
    # post: b[0..k] <= 6 and b[k+1..] > 6
    # PUT THE RETURN STATEMENT HERE


#### PART 2A ####

def partition2(b,h,k):
    """Returns: a position j indicating that the list b is partitioned about initial b[h]
    
    At the start, this function identifies x = b[h].  Then it modifies the list b.  It
    modifies it so that x is now at b[j] and everything in b[h..j-1] is <= x and
    everything in b[j+1..k] is >= x.  When done with this modification, it returns the 
    value j.
    
    Parameter b: The list to partition
    Precondition: b is a nonempty list of integers
    
    Parameter h: The start of the list
    Precondition: h is an int in 0..len(b)-1, h < k
    
    Parameter k: Then end of the list
    Precondition: h is an int in 0..len(b)-1, h < k
    """
    x = b[0]
    
    # PUT THE INITIALIZATION CODE HERE
    
    # inv: b[h..j-1] <= x = b[j] <= b[q+1..k], b[j+1..q] unknown
    # PUT THE WHILE LOOP HERE
    
    # post: b[h..j-1] <= x = b[j] <= b[j+1..k]
    # PUT THE RETURN STATEMENT HERE


def partition3(b,h,k):
    """Returns: a position j indicating that the list b is partitioned about initial b[h]
    
    At the start, this function identifies x = b[h].  Then it modifies the list b.  It
    modifies it so that x is now at b[j] and everything in b[h..j-1] is <= x and
    everything in b[j+1..k] is >= x.  When done with this modification, it returns the 
    value j.
    
    Parameter b: The list to partition
    Precondition: b is a nonempty list of integers
    
    Parameter h: The start of the list
    Precondition: h is an int in 0..len(b)-1, h < k
    
    Parameter k: Then end of the list
    Precondition: h is an int in 0..len(b)-1, h < k
    """
    x = b[0]
    
    # PUT THE INITIALIZATION CODE HERE
    
    # inv: b[h..j-1] <= x = b[j] <= b[j+1..n-1], b[n..] unknown
    # PUT THE WHILE LOOP HERE
    
    # post: b[h..j-1] <= x = b[j] <= b[j+1..k]
    # PUT THE RETURN STATEMENT HERE


#### PART 2B ####

def dnf2(b):
    """Returns: a tuple (i,j) indicating that the list b is organized in DNF format.
    
    This function modifies the list b.  It modifies it so that everything in b[0..i-1]
    is < 0, everythnng in b[i..j-1] is 0, and everything in b[j,..] is > 0. When done 
    with this modification, it returns the value (i,j).
    
    Parameter b: The list to partition
    Precondition: b is a nonempty list of integers
    """
    # PUT THE INITIALIZATION CODE HERE
    
    # inv: b[0..i-1] < 0, b[i..t-1] = 0, b[t..j-1] unknown, b[j..] > 0
    # PUT THE WHILE LOOP HERE
    
    # post: b[0..i-1] < 0, b[i..j-1] = 0, and b[j..] > 0


def dnf3(b):
    """Returns: a tuple (i,j) indicating that the list b is organized in DNF format.
    
    This function modifies the list b.  It modifies it so that everything in b[0..i-1]
    is < 0, everythnng in b[i..j-1] is 0, and everything in b[j,..] is > 0. When done 
    with this modification, it returns the value (i,j).
    
    Parameter b: The list to partition
    Precondition: b is a nonempty list of integers
    """
    # PUT THE INITIALIZATION CODE HERE
    
    # inv: b[0..s] < 0, b[s+1..i-1] unknown, b[i..j-1] = 0, b[j..] > 0
    # PUT THE WHILE LOOP HERE
    
    # post: b[0..i-1] < 0, b[i..j-1] = 0, and b[j..] > 0