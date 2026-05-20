#Reverse Numbers
a=123
rev=0
while a!=0 :
    id=a%10
    rev=rev*10+id
    a=a//10
print(rev)
#amount of notes 5631-->500,100,20,10,1
amount = 5031
if amount >= 500:
    rs500 = amount // 500
    amount = amount % 500
    print("500 rs notes =", rs500)
else:
    print("500 rs notes = 0")
if amount >= 100:
    rs100 = amount // 100
    amount = amount % 100
    print("100 rs notes =", rs100)
else:
    print("100 rs notes = 0")
if amount >= 20:
    rs20 = amount // 20
    amount = amount % 20
    print("20 rs notes =", rs20)
else:
    print("20 rs notes = 0")
if amount >= 10:
    rs10 = amount // 10
    amount = amount % 10
    print("10 rs notes =", rs10)
else:
    print("10 rs notes = 0")
if amount >= 1:
    rs1 = amount // 1
    print("1 rs notes =", rs1)
else:
    print("1 rs notes = 0")