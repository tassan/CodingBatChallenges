# not_string
# Given a string,
# return a new string where "not " has been added to the front.
# However, if the string already begins with "not",
# return the string unchanged.


def not_string(str):
    if len(str) >= 3 and str[:3] == 'not' in str:
        return str
    return 'not ' + str

print(not_string('is not'))
