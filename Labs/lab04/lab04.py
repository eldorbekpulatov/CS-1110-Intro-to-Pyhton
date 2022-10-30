# lab04.py
# <YOUR NAME HERE>
# <DATE HERE>
"""Unit test to test the module funcs.py"""

import cornelltest      # For assert_equals and assert_true
import funcs            # This is what we are testing


def test_asserts():
    """This is a simple test procedure to help you understand how assert works"""
    print 'Testing the cornelltest asserts'
    cornelltest.assert_equals('b c', 'ab cd'[1:4])
    #cornelltest.assert_equals('b c', 'ab cd'[1:3])     # UNCOMMENT ONLY WHEN DIRECTED
    
    cornelltest.assert_true(3 < 4)
    cornelltest.assert_equals(3, 1+2)
    
    cornelltest.assert_equals(3.0, 1.0+2.0)
    cornelltest.assert_floats_equal(6.3, 3.1+3.2)
    #cornelltest.assert_equals(6.3, 3.1+3.2)            # UNCOMMENT ONLY WHEN DIRECTED


# SCRIPT CODE (Call Test Procedures here)
test_asserts()
print 'Module funcs is working correctly'