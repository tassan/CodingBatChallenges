# front_back
# Given a string,
# return a new string where the first and last chars have been exchanged

# i tried :(
# def front_back(str):
#    temp = str[1:-1]
#    return str[-1:] + temp + str[:1]


def front_back(str):
    if len(str) <= 1:
        return str

    mid = str[1:len(str) - 1]
    return str[len(str) - 1] + mid + str[0]

print(front_back('caco'))
