# 2) (20 points) The question is about creating a two-dimensional matrix with 3 rows and 2 columns.
matrix = []

# function for user input and appending values to the matrix
for i in range(3):  # A for loop for row entries
    a = []
    for j in range(2):  # A for loop for column entries
        a.append(int(input("Enter a value: ")))
    matrix.append(a)

print('The list is')
print(matrix)
