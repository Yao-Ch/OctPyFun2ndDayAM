"""
Exercise 6:

    if isPrime(17):
        print("This number is a prime number")
    
    isPrime will return a boolean result (True or False)
    True if the argument it receives is a prime number False if not
    To test if the argument N is a prime number you can, in a loop, test
    if it can be divided by 2, 3, 4, ... N-1
    As soon as you find a divisor (you can use % for that purpose), you 
    can leave the loop and the function: N is not a prime number, you can 
    return FALSE
    If after having tested all numbers between 2 and N-1 none of them is
    a divisor of N, N is a prime number, you can return True
    
    def isPrime(nb):
        .....
"""

def isPrime(nb):
    if not isinstance(nb, int): # Error: an int should be provided!!!
        raise Exception("Wrong type of argument received")
        
    if nb < 0: # Error: a positive int should be provided!!!
        # print("Negative argument received")
        # return None
        raise Exception("Negative argument received")
  
    if nb in [0,1]: # <=>   if nb==0 or nb==1:
        return False # 0 and 1 are not a prime numbers
    
    ix=2
    while ix < nb:   
        # Note: another simpler but less efficient option is:
        # while ix < nb: 
            
        if nb % ix == 0:        # If ix is a divisor of nb:
            return False        #       nb is not a prime number
        
        ix += 1
        
    # for ix in range(2,nb):   
    #     if nb % ix == 0:        # If ix is a divisor of nb :
    #         return False        # 		nb is not a prime number
      
    return True # If we have reach this point, it means nb is a prime number


numbers=[2,6,78,4,6,89,23]

for nb in numbers:
    if isPrime(nb):
        print(f"{nb} is a prime number")
    else:
        print(f"{nb} is not a prime number")