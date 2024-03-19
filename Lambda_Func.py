# A lambda function is a special type of function without a name, also referred to as an anonymous function.
# Lambda creates a single line of output statement 
# Lambda can be used as a subtitute for def function. 
#Description:

#- Lambda - is a keyword in Python for defining the anonymous function.
#- argument(s) - any value passed to the lambda function
#- expression - expression is executed and returned

# Example 1
#snack = lambda : print("eggs")
#snack()

# subtituting def for lambda
#def num_square(num):
    #return num ** 2
#print("square of num is: ", num_square(8))

# Example 2
#num_square = lambda num:  num ** 2
#print("square of num is: ",  num_square(8))

# example 3
# a python function that determines Palindrome of a given string

def isPalindrome(string):
    """This function checks if a string is a palindrome."""
    if (string == string[::-1]):
        return "A Palindrome."
    else:
        return "Not a Palindrome."
    
    #Enter user input string
user_string = input("Enter string: ")
    
    # Call the function with the input
print(isPalindrome(user_string))
quit()

isPalindrome = lambda string: "Palindrome" if string == string[::-1] else "Not a palindrome."
string = input("Enter string:")

print(isPalindrome(string))

