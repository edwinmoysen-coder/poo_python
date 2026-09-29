l1 = [1,2,3]
l2=l1
l3=[1,2,3]

l1 [0] = 999

print (f"l1 {l1}")
print (f"l2 {l2}")
print (f"l3 {l3}")


if l1 is l2:
    print("l1 es l2")

if l1 is l3:
    print("l1 es l3")
else:
    print("l1 no es l3")
    
