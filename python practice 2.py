num = int(input("emter the number"))

orgi = num
orgi2 = num
count = 0 
sum2 = 0

while num>0:
    num = num // 10
    count += 1

# while num>0:
#     digit = num%10
#     sum+=digit

while orgi>0:
    digi = orgi%10
    sum2 +=digi**count
    orgi= orgi//10


if orgi2 == sum2:
    print(orgi2,"is a armstrong number")

else:
    print("not a armstrong number")

print(sum2)