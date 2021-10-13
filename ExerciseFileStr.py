
"""
New exercise:
    
Given a file with this format (you can use "data2.txt" for instance):

    x1:0.34;x2:0.56
    x1:0.24;x2:0.45
    x1:0.27;x2:0.55
    ...

extract out of it the numerical values associated with x1 and x2.
The values associated with x1 will be stored in a list with the name X1.
The values associated with x2 will be stored in a list with the name X2.

Create a list Y1 that will contain the cosine of each value stored in X1 
(use the math.cos() function)

Create a list Y2 that will contain the sine of each value stored in X2 
(use the math.sin() function)

Once the 4 lists will be created I will show you how to plot the 
corresponding points (X1,Y1, X2,Y2).
"""

import math

afile=open("data2.txt")

X1=[]
X2=[]

for line in afile:
    
    part1,part2=line.split(";") # unpacking

    X1.append(float(part1.split(":")[1]))
    X2.append(float(part2.split(":")[1]))
    
    # result=line.split(";")

    # X1.append(float(result[0].split(":")[1]))
    # X2.append(float(result[1].split(":")[1]))

afile.close()

print(X1)
print(X2)

Y1=[]
for e in X1:
    Y1.append(math.cos(e))

# or

# Y1=[math.cos(e) for e in X1]

Y2=[]
for e in X2:
    Y2.append(math.sin(e))

print(Y1)
print(Y2)

import matplotlib.pyplot as plt

plt.plot(X1, Y1, label="Cosine")
plt.plot(X2, Y2, label="Sine")
plt.legend()
plt.show()









# X1=[]
# X2=[]

# dataFile=open("data2.txt")

# for line in dataFile: # A loop to read the file line by line
#     part1, part2=line.split(";")
#     x1Value=part1[part1.index(":")+1:] # or x1Value=part1.split(":")[1] 
#     x2Value=part2[part2.index(":")+1:]  
#     X1.append(float(x1Value)) 
#     X2.append(float(x2Value)) 
    
# dataFile.close()

# import math

# Y1=[]    
# for element in X1:
#     Y1.append(math.cos(element))

# Y2=[]    
# for element in X2:
#     Y2.append(math.sin(element))
    
# print(X1, Y1)