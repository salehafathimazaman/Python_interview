g=[]
for  i in range(1,6):
    u_ip=input(f"enter {i} number: ")
    f=g.append(int(u_ip))
print(g)

def analyzelist(numberlist):
    largest=max(numberlist)
    smallest=min(numberlist)
    total=sum(numberlist)
    length=len(numberlist)
    avg= total/ length

    count=0
    for i  in numberlist:
        if i > avg:
            count+=1

    return largest, smallest, total, length, avg, count
  

largest, smallest, total, length, avg, count= analyzelist(g)

print("smallest:", smallest)
print("largest:", largest)
print("total:", total)
print("average: ", avg)
print("numbers greater than avg:", count)


    

