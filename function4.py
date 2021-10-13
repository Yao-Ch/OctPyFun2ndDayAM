
def add(*args):
    total=0
    for e in args:
        total+=e
    return total
        


result=add(4,5,10,23) 
print(result)

result=add() 
print(result)

result=add(78,89,12,34,67,78) 
print(result)

somme=add # an "alias" of the function add is created

result=somme(78,89,12,34,67,78) 
print(result)