# Colin Goodman
# this file combs through a given user file and finds where other users have been mentioned
# 2018

user = input("User: ")

try:
    file = open(user, 'r')
except FileNotFoundError:
    print("Unknown user. Perhaps their file has not been made yet?")
    exit()

loop = True
users_mentioned = []  # list of users mentioned by this user

while loop:
    file.readline()  # time
    link = file.readline().rstrip()  # user
    content = file.readline()  # tweet
    link = link.replace('U\thttp://twitter.com/', '')

    # if this tweet mentions another user:
    if content.find('@'):
        target = ''
        x = 0  # used to iterate thru tweet
        while x < content.sizeof():  # getting the mentioned user's handle
            if content[x] == '@':
                while content[x] != ' ':
                    target += content[x]
            x += 1
        users_mentioned.add(target)

file.close()

# create a new user file for their data
# this first part is for users mentioned by this user

fileName = user + "data"
result = open(fileName, 'w')
result.write("Mentioned users: \n")

for user in users_mentioned:
    result.write(user + " ")

result.write("Mentioned by: \n")
result.close()

# now to update other files

for user in users_mentioned:
    fileName = user + "data"
    other = open(fileName, 'a')
    other.write(user + " ")