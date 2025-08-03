## multiline string uses ''' or """ both on the beginning and the end
# 
# 
# for x in "banana":
#   print(x)
#
#
#string length - len()
#check string - print({what you want to check} in file)
#if statement
#if NOT statement

#string slicing - from the start position print([:7])
#               - from the end position print([2:])

#Negative indexing 
# Example

# Get the characters:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):
# b = "Hello, World!"
# print(b[-5:-2])

#####upper & lower case
# upper case--->print(x.upper())
###
#lower case--->print(x.lower())
###
# to remove unnecessary white space before or after a text----> print(x.strip())
###
#replace a string--->print(x.replace("word you wanna replace", "word you want to replace it with"))
###
#split ---> print(x.split(",")) # returns ['Hello', ' World!']


#####string concatenation
#To concatenate, or combine, two strings you can use the + operator.
#To add a space between them, add a " " for example: c = a + " " + b


###string format
#we cannot combine strings and numbers like this:
# age = 36
# This will produce an error:
# txt = "My name is John, I am " + age
# print(txt)
######## we can combine strings and numbers by using f-strings or the format() method!
# for example:
# price = 59
# txt = f"The price is {price} dollars"
# print(txt)

#A placeholder can include a modifier to format the value.
#A modifier is included by adding a colon :
#followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
# price = 59
# txt = f"The actual price is {price:.2f} dollars"
# print(txt)

######ESCAPE characters
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
#instead of this which is not going to run: txt = "We are the so-called "Vikings" from the north."
# use this with escape cahracter to run it succesfully: txt = "We are the so-called \"Vikings\" from the north."
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value




# Methods	              Descriptions
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning