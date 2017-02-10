# string_splosion
# Given a non-empty string like "Code" return a string like "CCoCodCode".


def string_splosion(str):
    x = 0
    while x < len(str):
        st = str[0:++x]
    return st


print(string_splosion('Code'))
