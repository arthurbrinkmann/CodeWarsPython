#Instructions from line 2-3
# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You are given one parameter, the original string. 
# You dont have to worry about strings with less than two characters

# Define a function named remove_chars with one parameter: s
def remove_chars(s):
    # Return a substring of s, excluding the first and last characters
    return s[1: -1]