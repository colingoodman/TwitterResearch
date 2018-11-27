# Colin Goodman
# this file determines social homogeneity - built to return a single number
# 2018

import tweepy

user_one = input("First user: ")
user_two = input("Second user: ")

# jaccard index: |Mv ^ Mv|/|Mv U Mv|

name_one = user_one + "data"
file_one = open(name_one, 'r')
file_one.readline()
list_one = file_one.readline().split()
size_one = list_one.sizeof()

name_two = user_two + "data"
file_two = open(name_two, 'r')
file_two.readline()
list_two = file_two.readline().split()
size_two = list_one.sizeof()

overlap = 0

for user_o in list_one:
    for user_t in list_two:
        if user_o == user_t:
            overlap += 1

final = (overlap / ((size_one - overlap) + (size_two - overlap)))  # this is the Jaccard similarity index number

