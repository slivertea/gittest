#!/usr/bin/python3.6
correctinput = "Vigus"
name = input("Hey person, what is your name? ")
valid = 0
while valid != 1:
    if correctinput not in name:
        name = input("Hey " + name +", that's not your name, Try again")
    else:
        valid=1
        print ("Good mroning" + name)
