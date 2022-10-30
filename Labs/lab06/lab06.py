# lab06.py
# Eldor Bekpulatov (eb654)
# Initial skeleton by Walker White (wmw2)
# September 26, 2016
"""Module to demonstrate debugging and error handling.

This module contains several functions with bugs in it.  You are to
find and remove the bugs using the techniques that we talked about in
class.  

In addition, you will also add assert statements to this functions to
assert the (somewhat complex) precondition.  These assert statements
will be aided by the latter two functions in this module."""


# PART 1: DEBUGGING
def time_to_military(s):
    """ Returns: the time in 24-hour (military) format.
    
    24-hour format has the form '<hours>:<minutes>'. The hours are between 0 and 23, 
    and are always two digits (so there must be a leading zero).  The minutes are 
    between 0 and 59, and are always 2 digits.
    
    Examples:
        '2:45 PM' becomes '14:45'
        '9:05 AM' becomes '09:05'
        '12:00 AM' becomes '00:00'
    
    Parameter s: string representation of the time
    Precondition: s is a string in 12-format <hours>:<min> AM/PM"""
    # PART 2: Add assert statements here to enforce preconditions
    assert is_time_format(s)
    
    # Split up the string
    pos1 = s.index(':')
    pos2 = s.index(' ')
    
    # Extract hours and minutes
    hour = int(s[:pos1])
    mins = s[pos1+1:pos2]
    suff = s[pos2+1:]
    
    # Adjust hour to be correct.
    if (suff == 'PM') and (hour != 12):
        hour += 12
    if (suff=="PM") and (hour ==12):
        hour=12
    if (suff=="AM") and (hour==12):
        hour=0
    
    # Add a leading zero if necessary
    if (hour < 10):
        hour = '0'+str(hour)
    else:
        hour = str(hour)
    
    # Glue it back together
    return str(hour)+':'+mins


def time_to_minutes(s):
    """Returns: number of minutes since midnight
    
    Examples:
       '2:45 PM' => 14*60+45 = 885
       '9:05 AM' => 9*60+5 = 545
      '12:00 AM' => 0
    
    Parameter s: string representation of the time
    Precondition: s is a string in 12-format <hours>:<min> AM/PM"""
    # PART 2: Add assert statements here to enforce preconditions
    assert is_time_format
    # Find the separators
    pos1 = s.index(':')
    pos2 = s.index(' ')
    
    # Get hour and convert to int
    hour = s[:pos1]
    hour = int(hour)
    
    
    # Adjust hour to be correct.
    suff = s[pos2+1:]
    if (suff == 'PM' and hour !=12):
        hour +=12
    elif (suff == 'AM' and hour == 12):
        hour = 0
    
    # Get min and convert to int
    mins = s[pos1+1:pos2]
    mins = int(mins)
    
    
    return hour*60+mins


# PART 2: ASSERT HELPER
def is_time_format(s):
    """Returns: True if s is a string in 12-format <hours>:<min> AM/PM
    
    Example: 
        lab06.is_time_format('2:45 PM') returns True
        lab06.is_time_format('2:45PM') returns False
        lab06.is_time_format('14:45') returns False
        lab06.is_time_format('14:45 AM') returns False
        lab06.is_time_format(245) returns False
    
    Parameter s: the candidate time to format
    Precondition: NONE (s can be any value)"""
    # HINT: Your function must be prepared to do something if s is a string.
    # Even if s is a string, the first number before the colon may be one
    # or two digits.  You must be prepared for either.
    # You might find the method s.isdigit() to be useful.
    
    if (type(s)==str):
        #print s
        #check if it has a space after mins
        if (s.find(' ') !=-1 and s.find(':')!= -1):
            #print "has space and (:)"
        
    
            pos1 = s.index(':')
            pos2 = s.index(' ')
    
            # Get hour and convert to int
            hour = s[:pos1]
            hour = int(hour)
        
    
            # Get min and convert to int
            mins = s[pos1+1:pos2]
            mins = int(mins)
        
    
            #get suff
            suff= s[pos2+1:]
        

            #check if the hours make sense
            if (str(hour).isdigit() and hour<=12 and hour>= 0):
                #print "checked hours"
            
    
                #check if the mins make sense
                if (str(mins).isdigit() and mins<=59 and mins >= 0):
                    #print "checked mins"
                    return True
            
                else:
                    return False

            else:
                return False
        else:
            return False
    else:
        return False
    
    
        
        
    
    
# PART 3: TRY-EXCEPT
def something_to_military(s):
    """Returns: the time in 24-hour (military) format if appropriate.
    
    The function is the same as time_to_military if s satisfies the
    precondition for that function.  If s does not satisfy the precondition
    then this function returns 'Invalid time format'
    
    Examples: 
        something_to_military('2:45 PM') returns '14:45'
        something_to_military('9:05 AM') returns '09:05'
        something_to_military('12:00 AM') returns '00:00'
        something_to_military(905) returns 'Invalid time format'
        something_to_military('abc') returns 'Invalid time format'
        something_to_military('9:05') returns 'Invalid time format'
    
    Parameter s: the candidate time to format
    Precondition: NONE (s can be any value)"""
    # You are not allowed to use 'if' in this definition. Use try-except instead.
    # Hint: You have to complete PART 2 before you complete this part.
    try:
        x=time_to_military(s)
        return x
    except:
        return "Invalid time format"
