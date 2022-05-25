from functools import reduce
sequence = [1, 2, 3]
def sum_of_squares(sequence):
    a =[]
    a = (i*i for i in (sequence))
    return a

print(reduce(sequence, sum_of_squares))
