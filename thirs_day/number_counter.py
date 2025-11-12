user_input=input("enter the number till which the counting should go on:")
number=int(user_input)

def allnumbers(number):
    for i in range(1, number+1):
        print(i)

def evennumbers(number):
    for i in range(1, number+1):
        if i%2==0:
            print(i)

def oddnumbers(number):
    for i in range(1, number+1):
        if i%2!=0:
            print(i)

option_input=input("select a for all numbers, b for even only and c for oddonly: ")

if option_input=='a':
    allnumbers(number)
elif option_input=='b':
    evennumbers(number)
elif option_input=='c':
    oddnumbers(number)



