# Colin Goodman - 2018
# Information propagation in social media networks
# This file searches through the tweet text files and organizes all the users by ID

import tweepy

# tweepy stuff
auth = tweepy.OAuthHandler('0oG3gXlR17hHDfrmK5ICkR6nV', '2oOe6SxCaBgNz7PTtwriSTVj5Vx6lkZdoAkb4nM0BpEtZl0BOz')
auth.set_access_token('247468435-MM16zZOkuNPIL7qE7aNRfWDs3YRx3VSmV0xWKSed', '5Bx6AbxFUdv6zh0xMU9BAwKhBuhOq0fR8inNme6MK7bVx')
api = tweepy.API(auth)

file = open('tweets.txt', 'r', encoding="utf8")
writeTo = open('userIDs.txt', 'w', encoding="utf8")

users = []  # list of user IDS

loop = True

while loop:
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
        for id in users:
            if id == link:
                check = True
        if check == False:
            users.Add(link)