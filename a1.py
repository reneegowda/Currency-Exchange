"""
Module for currency exchange

This module provides several string parsing functions to implement a
simple currency exchange routine using an online currency service.
The primary function in this module is exchange.

Author: Renee Gowda (rsg276) and Leepakshi Anand (la453)
Date: September 20th 2024
"""

import introcs


def before_space(s):
    """
    Returns a copy of s up to, but not including, the first space
    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    # Find the index of the first space in the string
    b = int(s.find(" "))

    # Slice the string from the beginning up to the space
    before = s[0:b]

    # Return the substring before the space
    return before


def after_space(s):
    """
    Returns a copy of s after the first space
    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    # Find the index of the first space and move one position ahead to start after the space
    a = int(s.find(" ")) + 1

    # Slice the string from the position after the space
    after = s[a:]

    # Return the substring after the space
    return after


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quotes

    A quote character is one that is inside a string, not one that
    delimits it.  We typically use single quotes (') to delimit a
    string if want to use a double quote character (") inside of it.

    Parameter s: a string to search
    Precondition: s is a string containing at least two double quotes
    """
    # Find the index of the first quote and add 1 to start extracting inside the quotes
    a = (s.index('\"')) + 1

    # Find the index of the second quote to determine the end of the quoted substring
    b = s.index('\"', a)

    # Slice the string to get the content inside the quotes
    quote = s[a:b]

    # Return the substring between the quotes
    return quote


def get_src(json):
    """
    Returns the src value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the keyword
    "src". For example, if the JSON is

    '{ "src":"1 Bitcoin", "dst":"9916.0137 Euros", "valid":true, "err":"" }'

    then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    # Find the index of the "src" keyword in the JSON string
    src_value = json.index('"src":')

    # Extract and return the value inside the quotes following the "src" keyword
    return first_inside_quotes(json[src_value+6:])


def get_dst(json):
    """
    Returns the dst value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the keyword
    "dst". For example, if the JSON is

    '{ "src":"1 Bitcoin", "dst":"9916.0137 Euros", "valid":true, "err":"" }'

    then this function returns '9916.0137 Euros' (not
    '"9916.0137 Euros"').

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    # Find the index of the "dst" keyword in the JSON string
    dst_value = json.index('"dst":')

    # Extract and return the value inside the quotes following the "dst" keyword
    return first_inside_quotes(json[dst_value+6:])


def has_error(json):
    """
    Returns True if the query has an error; False otherwise.

    Given a JSON response to a currency query, this returns the
    opposite of the value following the keyword "valid". For example,
    if the JSON is

    '{ "src":"", "dst":"", "valid":false, "err":"Currency amount is invalid." }'

    then the query is not valid, so this function returns True (It
    does NOT return the message 'Source currency code is invalid').

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    # Find the index of the "valid" keyword in the JSON string
    valid_pos = json.index('"valid":')

    # Extract the value after "valid", which is either 'true' or 'false'
    valid_value = json[valid_pos+8]

    # Check if the value is 'true' (converted to a boolean) and return the opposite (False if True)
    value = valid_value[0]
    temp = (value == 't')

    # Return the opposite of the validity check (True if error, False otherwise)
    return (temp != True)


def currency_response(old, new, amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency old to the
    currency new. The response should be a string of the form

    '{ "src":"<old-amt>", "dst":"<new-amt>", "valid":true, "err":"" }'

    where the values old-amount and new-amount contain the value
    and name for the original and new currencies. If the query is
    invalid, both old-amount and new-amount will be empty, while
    "valid" will be followed by the value false (and "err" will have
        an error message).

    Parameter old: the currency on hand (the SRC)
    Precondition: old is a string with no spaces or non-letters

    Parameter new: the currency to convert to (the DST)
    Precondition: new is a string with no spaces or non-letters

    Parameter amt: amount of currency to convert
    Precondition: amt is a float
    """
    # Build the query string with the given old, new, and amount values
    specs = "from=" + old + "&to=" + new + "&amt=" + str(amt)

    # Build the full URL for the query
    link = "http://cs1110.cs.cornell.edu/2024fa/a1?" + specs

    # Perform the query and return the response
    return introcs.urlread(link)


def is_currency(code):
    """
    Returns: True if code is a valid (3 letter code for a) currency
    It returns False otherwise.

    Parameter code: the currency code to verify
    Precondition: code is a string with no spaces or non-letters.
    """
    # Perform a currency query to verify if the given code is valid
    response = currency_response('USD', code, 2.5)

    # Return True if no error and the response has a destination value
    return not has_error(response) and get_dst(response) != ""


def exchange(old, new, amt):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency
    old to the currency new. The value returned represents the
    amount in currency new.

    The value returned has type float.

    Parameter old: the currency on hand (the SRC)
    Precondition: old is a string for a valid currency code

    Parameter new: the currency to convert to (the DST)
    Precondition: new is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition: amt is a float
    """
    # Get the response for the exchange using the given parameters
    response = currency_response(old, new, amt)

    # Extract the destination value (amount in the new currency)
    dst = get_dst(response)

    # Get the numeric amount from the destination string (before the space)
    amount = before_space(dst)

    # Return the amount as a float
    return float(amount)
