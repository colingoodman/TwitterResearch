# Colin Goodman
# this file determines a given users mention rate
# !! due to the nature of this property, it may take some time to execute
# 2018

user = input("User: ")
fileName = user + "data"

user_file = open(fileName, 'r')

user_file.readline()
user_file.readline()
user_file.readline()

targets = user_file.readline().split()

counter = 0

for target in targets:
    counter = 0
    new_file = open(target, 'r')

    loop = True
    while loop:
        line = new_file.readline()
        if line.sizeof() == 0:
            loop = False
            continue
        if line.find(user):
            counter += 1

average = 200  # this is a constant defined in the Guille paper
result = counter / average
