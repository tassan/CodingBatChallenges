# string_times
# Given a string and a non-negative int n,
# return a larger string that is n copies of the original


def string_times(str, n):
    if n > 0:
        return str * n
    return ''


print(string_times('Hi', 4))
