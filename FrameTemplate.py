# The following script takes input from the user and formats it
#
# SKILLS:
#       1.decision making with if-elif-else
#       2.handling user input
#
# Author:
#
#
# 
sentence = input("")
print("-------------------------------------")
print("Format your sentence -> use the keys:")
print("<c> Capitalize")
print("<u> Upper Case")
print("<l> Lower Case")
print("<r> replace x with y")
print("-------------------------------------")

# *********** PUT YOUR CODE HERE *********************************
# Ask the user to select the format type (c, u, or l) and store
# the input in a variable named format
# USER INPUT OF FORMAT TYPE --------------------------------------
# ****************************************************************
format = 'c' # replace with actual user input

# The following line of code is using a string function
# What kind of reformatting does the lower function do?
format = string.lower(format) # reformats the user input

# *********** PUT YOUR CODE HERE *********************************
# Check format type selected by the user (letter)
# Make sure that upper case and lower case letters are accepted
# if 'c' then use an appropriate string function
#               to capitalize
# if 'u' then use an appropriate string function to put
#               to upper case
# if 'l' then use an appropriate string function to put
#               to lower case
# Finally, if the user accidentally typed something else
# then inform the user about the mistake and put the sentence
# to some default (e.g. do no user formatting)
# ****************************************************************
