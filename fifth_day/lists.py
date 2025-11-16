g=[]

for i in range(5):

    number=int(input(f"Enter number {i+1}: "))
    g.append(number)

def analyzelist(number_list):
    largest=max(number_list)
    smallest=min(number_list)
    total= sum(number_list)
    return largest, smallest, total

largest, smallest, total= analyzelist(g)

print("largest:", largest)
print("smallest:", smallest)
print("total:", total)






