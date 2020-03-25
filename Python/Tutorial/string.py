a = "Hello, World!"
print(len(a))

#================================================================
#The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World!    "
print(a.strip()) # returns "Hello, World!"

#================================================================
#The lower() method returns the string in lower case:

print(a.lower())
#================================================================
#The upper() method returns the string in upper case:

print(a.upper())
#================================================================
#The replace() method replaces a string with another string:

print(a.replace("H", "J"))
#================================================================
#The split() method splits the string into substrings if it finds instances of the separator:

print(a.split(",")) # returns ['Hello', ' World!']
#================================================================
#Check if the phrase "ain" is present in the following text:

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)
#================================================================
#Check if the phrase "ain" is NOT present in the following text:

txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x) 
#================================================================
#Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)
#================================================================
#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#================================================================
#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))