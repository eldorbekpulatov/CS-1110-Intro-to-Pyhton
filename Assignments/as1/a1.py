# a1.py
# Eldor Bekpulatov (eb654)
#Camila Pretiz (cp573)
# Sept 9, 2016

import urllib2
"""Module for currency exchange

This module provides several string parsing
functions to implement a 
simple currency exchange routine using an online
currency service. 
The primary function in this module is exchange."""

def before_space(s):

    ''' Returns: Substring of s; up to, but not
    including, the first space

    Parameter s: the string to slice
    
    Precondition: s has at least one space in it'''

    ns=s.strip()
    before= ns[:ns.index(" ")]
    return before


def after_space(s):

    '''Returns: Substring of s after the first space

    Parameter s: the string to slice
    
    Precondition: s has at least one space in it'''

    ns=s.strip()
    af=ns[ns.index(" "):]
    after= af.strip()
    return after


def first_inside_quotes(s):
    
    """ Returns: The first substring of s between
    two(double) quote characters
    
    Parameter s: a string to search
    
    Precondition: s is a string with at least two
    (double) quote characters inside."""
    
    beg=s.index('"')
    mid=s[beg+1:]
    end=mid.index('"')
    res=mid[:end]
    return res 


def get_from(json):
    
    """"Returns: The FROM value in the response
    to a currency query.
    
    Parameter json: a json string to parse
    
    Precondition: json is the response to
    a currency query"""
    
    c=json.index(':')
    d=json[c:]
    e=first_inside_quotes(d)
    return e

    
def get_to(json):
    
    """Returns: The TO value in the response to
    a currency query.
    
    Parameter json: a json string to parse
    
    Precondition: json is the response to
    a currencyquery"""
    
    c=json.index('to')
    d=json[c:]
    e=d.index(':')
    f=d[e:]
    g=first_inside_quotes(f)
    return g


def has_error(json):
    
    '''Returns: True if the query has an error; False
    otherwise.
    
    Parameter json: a json string to parse
    
    Precondition: json is the response to a currency
    query'''
    
    x='true' in json 
    return not x


def currency_response(currency_from,
                      currency_to, amount_from):
    
    """Returns: a JSON string that is a response
    to a currency query.
    
    Parameter currency_from: the currency on
    hand
    
    Precondition: currency_from is a string
    
    Parameter currency_to: the currency to
    convertto
    
    Precondition: currency_to is a string
    
    Parameter amount_from: amount of currency to
    convert
    
    Precondition: amount_from is a float"""
    
    x=currency_from.upper()
    a=currency_to.upper()
    y=urllib2.urlopen('http://cs1110.cs.cornell.edu/'+
    '2016fa/a1server.php?from='+x.strip()+'&to='+
    a.strip()+'&amt='+str(amount_from))
    return y.read()


def iscurrency(currency):
    
    """Returns: True if currency is a valid
    (3 letter code for a) currency. 
    It returns False otherwise.

    Parameter currency: the currency code to verify
    
    Precondition: currency is a string."""
    
    v=currency_response(currency, 'USD', 1)
    c=has_error(v)
    return not c


def exchange(currency_from, currency_to,
                                            amount_from):
    """Returns: amount of currency received in the
    given exchange.
    
    The value returned has type float. 

    Parameter currency_from: the currency on hand

    Precondition: currency_from is a string for
    a valid currency code
    
    Parameter currency
    _to: the currency to
    convert to
    
    Precondition: currency_to is a string for
    a valid currency code
    
    Parameter amount_from: amount of currency
    to convert
    
    Precondition: amount_from is a float"""

    json=currency_response(currency_from,
                           currency_to, amount_from)
    s=get_to(json)
    ans=before_space(s)
    return float(ans)

