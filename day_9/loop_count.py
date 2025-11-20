u_input=input("enter a sentence: ")

def count_aplha(h):
    count=0
    for i in h:
        if i== "a" or i== "A":
            count+=1
    return count

ano=count_aplha(u_input)
    
print(f"the number os time a appearded is {ano}")
