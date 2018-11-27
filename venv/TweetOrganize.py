# Colin Goodman - 2018
# Information propagation in social media networks
# This file creates a text file for every user in the network
# This file will also probably take a very long time to run completely if there are a lot of users

import tweepy

# tweepy stuff
auth = tweepy.OAuthHandler('0oG3gXlR17hHDfrmK5ICkR6nV', '2oOe6SxCaBgNz7PTtwriSTVj5Vx6lkZdoAkb4nM0BpEtZl0BOz')
auth.set_access_token('247468435-MM16zZOkuNPIL7qE7aNRfWDs3YRx3VSmV0xWKSed', '5Bx6AbxFUdv6zh0xMU9BAwKhBuhOq0fR8inNme6MK7bVx')
api = tweepy.API(auth)

# make sure these files exist
file = open('tweets.txt', 'r', encoding="utf8")
writeTo = open('userIDs.txt', 'w', encoding="utf8")

users = []  # list of tuples of users (username, user ID)

loop = True

while loop:  # build list
    file.readline()  # time
    link = file.readline().rstrip()  # user
    file.readline()  # tweet
    link = link.replace('U\thttp://twitter.com/', '')

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
            userTuple = (link, api.get_User(link).id)
            users.Add(userTuple)

file.close()

for node in users:  # for each iteration of this loop, a new user file is created
    newFile = open(node[1] + '.txt', 'w', encoding="utf8")  # create text file for user
    file = open('tweets.txt', 'r', encoding="utf8")
    loop = True

    while loop:  # loop thru tweet file again
        time = file.readline()
        link = file.readline().rstrip()
        message = file.readline()

        if len(link) == 0:  # end while loop if at end of tweet file
            loop = False
            continue

        link = link.replace('U\thttp://twitter.com/', '')

        if link == node[0]:  # if given tweet was tweeted by user, add it to the new file
            newFile.write(time)
            newFile.write(message)
            newFile.write()