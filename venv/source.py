# Colin Goodman - 2018
# Information propagation in social media networks

import tweepy

# tweepy stuff
api = tweepy.API(auth)

# preparing files
file = open('tweets2009-06.txt.001', 'r', )  # encoding="utf8")
keyWords = open('testKey.txt', 'r', )  # encoding="utf8")
writeTo = open('results.txt', 'w', )  # encoding="utf8")

# pull key words and organize them into array
print('reading in key\n')
loop = True
key = []  # array of key words (KWs)
int = 0
while loop:
    string = keyWords.readline().rstrip().lower()
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

    # The following if statements catch if there is a formatting issue.
    if time.find('T\t') == -1:
        print('Tweet not formatted properly. (T)')
        break;
    link = file.readline().rstrip()
    if link.find('U\t') == -1:
        print('Tweet not formatted properly. (U)')
        break;
    string = file.readline().rstrip()
    if string.find('W\t') == -1:
        print('Tweet not formatted properly. (W)')
        break;

    link = link.replace('U\thttp://twitter.com/', '')
    time = time.replace('T\t', '')
    string = string.replace('W\t', '')
    workString = string.lower()

    if len(string) == 0:  # if end of text file, stop
        loop = False
    else:
        index = 0
        while loopThru:  # loop thru array of KWs
            if len(key) <= index:
                break
            if workString.find(key[index]) != -1:  # if kw in tweet, write tweet and quit
                try: # if the user still exists, add them to file
                    user = str(api.get_user(link).id)
                    writeTo.write(time + "\n" + link + '\n' + string + "\n\n")
                except: # if user no longer exists, ignore the tweet
                    user = 'null'
                break
            index += 1

    file.readline()  # this consumes the empty lines separating each tweet

print('done!')
