
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

X1=[]
X2=[]
f1=open("temp/data2.txt")

for line in f1:

    #line=line.strip()  # line is now a string without the initial and final "whitespaces"
    split1=line.split(";") # split1 is a list composed of 2 strings

    split2=split1[0].split(":")# split2 is a list composed of 2 strings
    split3=split1[1].split(":")# split3 is a list composed of 2 strings
    
    x1=float(split2[1]) # We convert into float the 2nd element of split2
    x2=float(split3[1]) # We convert into float the 2nd element of split3
    
    X1.append(x1)
    X2.append(x2)
    
f1.close()

print(X1)
print(X2)

Y1=[]
for e in X1:
    Y1.append(math.cos(e))
    
Y2=[]
for e in X2:
    Y2.append(math.sin(e))


