# 1) (15 points) Write a function and accept two arguments: a list and a number n.

# declaring initial values, no user input needed
number = 15
lst_1 = [11, 26, 7, 34, 25, 15, 43, 81, 19, 37]


def display_greater(lst_1, number):
    # declare "ans" list
    ans = []
    # iterate "lst" and find numbers greater than given number
    for n in lst_1:
        if n > number:
            # if found append it to "ans" list
            ans.append(n)
    # print number
    print("Number greater > :", number)
    # print original list
    print("Original list of numbers:")
    print(lst_1)
    # print "ans" lis
    print("List of numbers that are larger than", number, ":")
    print(ans)


display_greater(lst_1, number)
