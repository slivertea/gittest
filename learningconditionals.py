#!/usr/bin/python3.6

my_integer = 443
if my_integer > 0:
    print("Hey, that looks like its a positive number!")

my_integer = -443
if my_integer > 0:
    print("Hey, that looks like its a positive number!")

#my_integer = "Perl is king!"
#if my_integer > 0:#
    #print("Hey, that looks like its a positive number!")

mystring = "Perl is king!"
mysuccess = "Yup, perl is king"
myfail = "Python is king, but it Perl is still better"
if "Perl" in mystring:
    print(mysuccess)

elif "?" in mystring:
    print(" ... and it has a bang")

if "king" in mystring:
    print(".....and perl is definitely KING!")
