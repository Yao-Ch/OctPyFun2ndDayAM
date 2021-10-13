
def sub(a=0, b=0):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        temp=a-b
        return temp
    else:
        # print("Wrong argument given")
        # return None
        raise Exception("Wrong argument given")
        

result=sub() # Positional arguments
print(result)
nb=12
print("Nb is", nb, "nb**2 is", nb**2, sep=" ")




