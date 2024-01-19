#Abdul Muizz

#Question No. 7:
#Write a program that takes user input for their age and prints a message addressing their age group (e.g., "Teenager," "Adult").

#First we declare a variable "age" and use input function.
age = int(input("Enter your age :"))

#Now for adding condition to print statement ,we use if else conditon.
if age<13 :
    print("Underage")
elif 13<= age <= 18 :
    print("Teenager")
elif 18<= age <= 65 :
    print("Adult")
else :
    print("Senior Citizen")