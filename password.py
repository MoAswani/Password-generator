# python unbreakable password generator
import random

def generate():
    password_length = int(input("please enter the length of your password: "))
    password = random.sample(x, password_length)
    print("Hello", name, 'your strong password is', ''.join(password))

caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = caps.lower()
numbers = '1234567890'
symbols = '!@#$%^&*/\_+?'
x = caps + lower + numbers + symbols
name = input("Enter your username: ")


#Calling the function to generate password
generate()

 #User decides to continue with password or generate another one
user_choise = int(input("press 1 to continue with generated password or press 2 to generate another password: "))

if user_choise == 1:
    print("password succesfully created")

elif user_choise ==2:
    generate()

