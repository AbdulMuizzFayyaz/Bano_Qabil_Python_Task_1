#Abdul Muizz

#Question No. 9:
#Combine two strings using string concatenation, and then use string interpolation to include the length of the resulting string in a print statement.
 
#First we declare 2 variables with string value.
string1 = "Hello"
string2 = " World!"

#Now we declare another variable "combined_string" ,which will concatenate "string1" "string2".
combined_string = string1 + string2

#Now we print using print function and use interpolation to include lenght of the resulting string.
print(f"The combined string is :{combined_string}.It's lenght is :{len(combined_string)} characters")