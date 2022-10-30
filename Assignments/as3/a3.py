# a3.py
# Camila Pretiz (cp573) and Eldor Bekpulatov (eb654)
# 10/06/2016
""" Functions for Assignment A3"""

import colormodel
import math

def complement_rgb(rgb):
    """Returns: the complement of color rgb.
    
    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object"""
    complement = colormodel.RGB(255-rgb.red, 255-rgb.green, 255-rgb.blue)
    return complement


def round(number, places):
    """Returns: the number rounded to the given number of decimal places.
    
    The value returned is a float.
    
    This function is more stable than the built-in round.  The built-in round
    has weird behavior where round(100.55,1) is 100.5 while round(100.45,1) is
    also 100.5.  We want to ensure that anything ending in a 5 is rounded UP.
    
    It is possible to write this function without the second precondition on
    places. If you want to do that, we leave that as an optional challenge.
    
    Parameter number: the number to round to the given decimal place
    Precondition: number is an int or float
    
    Parameter places: the decimal place to round to
    Precondition: places is an int; 0 <= places <= 3"""
    # To get the desired output, do the following
    #   1. Shift the number "to the left" so that the position to round to is
    #      left of the decimal place.  For example, if you are rounding 100.556
    #      to the first decimal place, the number becomes 1005.56.  If you are
    #      rounding to the second decimal place, it becomes 10055.6.  If you
    #      are rounding 100.556 to the nearest integer, it remains 100.556.
    x = number*10**(places)
    #   2. Add 0.5 to this number
    x = x + 0.5
    #   3. Convert the number to an int, cutting it off to the right of the
    #      decimal.
    x = int(x)
    #   4. Shift the number back "to the right" the same amount that you did to
    #      the left. Suppose that in step 1 you converted 100.556 to 1005.56.
    #      In this case, divide the number by 10 to put it back.
    result = float(x)/float(10**(places))
    return result


def str5(value):
    """ Returns: value as a string, but expand or round to be exactly 5
    characters.
    
    The decimal point counts as one of the five characters.
   
    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.
    
    Parameter value: the number to conver to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360."""
    # Note:Obviously, you want to use the function round() that you just
    # defined. 
    # However, remember that the rounding takes place at a different place
    # depending on how big value is. Look at the examples in the specification.
    x = float(value)
    dot = str(x).index(".")
    places = 5-(dot+1)
    result = round(x, places)
    if len(str(result))<5:
        result = str(result) + '0'*(5-len(str(result)))
    return str(result)


def str5_cmyk(cmyk):
    """Returns: String representation of cmyk in the form "(C, M, Y, K)".
    
    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)
    
    Example: if str(cmyk) is 
    
          '(0.0,31.3725490196,31.3725490196,0.0)'
    
    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces
    after the commas. These must be there.
    
    Parameter cmtk: the color to convert to a string
    Precondition: cmyk is an CMYK object."""
    string = str(cmyk)
    x = string.index("(")
    z = string.index(",")
    c = str5(float(string[x+1:z]))
    string = string[z+1:]
    z = string.index(",")
    m = str5(float(string[:z]))
    string = string[z+1:]
    z = string.index(",")
    y = str5(float(string[:z]))
    string = string[z+1:]
    k = str5(float(string[:-1]))
    result = '(' + c + ', ' + m + ', ' + y + ', ' + k + ')'
    return result


def str5_hsv(hsv):
    """Returns: String representation of hsv in the form "(H, S, V)".
    
    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)
    
    Example: if str(hsv) is 
    
          '(0.0,0.313725490196,1.0)'
    
    then str5_hsv(hsv) is '(0.000, 0.314, 1.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter hsv: the color to convert to a string
    Precondition: hsv is an HSV object."""
    string = str(hsv)
    x = string.index("(")
    z = string.index(",")
    h = str5(float(string[x+1:z]))
    string = string[z+1:]
    z = string.index(",")
    s = str5(float(string[:z]))
    string = string[z+1:]
    v = str5(float(string[:-1]))
    result = '(' + h + ', ' + s + ', ' + v + ')'
    return result


def rgb_to_cmyk(rgb):
    """Returns: color rgb in space CMYK, with the most black possible.
    
    Formulae from en.wikipedia.org/wiki/CMYK_color_model.
    
    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object"""
    # The RGB numbers are in the range 0..255.
    # Change the RGB numbers to the range 0..1 by dividing them by 255.0.
    c = 1 - (rgb.red/255.0)
    m = 1 - (rgb.green/255.0)
    y = 1 - (rgb.blue/255.0)
    if c == 1.0 and m == 1.0 and y == 1.0:
        c = 0
        m = 0
        y = 0
        k = 1.0
    else:
        k = min(c, m, y)
        c = (c-k)/(1-k)
        m = (m-k)/(1-k)
        y = (y-k)/(1-k)
    c = c*100
    m = m*100
    y = y*100
    k = k*100
    v = colormodel.CMYK(c, m, y, k)
    return v #result


def cmyk_to_rgb(cmyk):
    """Returns : color CMYK in space RGB.

    Formulae from en.wikipedia.org/wiki/CMYK_color_model.
   
    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object."""
    # The CMYK numbers are in the range 0.0..100.0.  Deal with them in the 
    # same way as the RGB numbers in rgb_to_cmyk()
    c = cmyk.cyan/100.0
    m = cmyk.magenta/100.0
    y = cmyk.yellow/100.0
    k = cmyk.black/100.0
    r = int(round(((1-c)*(1-k)*255.0), 0))
    g = int(round(((1-m)*(1-k)*255.0), 0))
    b = int(round(((1-y)*(1-k)*255.0), 0))
    result = colormodel.RGB(r, g, b)
    return result


def rgb_to_hsv(rgb):
    """Return: color rgb in HSV color space.

    Formulae from wikipedia.org/wiki/HSV_color_space.
   
    Parameter rgb: the color to convert to a HSV object
    Precondition: rgb is an RGB object"""
    # The RGB numbers are in the range 0..255.
    # Change them to range 0..1 by dividing them by 255.0.
    r = rgb.red/255.0
    g = rgb.green/255.0
    b = rgb.blue/255.0
    MAX = max(r, g, b)
    MIN = min(r, g, b)
    if MAX == MIN:
        h = 0
    elif MAX == r and g>=b:
        h = 60.0 * (g - b) / (MAX - MIN)
    elif MAX == r and g<b:
        h = 60.0 * (g - b) / (MAX - MIN) + 360.0
    elif MAX == g:
        h = 60.0 * (b - r) / (MAX - MIN) + 120.0
    elif MAX == b:
        h = 60.0 * (r - g) / (MAX - MIN) + 240.0
    if MAX == 0:
        s = 0
    else:
        s = 1- MIN/MAX
    v = MAX
    hsv = colormodel.HSV(h, s, v)
    return hsv #result


def hsv_to_rgb(hsv):
    """Returns: color in RGB color space.
    
    Formulae from http://en.wikipedia.org/wiki/HSV_color_space.
    
    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object."""
    H = hsv.hue
    S = hsv.saturation
    V = hsv.value
    Hi = math.floor(H/60)
    f = H/60 - Hi
    p = V *(1-S)
    q = V * (1 - (f*S))
    t = V * (1-(1-f)*S)
    if Hi == 0:
        R = V
        G = t
        B = p
    if Hi == 1:
        R = q
        G = V
        B = p
    if Hi == 2:
        R = p 
        G = V
        B = t
    if Hi == 3:
        R = p 
        G = q
        B = V
    if Hi == 4:
        R = t
        G = p
        B = V
    if Hi == 5:
        R = V
        G = p 
        B = q
    R = int(round(R*255.0, 0))
    G = int(round(G*255.0, 0))
    B = int(round(B*255.0, 0))
    result = colormodel.RGB(R, G, B)
    return result
