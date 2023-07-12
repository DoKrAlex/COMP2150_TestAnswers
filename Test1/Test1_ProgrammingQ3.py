# 3) (15 points) Write a function (string_total) to compute the sum of digits in a string.

# function for finding the sum of all digits in the user inputted sequence
def string_total(num_string):
    total = 0
    for ch in num_string:  # A for loop for adding every number in the string
        total += int(ch)
    return total


# function for user input and printing the sum
def main():
    num_string = input("Enter a sequence of digits with nothing separating them: ")
    print("The total of the digits in the string you entered is", string_total(num_string))


main()