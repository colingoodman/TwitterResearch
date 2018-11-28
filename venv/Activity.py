# Colin Goodman
# this file determines a given user's activity index
# 2018

user = input("User: ")
file = open(user, "r")

loop = True
total = 0

while loop:
    file.readline()
    file.readline()
    message = file.readline()

    if message.sizeof() > 0:  # this logic seems silly but its necessary to write like this
        loop = True
        total += 1
    else:
        loop = False

result = 1
if total < (30.4 * 24):  # this hardcoded number is provided in Guille's paper
    result = total / (30.4 * 24)
