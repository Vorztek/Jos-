from gen_nombre2 import gen_number

liste1 = [0]
liste2 =  [1, 2, 3, -1, 1851, 8999, -151, 22, -5000]

value = gen_number(20,100)
#print(value)
#print(type(liste1))

def minimum():
    min_value = value[0]
    for i in value:
        if i > min_value:
            min_value = i
    return min_value

print(minimum())
print(max(value), min(value))