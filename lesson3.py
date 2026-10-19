"""Python is a programming language with dynamic and strong typing
str -> string -> text
Strings are piaces of text encloased within single or duble quotation marks"""

# Simple quotes
print('Matheus Goes')
print(1, 'Matheus "Goes"')

#Duble quotes
print("Matheus Goes")
print(2, "Matheus 'Goes'")

#Escape
print("Matheus \"Goes\"") # O \ it skips to the next caracter, in this case,  it skips to the " and doe'sn't cloe the string, so it prints the " in the output

# r
print(r"Matheus \"Goes\"") # The "r" before the string cause the '\'  to be ignored, in other words, it doesn't skip to the next caracter 