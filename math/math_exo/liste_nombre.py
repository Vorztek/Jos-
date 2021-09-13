#age = int(input("Age:"))

#if age <= 13:
    #print("Yes")

#else:
    #print("No")

a = [1, 2, 3, 4, 5]
b = []

for i in a:
    b.append(i * 2)
c = [num * 2 for num in a]
print(c)
