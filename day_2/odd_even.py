def evenorodd(number):
    if number % 2==0:
        print("given number is even")
    else:
        print("number is off")

user_input=input('give a numer to check if it is even or odd:')
number =int(user_input)

evenorodd(number)
