# test11.py
# Lillian Lee (LJL2) and Walker White (wmw2)
# November 9, 2014
"""Test cases for lab11.py"""

import cornelltest
import lab11

def test_numberof():
    """Test the function numberof"""
    print '  Testing numberof'
    mylist = [5, 3, 3455, 74, 74, 74, 3]
    cornelltest.assert_equals(3, lab11.numberof(mylist,74))
    cornelltest.assert_equals(2, lab11.numberof(mylist,3))
    cornelltest.assert_equals(0, lab11.numberof(mylist,4))
    cornelltest.assert_equals(1, lab11.numberof([4],4))
    cornelltest.assert_equals(0, lab11.numberof([],4))
    print '  numberof looks okay'


def test_replace_copy():
    """Test the function replace_copy"""
    print '  Testing replace_copy'
    cornelltest.assert_equals([4], lab11.replace_copy([5],5,4))
    cornelltest.assert_equals([], lab11.replace_copy([], 1, 2))
    mylist = [5, 3, 3455, 74, 74, 74, 3]
    cornelltest.assert_equals([5, 20, 3455, 74, 74, 74, 20], lab11.replace_copy(mylist,3, 20))
    cornelltest.assert_equals([5, 3, 3455, 74, 74, 74, 3], lab11.replace_copy(mylist, 1, 3))
    print '  replace_copy looks okay'


def test_replace():
    """Test the function replace"""
    print '  Testing replace'
    mylist = [5]
    lab11.replace(mylist,5,4)
    cornelltest.assert_equals([4], mylist)
    
    mylist = []
    lab11.replace(mylist,1,2)    
    cornelltest.assert_equals([], mylist)
    
    mylist = [5, 3, 3455, 74, 74, 74, 3]
    lab11.replace(mylist, 3, 20)
    cornelltest.assert_equals([5, 20, 3455, 74, 74, 74, 20], mylist)
    
    lab11.replace(mylist, 1, 3)
    cornelltest.assert_equals([5, 20, 3455, 74, 74, 74, 20], mylist)
    print '  replace looks okay'


def test_exp():
    """Test the function exp"""
    print '  Testing exp'
    cornelltest.assert_equals(2.71828,      round(lab11.exp(1),5))
    cornelltest.assert_equals(2.71828182846,round(lab11.exp(1,1e-12),11))
    cornelltest.assert_equals(0.13534,      round(lab11.exp(-2),5))
    cornelltest.assert_equals(0.13533528324,round(lab11.exp(-2,1e-12),11))
    cornelltest.assert_equals(2981.0,       round(lab11.exp(8,1e-1),0))
    cornelltest.assert_equals(2980.95799,   round(lab11.exp(8),5))
    cornelltest.assert_equals(2980.95798704173,round(lab11.exp(8,1e-12),11))
    print '  exp looks okay'

    
# Script Code
if __name__ == '__main__':
    print 'Testing while loops'
    test_numberof()
    test_replace_copy()
    test_replace()
    test_exp()
    print "Module lab11.py is working correctly"