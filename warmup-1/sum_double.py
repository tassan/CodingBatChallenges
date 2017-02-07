# sum_double
# Given two int values, return their sum.
# Unless the two values are the same, then return double their sum.


def sum_double(a, b):
    if not a == b:
        return a + b
    return 2*(a+b)

print(sum_double(1, 1))
