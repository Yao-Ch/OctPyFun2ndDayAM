
def sub(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        temp=a-b
        return temp
    else:
        # print("Wrong argument given")
        # return None
        raise Exception("Wrong argument given")
        

result=sub(12, 23) # Positional arguments
print(result)
print("The end")

result=sub(b=12, a=23) # Named arguments
print(result)
print("The end")
# result=add("abc", "GHT")
# print(result)
# print("The end")



