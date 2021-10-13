
def add(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        temp=a+b
        return temp
    else:
        # print("Wrong argument given")
        # return None
        raise Exception("Wrong argument given")
        

result=add(12, 23)
print(result)
print("The end")

# result=add("abc", "GHT")
# print(result)
# print("The end")



