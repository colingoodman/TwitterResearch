# Colin Goodman - 2018
# Information propagation in social media networks
# This file creates a text file for every user in the network
# This file will also probably take a very long time to run completely if there are a lot of users

import os
import tweepy

# tweepy stuff

api = tweepy.API(auth)

targetTweets = 'testTweets.txt'  # file we are opening

file = open(targetTweets, 'r')  # , encoding="utf8")
writeTo = open('userIDs.txt', 'w')  # , encoding="utf8")

users = []  # list of tuples of users (username, user ID)
deadUser = 0;

loop = True

while loop:  # build list
    file.readline()  # time
    link = file.readline().rstrip()  # user
    file.readline()  # tweet
    link = link.replace('U\thttp://twitter.com/', '')
    file.readline()

    if len(link) == 0:  # if end of text file, stop
        loop = False
    else:
        if len(link) == 0:  # if there is nothing in the list
            continue
        check = False

        for node in users:  # check for duplicates in user list
            if node[0] == link:
                check = True

        if not check:  # if user not in list, add them to it
            try:
                idNum = str(api.get_user(link).id)
                userTuple = (link, idNum)
                users.append(userTuple)
                writeTo.write(idNum)
                writeTo.write(idNum)
            except:
                deadUser = deadUser + 1

file.close()
print('Number of invalid usernames: ')
print(deadUser)

here = os.path.dirname(os.path.realpath(__file__))
subdir = "users"
os.mkdir(os.path.join(here, subdir))

for node in users:  # for each iteration of this loop, a new user file is created
    fileName = str(node[1]).__add__('.txt')
    file = open(targetTweets, 'r')  # , encoding="utf8")
    loop = True

    filePath = os.path.join(here, subdir, fileName)

    newFile = open(filePath, 'w')

    while loop:  # loop thru tweet file again
        time = file.readline()
        link = file.readline().rstrip()
        link = link.replace('U\thttp://twitter.com/', '')
        message = file.readline()
        file.readline()

        if len(link) == 0:  # end while loop if at end of tweet file
            loop = False
            continue

        if link == node[0]:  # if given tweet was tweeted by user, add it to the new file
            newFile.write(time)
            newFile.write(message)
            newFile.write('')

file.close()
newFile.close()
writeTo.close()

print('..Success')
