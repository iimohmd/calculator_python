
#import close
from fileinput import close
from os import system
import os
#import close

#name calculator  is Good name don't change (:
def name():
    print("====================================")
    print("MOHMMMED TAHER CALCULATOR !")
    print("====================================\n")
name()
#name calculator  is Good name don't change (:

#for inputs
num1 = int(input("Enter your number 1\n"))
mark = input("Enter mark\n")
num2 = int(input("Enter your number 2\n"))
#for inputs


#for chack exit or not !
def chack():
    massages = input("Are you want exit ? (y or n)\n")
    if(massages == "y"):
        close   
    elif(massages == "n"):
        #commend clear
        os.system('cls')
        # call funciton
        name()
        #repit
        num1 = int(input("Enter your number 1\n"))
        mark = input("Enter mark\n")
        num2 = int(input("Enter your number 2\n"))
    if mark == "x":
        print("result :")
        print(num1 * num2)
        chack()
    elif mark == "+":
        print("result :")
        print(num1 + num2)
        chack()
    elif mark == "-":
        print("result :")
        print(num1 - num2)
        chack()
    elif mark == "/":
        print("result :")
        print(num1 / num2)
        chack()
    else:
        print("==========================")
        print("Erorr[1]")
        print("==========================")
        chack()
        
#for chack exit or not !

#brine 
def result():
    #if statement
    if mark == "x":
        
        print("result :")
        print(num1 * num2)
        chack()
    elif mark == "+":
        print("result :")
        print(num1 + num2)
        chack()
    elif mark == "-":
        print("result :")
        print(num1 - num2)
        chack()
    elif mark == "/":
        print("result :")
        print(num1 / num2)
        chack()
    else:
        print("==========================")
        print("Erorr[0]")
        print("==========================")
        chack()

#write function becuse run 
result()
