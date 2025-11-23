print("i dont know i did cmmit form the past 2 days,,i feel bad..but hopefully i am back on track")

u_i= input(" enter a number matching your emotion: 1= happy, 2= sad, 3= anxious and 4 = nuetral: ")

i = int(u_i)

def emotions(choice):
    if i == 1:
        print(" Being happy shuld be contagious. Spread your happiness aroug and rember life is not always sad. there is always happiness at the end of the tunnel")
    elif i == 2:
        print(" Dont be sad because verily with hardship comes ease")
    elif i == 3:
        print(" anxiety is just unwanted fear of unlikely thing. dont worry..just breate")
    else:
        print(" its sometimes okay to be just okay..not happy or sad just okay")


emotions(i)