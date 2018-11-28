# Colin Goodman
# this file determines a given users mention rate
# !! due to the nature of this property, it may take some time to execute
# 2018

user = input("User: ")
fileName = user + "data"

user_file = open(fileName, 'r')

user_file.readline()  # skip past the lines in the file we do not need
user_file.readline()
user_file.readline()

targets = user_file.readline().split()

counter = 0

# for every person that has mentioned this user, find how many times they mentioned this user
for target in targets:
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
