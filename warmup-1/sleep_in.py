# sleep_in

# The parameter weekday is True if it is a weekday,
# and the parameter vacation is True if we are on vacation.
# We sleep in if it is not a weekday or we're on vacation.
# Return True if we sleep in.


weekday = True
vacation = True


def sleep_in(weekday, vacation):
    sleep = False

    if weekday == True:
        sleep = False
    elif weekday == False:
        sleep = True

    if vacation == True:
        sleep = True

    return sleep

print(sleep_in(True, True))

