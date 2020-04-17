import re


#Strings with r are pure strings
#str_regex = r'.....'

##we can create a group by using parenthesis ()

#Creating a Regex object
##\d represents an integer
phone_num_regex = re.compile(r'(\d{3})-(\d{3})-(\d{3})')

##search() searches for the regex within the string
##if nothing is found it returns None
##if the pattern is found, it returns a Match object
mo = phone_num_regex.search("My phone number is 444-555-666")


if mo != None:
    ##group() return the pattern found
    ##group() has an index parameter, wich gets the group from the tuple of groups
    print("Phone number found: {}".format(mo.group()))
    print(mo.groups()) ##groups() returns a tuple with all groups
else:
    print("No pattern was found")