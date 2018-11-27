# Colin Goodman
# this file determines if there is a friendship between a given user and another
# 2018

user_one = input("First user: ")
user_two = input("Second user: ")

name = user_one + "data"
file = open(name, 'r')
file.readline()
mentioned = file.readline().split()

result = 0

for user in mentioned:
    if user == user_two:
        result = 1
