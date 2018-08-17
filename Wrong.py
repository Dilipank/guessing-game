test="Hello there!"

c=0

# Wrong code (without any built-ins)

# while test[c]!=test[-1]:    

#     c+=1

# print(c+1)

# Probably wrong code (Has a bug too)

while test.index(test[c]) < test.index(test[-1]):

    c+=1

print(c+1)
