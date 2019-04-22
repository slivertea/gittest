#!/usr/bin/python3.6
my_list = [1, 2, 3]
print(my_list)
print(my_list[0])
#
my_list.append("four")
print(my_list)
#
del my_list[2]
print(my_list)
#
nested_list = []
nested_list.append(123)
nested_list.append(22)
nested_list.append('ntp')
nested_list.append('ssh')
print(nested_list)
#
my_list.append(nested_list)
print(my_list)
#
print(my_list[3])
#
print(my_list[3][2])
#
#print(my_list[0][1])
print(my_list[2][1])
###################################3
sliced = my_list[1:3]
print(sliced)
############################
slice_me = "ip_address"
sliced = slice_me[:2]
print(sliced)

###################################
my_dictionary = {}
#print(type(my_dictionary))
#
my_dictionary["gigE0"] = "Link to ISP"
my_dictionary["gigE1"] = "DMZ"
my_dictionary["gigE2"] = "Inside"
my_dictionary["gigE3"] = "Guest"
print(my_dictionary)
print(my_dictionary['gigE3'])

# Dictionaries
my_list = [3, 2, 1]
my_other_dictionary = {}
my_other_dictionary["ohai-key"] = "ohai-value"
my_dictionary["NL"] = my_list
my_dictionary["ND"] = my_other_dictionary
print(my_dictionary)
# Nested Dictionaries
print(my_dictionary["ND"]["ohai-key"]) # - match the keyname to the key name of the dictionary
