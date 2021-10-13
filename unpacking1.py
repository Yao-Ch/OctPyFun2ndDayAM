
data=[34,56,67]

first, second, third = data

print(data[0], first)

data=[34, 56, 77, 199]

first, second, *other, prev, last = data

print(other, prev, last)