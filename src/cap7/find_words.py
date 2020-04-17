import re


##the | pipe is an or operator
##create a regex to find Batman or Iron Man in a string
hero_regex = re.compile(r"Batman|Iron Man")

mo1 = hero_regex.search("Batman is very rich, but Iron Man is richier")

print(mo1.group())


mo2 = hero_regex.search("Iron Man is very rich, but Batman is richier")

print(mo2.group())