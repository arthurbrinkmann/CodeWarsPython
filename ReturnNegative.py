# Lines 2-7 Insturctions
#In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?
#
#Examples
#make_negative(1);  # return -1
#make_negative(-5); # return -5
#make_negative(0);  # return 0

def make_negative(number):  # Define a function called make_negative that takes one parameter, number.
    """
    Function to return a negative number.  # Documentation string explaining the purpose of the function.
    
    Parameters:  # Explanation of the parameters the function expects.
        number (int or float): The number to convert to negative if it's positive.
    
    Returns:  # Explanation of what the function returns.
        int or float: The negative number.
    """
    if number > 0:  # Check if the number is greater than 0.
        return -number  # If it is, return the negative of the number.
    else:  # If the number is not greater than 0 (i.e., it's negative or zero),
        return number  # return the number unchanged.
    pass  # This line is not necessary and does nothing in this context.
