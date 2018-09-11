# Colin Goodman - 2018
# Information propagation in social media networks

import tweepy

# tweepy stuff
auth = tweepy.OAuthHandler('0oG3gXlR17hHDfrmK5ICkR6nV', '2oOe6SxCaBgNz7PTtwriSTVj5Vx6lkZdoAkb4nM0BpEtZl0BOz')
auth.set_access_token('247468435-MM16zZOkuNPIL7qE7aNRfWDs3YRx3VSmV0xWKSed', '5Bx6AbxFUdv6zh0xMU9BAwKhBuhOq0fR8inNme6MK7bVx')
api = tweepy.API(auth)

# preparing files
file = open('tweets2009-06-num2.txt', 'r', encoding="utf8")
keyWords = open('key.txt', 'r', encoding="utf8")
writeTo = open('result2.txt', 'w', encoding="utf8")

# pull key words and organize them into array
print('reading in key\n')
loop = True
key = []  # array of key words (KWs)
int = 0
while loop:
    string = keyWords.readline().rstrip()
    if len(string) == 0:
        loop = False
    else:
        key.append(string)
print('key read successfully. reading and sorting tweets.\n')

# checking for keywords in all tweets
loop = True
loopThru = True
while loop:
    time = file.readline().rstrip()
    link = file.readline().rstrip()
    string = file.readline().rstrip()
    workString = string.lower()
    link = link.replace('U\thttp://twitter.com/', '')
    time = time.replace('T\t', '')
    string = string.replace('W\t', '')

    if len(string) == 0:  # if end of text file, stop
        loop = False
    else:
        index = 0
        while loopThru:  # loop thru array of KWs
            if len(key) <= index:
                break
            if workString.find(key[index]) != -1:  # if kw in tweet, write tweet and quit
                user = str(api.get_user(link).id)
                writeTo.write(time + "\n" + link + "\n" + user + '\n' + string + "\n\n")
                break
            index += 1

    file.readline()  # this consumes the empty lines separating each tweet

print('done!')