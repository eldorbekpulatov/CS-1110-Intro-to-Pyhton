# a1test.py
# # Eldor Bekpulatov (eb654)
#Camila Pretiz (cp573)
# Sept 9, 2016

"""Unit test for module a1

When run as a script, this module invokes several
procedures that test the various functions
in the module a1."""

import cornelltest
import a1

def testA():
    # Test case 1
    result = a1.before_space('0.8963 Euros')
    cornelltest.assert_equals('0.8963', result)
    
    # Test case 2
    result = a1.after_space('0.8963 Euros')
    cornelltest.assert_equals('Euros', result)
    
    # Test case 3
    result=a1.before_space(" 0.8963 Euros")
    cornelltest.assert_equals("0.8963", result)
    
    # Test case 4
    result=a1.after_space(" 0.8963 Euros")
    cornelltest.assert_equals('Euros', result)
                          
    # Test case 5
    result=a1.before_space("  0.8963   Euros")
    cornelltest.assert_equals("0.8963", result)
    
    # Test case 6
    result=a1.after_space('  0.8963  Euros')
    cornelltest.assert_equals('Euros', result)
    
    
def testB():
    
    # Test case 1
    result=a1.first_inside_quotes('A "B C" D "E F" ')
    cornelltest.assert_equals('B C', result)
    
    #Test case 2
    result=a1.get_from('{"from":"2 United States '
    +'Dollars","to":"1.825936 Euros","success":' +
    'true,"error":""}')
    cornelltest.assert_equals('2 United States ' +
                              'Dollars', result)
    
    #Test case 3
    result=a1.get_from('{"from":"","to":"","success"'+
    ':false,"error":"Source currency code is invalid."}')
    cornelltest.assert_equals('', result)
    
    #Test case 4
    result=a1.get_to('{"from":"2 United States'+
    'Dollars","to":"1.825936 Euros","success":true,'+
    '"error":""}')
    cornelltest.assert_equals('1.825936 Euros',
                                                result)
    
    #Test case 5
    result=a1.get_to('{"from":"","to":"","success":'+
    'false,"error":"Source currency code is invalid."}')
    cornelltest.assert_equals('', result)
    
    #Test case 6
    result=a1.has_error('{"from":"","to":"","success"'+
    ':false,"error":"Source currency code is invalid."}')
    cornelltest.assert_equals(True, result)
    
    #Test case 7
    result=a1.has_error('{"from":"2 United States'+
    'Dollars","to":"1.825936 Euros","success":'+
    'true,"error":""}')
    cornelltest.assert_equals(False, result)
    

def testC():
    
    #Test case 1
    result=a1.currency_response('USD', "BOB", 3.5)
    cornelltest.assert_equals('{ "from" : "3.5 United'+
    ' States Dollars", "to" : "24.219951 Bolivian '+
    'Bolivianos", "success" : true, "error" : "" }',
    result)
    
    #Test case 2
    result=a1.currency_response("usd", "bob", 3.5)
    cornelltest.assert_equals('{ "from" : "3.5 United'+
    ' States Dollars", "to" : "24.219951 Bolivian '+
    'Bolivianos", "success" : true, "error" : "" }', result)
    
    #Test case 3
    result=a1.currency_response(" usd", " bob", 3.5)
    cornelltest.assert_equals('{ "from" : "3.5 United'+
    ' States Dollars", "to" : "24.219951 Bolivian'+
    ' Bolivianos", "success" : true, "error" : "" }', result)
    

def testD():
    
    # Test case 1
    result=a1.iscurrency(" ")
    cornelltest.assert_equals(False, result)
    
    # Test case 2
    result=a1.iscurrency(" usd ")
    cornelltest.assert_equals(True, result) 
    
    # Test case 3
    result=a1.iscurrency("USD")
    cornelltest.assert_equals(True, result) 
    
    # Test case 4
    result=a1.iscurrency("usd")
    cornelltest.assert_equals(True, result) 

    # Test case 5
    result=a1.iscurrency("USb")
    cornelltest.assert_equals(False, result)
    
    #Test case 6
    result=a1.exchange("USD", "UZS", 1)
    cornelltest.assert_floats_equal(2988.825, result)
    
     #Test case 7
    result=a1.exchange("USD", "Uzs", 1)
    cornelltest.assert_floats_equal(2988.825, result)
    
    #Test case 8
    result=a1.exchange(" usd ", " uzs ", 1)
    cornelltest.assert_floats_equal(2988.825, result)
    
    
testA()
testB()
testC()
testD()
    
print "Module a1 passed all tests"