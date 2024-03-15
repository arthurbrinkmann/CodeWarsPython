# Lines 2-3 Insturctions
#Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for
#false.
def bool_to_word(boolean):  # Define a function named "bool_to_word" which takes a boolean parameter
    if boolean == True:  # Check if the boolean parameter is True
        return "Yes"  # Return "Yes" if the boolean parameter is True
    elif boolean == False:  # Check if the boolean parameter is False
        return "No"  # Return "No" if the boolean parameter is False
    return boolean  # Return the boolean parameter if it's not True or False
