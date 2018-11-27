# Colin Goodman
# this file combs thru a given user file and finds where other users have been mentioned
# 2018

import tweepy

#auth = tweepy.OAuthHandler

user = input("User: ")
file = open(user, 'r')

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
                x += 1
                while content[x] != ' ':
                    target += content[x]
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