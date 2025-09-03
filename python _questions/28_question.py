# Question: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1. Example Suppose the following inputs are given to the program: 3,5 Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# Hints: Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.
# def generate_2d_array(x, y):
#     array = []
#     for i in range(x):
#         row = []
#         for j in range(y):
#             row.append(i * j)   
#         array.append(row)
#     return array
# print(generate_2d_array(3, 5))


def gen_2d_array(x, y):
    return [[i * j for j in range(y)] for i in range(x)]
print(gen_2d_array(3, 5))


# Outer Structure
# - for i in range(x) — This loop runs x times. Each i represents a row index.
# - For each i, it creates a list: [i * j for j in range(y)]
# So the outer list will contain x inner lists.

# Inner List
# - for j in range(y) — This loop runs y times for each i. Each j represents a column index.
# - i * j — This is the value being calculated for each cell.
# So each inner list contains y elements, where each element is the product of the current i and j.

# Let’s say x = 3 and y = 4. Then the code becomes:
# [[i * j for j in range(4)] for i in range(3)]


# Let’s compute it:
# - When i = 0: [0*0, 0*1, 0*2, 0*3] → [0, 0, 0, 0]
# - When i = 1: [1*0, 1*1, 1*2, 1*3] → [0, 1, 2, 3]
# - When i = 2: [2*0, 2*1, 2*2, 2*3] → [0, 2, 4, 6]

