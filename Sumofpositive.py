# Lines 2-6 Insturctions
#You get an array of numbers, return the sum of all of the positives ones.
#
#Example [1,-4,7,12] => 1 + 7 + 12 = 20
#
#Note: if there is nothing to sum, the sum is default to 0.


def positive_sum(arr):
    # Initialize the sum to 0
    total_sum = 0  

    # Iterate through the numbers in the array
    for num in arr:
        # Check if the number is positive
        if num > 0:  
            # Add the positive number to the sum
            total_sum += num  

    return total_sum