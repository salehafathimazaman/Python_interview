try:

    user_input=input("enter A:")
    user_input_2=input("enter B:")
    A=int(user_input)
    B=int(user_input_2)

except:
    print("invalid inpu, please input only numbers")
    exit()
def multiplereturns(A, B):
    return A+B,A-B,A*B

sumvalue, diff_value, product_value= multiplereturns(A, B)


print(f"sum of A and B = {sumvalue} differenc eof A and b is {diff_value} product of A and B is {product_value}")

