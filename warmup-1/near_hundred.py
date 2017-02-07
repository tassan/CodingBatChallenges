# near_hundred
# Given an int n, return True if it is within 10 of 100 or 200.
# Note: abs(num) computes the absolute value of a number.


def near_hundred(n):
    if n <= 100:
        if n >= abs(10 - 100):
            return True
        return False
    if n >= 100:
        if n >= abs(10 - 200):
            return True
        return False


print(near_hundred(89))
