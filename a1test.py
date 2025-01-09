"""
Test script for module a1

When run as a script, this module invokes several procedures that
test the various functions in the module a1.

Author: Leepakshi Anand(la453) and Renee Gowda(rsg276)
Date: September 20, 2024
"""

import introcs
import a1

def testA():

    """
    Test procedure for Part A
    """
    print('Testing before_space')

    #tests for one space
    result = a1.before_space("hello ")
    introcs.assert_equals("hello",result)

    #tests for multiple separated spaces
    result = a1.before_space("1 2 3 4 5 6")
    introcs.assert_equals("1",result)

    #tests for an empty string
    result = a1.before_space(" ")
    introcs.assert_equals('',result)

    #tests for multiple continuous spaces
    result = a1.before_space("hi   bye")
    introcs.assert_equals("hi",result)

    print('Testing after_space')

    #tests for one space
    result = a1.after_space(" hello")
    introcs.assert_equals("hello",result)

    #tests for multiple separated spaces
    result = a1.after_space("1 2 3 4 5 6")
    introcs.assert_equals("2 3 4 5 6",result)

    #tests for an empty string
    result = a1.after_space(" ")
    introcs.assert_equals('',result)

    #tests for multiple continuous spaces
    result = a1.after_space("hi   bye")
    introcs.assert_equals("  bye",result)

    pass


def testB():

    print('Testing first_inside_quotes')

    #tests two character in double string surrounded by other character
    result = a1.first_inside_quotes('A "B C" B')
    introcs.assert_equals('B C', result)

    #tests multiple double quotes sections
    result = a1.first_inside_quotes('12"34"56"78"9')
    introcs.assert_equals('34', result)

    #tests special character space
    result = a1.first_inside_quotes('a"\"b')
    introcs.assert_equals('', result)

    #tests double quotes not surrounded by other character
    result = a1.first_inside_quotes('"hi"')
    introcs.assert_equals('hi', result)

    print('Testing slicing the string right after the key word src ' + \
      'for different inputs')

    stri1 = '{ "src":"Bitcoin", "dst":"Euros", "valid":true, "err":"" }'
    stri2 = '{ "src":"1 Big Bitcoin", "dst":"9916.0137 Euros", ' + \
    '"valid":false, "err":"Currency amount is invalid." }'
    stri3 = '{ "src":" ", "dst":" ", "valid":true, "err":"" }'
    stri4 = '{ "src":  "1672huq9qy", "dst":  "shbaja234", ' + \
    '"valid":true, "err":"" }'

    #testing only one word after src
    result1 = a1.get_src(stri1)
    introcs.assert_equals('Bitcoin',result1)

    #testing multiple words after src
    result2 = a1.get_src(stri2)
    introcs.assert_equals('1 Big Bitcoin',result2)

    #testing a blank quotation after src
    result7 = a1.get_src(stri3)
    introcs.assert_equals(" ",result7)

    #testing extra spaces after src
    result8 = a1.get_src(stri4)
    introcs.assert_equals("1672huq9qy",result8)

    print('Testing slicing the string right after the key word dst')

    #testing only one word after dst
    result3 = a1.get_dst(stri1)
    introcs.assert_equals('Euros',result3)

    #testing multiple words after dst
    result4 = a1.get_dst(stri2)
    introcs.assert_equals('9916.0137 Euros',result4)

    #testing a blank quotation after dst
    result9 = a1.get_dst(stri3)
    introcs.assert_equals(" ",result9)

    #testing extra spaces after dst
    result10 = a1.get_dst(stri4)
    introcs.assert_equals("shbaja234",result10)

    print('Testing the has error function')

    #testing where there is not an error
    result5 = a1.has_error(stri1)
    introcs.assert_equals(result5, False)

    #testing where there is an error
    result6 = a1.has_error(stri2)
    introcs.assert_equals(result6, True)


def testC():
    """
    Test procedure for Part C
    """

    print('Testing if it returns the correct response to a currency query')

    #testing a valid curency conversion
    result1 = a1.currency_response('USD', 'CUP', 2.5)
    introcs.assert_equals('{ "src":"2.5 United States Dollars", ' + \
                      '"dst":"64.375 Cuban Pesos", "valid":true, ' + \
                      '"err":"" }', result1)

    #testing an invalid currency conversion (both are invalid)
    result2 = a1.currency_response('LOL', 'OMG', 2.5)
    introcs.assert_equals('{ "src":"", "dst":"", "valid":false, ' + \
                      '"err":"Source currency code is invalid." }', result2)

    #testing an invalid currency conversion (first is valid, second is invalid)
    result3 = a1.currency_response('USD', 'OMG', 2.5)
    introcs.assert_equals('{ "src":"", "dst":"", "valid":false, ' + \
                      '"err":"Exchange currency code is invalid." }', result3)

    #testing an invalid currency conversion (first is invalid, second is valid)
    result4 = a1.currency_response('LOL', 'USD', 2.5)
    introcs.assert_equals('{ "src":"", "dst":"", "valid":false, ' + \
                      '"err":"Source currency code is invalid." }', result4)

    #testing when it has nothing
    result5 = a1.currency_response('', '', 2.5)
    introcs.assert_equals('{ "src":"", "dst":"", "valid":false, ' + \
                      '"err":"Source currency code is invalid." }', result5)


def testD():
    """
    Test procedure for Part D
    """

    print('Testing if it recognizes whether or not it is actual currency')

    #testing an actual currency
    result1 = a1.is_currency('USD')
    introcs.assert_equals(True, result1)

    #testing an actual currency
    result2 = a1.is_currency('CUP')
    introcs.assert_equals(True, result2)

    #testing a non-currency
    result3 = a1.is_currency('HAHA')
    introcs.assert_equals(False, result3),

    #testing a non-currency
    result4 = a1.is_currency('OMG')
    introcs.assert_equals(False, result4)

    print('Testing whether function exchange works')

    #testing if the exchange can work properly
    result5 = a1.exchange('USD', 'CUP', 2.5)
    introcs.assert_floats_equal(result5, 64.375)

testA()
testB()
testC()
testD()
print('Module a1 passed all tests.')
