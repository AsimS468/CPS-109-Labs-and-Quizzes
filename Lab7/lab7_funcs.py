'''
No description needed at this point. Fill in the functions below
according to the description provided. 

These functions must be solved RECURSIVELY. If your solution does
not use recursion, you risk receiving a zero on the lab submission.

'''


# --------------------------------------------------------------
# 1) Count occurrences
# --------------------------------------------------------------

def count(items, target):

    '''
    This function emulates the list method 'count'. Assume items
    is a list, and target is some object. Return the number of
    times that target appears in items.
    
    YOU MUST USE RECURSION!    
    
    '''
    n = 0
    if len(items) == 0:
        return 0
    
    if items[0] == target:
        n = 1
    else:
        n = 0

    return n + count(items[1:], target)
    



    
# --------------------------------------------------------------
# 2) Sum of integers
# --------------------------------------------------------------

def integer_sum(items):

    '''
    This function calculates and returns the sum of the integer
    values in the list 'items'.
    
    Be careful - items may contain things other than integers!
    
    For example, if the input is [ 1, 3, 'hello', 5.66 ], you 
    should return 4 (1 + 3).
    
    Hint: You can check if an object is an integer by performing 
    the following comparison: type(obj) == int
    
    YOU MUST USE RECURSION!    
    
    '''
    
    n = 0
    if len(items) == 0:
        return 0
    
    if type(items[0]) == int:
        return items[0] + integer_sum(items[1:])
    else:
        return integer_sum(items[1:])


    
  
# --------------------------------------------------------------
# 3) Exponentiation
# --------------------------------------------------------------

def pow_rec(base, exponent):

    '''
    Assume that base and exponent are integers >= 0.
    
    Calculate and return base to the power of exponent using 
    repeated multiplications.
    
    YOU MUST USE RECURSION!

    '''

    n = base
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    
    if exponent > 1:
        return n * pow_rec(base, exponent-1)



    
# --------------------------------------------------------------
# 4) Palindrome checker
# --------------------------------------------------------------

def is_palindrome(text):

    '''
    A recursion classic.
    
    Assume that 'text' is a string. Return True if text is a 
    palindrome, and False otherwise. 
    
    A string is a palindrome if it reads the same forwards and
    backwards. For example, 'racecar' is a palindrome.
    
    YOU MUST USE RECURSION!

    '''

    if len(text) <= 1:
        return True

    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    else: return False


# --------------------------------------------------------------
# 5) Nested list reverser
# --------------------------------------------------------------

def nested_reverse(items):

    '''
    Assume that items is a list, that may contain nested lists
    as elements. This function will perform a reverse operation,
    but with a twist - nested sublists must be reveresed as well.
    
    For example, if the input is [ 1, 2, [5, 4, 3, [9, 0], 3 ] ]
    then you should return [ [ 3, [0, 9], 3, 4, 5], 2, 1 ]

    Hint: You can check if an object is a list by performing the 
    following comparison: type(obj) == list
    
    YOU MUST USE RECURSION!

    '''

    if len(items) == 0:
        return []
    
    rItems = []
    for item in reversed(items):
        if type(item) == list:
            rItems.append(nested_reverse(item))
        else:
            rItems.append(item)
    
    return rItems


