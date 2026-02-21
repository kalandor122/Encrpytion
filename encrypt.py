import random

def listToString(s):
   
    # initialize an empty string
    str1 = " "
   
    # return string 
    return (str1.join(s))

def find_indices(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    return indices

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


message = list(input("what is the message:"))
keyone = []
keytwo = []
keythree =  []
x = random.randrange(1, 10)
y = random.randrange(1, 999)

print(message)
for i in range(len(message)):
    keyone.append(str(abc.index(message[i]) + 1))
    keytwo = listToString(keyone)
    keyfour = ''.join(keyone)
    keytwo = keytwo.replace(" ", ",")
    print(list(keytwo))


keythree = (find_indices(list(keytwo), ","))
keyfive = (x, y)
keyfour = int(keyfour) * x
keyfour = int(keyfour) + y

for i in range(len(keythree)):
    if i == 0:
        print("")
    else:    
        keythree[i] = keythree[i] - 1 


print(f"1. kulcs {keythree}")
print(f"2. kulcs {keyfive}")

print(keyfour)





