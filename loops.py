c=list(range(1,5))

for i in c:
    if i ==3:
        print("found no 3")
        break
print(c)

#finding the multiples of 3 and 5 and adding their sum
# 1,2,3,4,5,6,7,8,9= 3+6+9=`18` +15= 33
sum=0
for i in range(1,11):
    if i % 3==0 or i%5==0:
        sum+=i

    # sum+=i

print(sum)

leters= [1,2,3,4,5,6,6,7]

for i in range(len(leters)):
    print(i)