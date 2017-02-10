# front_times
# Given a string and a non-negative int n,
# we'll say that the front of the string is the first 3 chars,
# or whatever is there if the string is less than length 3.
# Return n copies of the front;


def front_times(str, n):
    if n > 0:
        if len(str) < 3:
            return str * n
        return str[:3] * n
    return ''

print(front_times('', 3))
