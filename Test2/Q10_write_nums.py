# Part C -  Your function (write_nums(n) ) raises a "LessThanZeroError" error if the entered number (n) is negative(<0).
# LessThanZeroError is a custom error type.
class LessThanZeroError(Exception):
  def __init__(self, value):
    self.value = value

# Part A - Write a recursive function (called write_nums) that accepts an integer n as a parameter and prints a sequence
# of numbers from 1 to n, separated by a comma. For example, if n = 5, output 1, 2, 3, 4, 5.
def write_nums(n):
  # check if n is greater than 0
  if n > 0:
    # recursively call the write_nums function
    write_nums(n - 1)
    # print n
    print(n, end = ', ')
  if n < 0:
    raise LessThanZeroError('Input must be greater than 0')


while True:
    try:
        user_input = input("Enter a number (hit return/enter to quit): ")
        # Part B - Your program asks the user to enter a number to print the sequence of n number repeatability until
        # you hit the enter key to exit.
        if not user_input:
          print("You hit 'return or enter' to quit")
          exit('done')
        n = int(user_input)
        write_nums(n)
        print('')
    # Part D - Your test program (outside of the write_nums(n) function ), uses the while loop with the try.. expect
    # blocks to catch the NAN (not a number) entries and exit the while loop when the user hits the “enter” key
    except ValueError:
      print(f"you entered '{user_input}', it is not a number")
    except LessThanZeroError as f1:
        print(f'{f1}')