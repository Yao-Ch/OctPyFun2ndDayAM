def add(*args):
    total=0
    for e in args:
        total+=e
    return total

def sub(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        temp=a-b
        return temp
    else:
        # print("Wrong argument given")
        # return None
        raise Exception("Wrong argument given")
