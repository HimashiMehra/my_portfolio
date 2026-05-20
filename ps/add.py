# #Code Sum Of Two Numbers
# a=int(input("Enter a no a: "))
# b=int(input("Enter a no b: "))
# c=a+b
# print("SUM:",c)

# #Avrage input 10,20=15
# #swap no.
# a=10
# b=20
# c=a
# a=b
# b=c
# print(a)
# print(b)
# #without  using variable swapping
# a=10
# b=30
# a=a+b#a=10+30=40
# b=a-b#b=40-30=10
# a=a-b#a=40-10=30
# print("Value of a:",a)
# print("Value of b:",b)
#3rd way
# a=9
# b=8
# a,b=b,a
# print(a)
# print(b)
#discount
# amount=540
# discount=20
# #price=540*20/100
# price=amount*discount/100
# print(price)

#max numbers
a=100
b=96
c=78
if a>b and a>c:
    print("A is Max",a)
elif a<b and a>c:
    print("A is 2nd Max",a)
elif a>b and a<c:
    print("A is 3rd Max",a)
elif a<b and a<c:
    print("A is 3rd Max",a)

if b>a and b>c:
    print("B is Max",b) 
elif b>c and b<a:
    print("B is 2nd MAX",b)
elif b<c and b>a:
    print("B is 2nd MAX",b)
elif b<a and b<c:
    print("B is 3rd MAX",c)


if c>a and c>b:
    print("c is Max",c)
elif c>b and c<a:
    print("c is 2nd Max",c)
elif c<b and c>a:
    print("c is 2nd Max",c)
elif c<a and c<b:
    print("c is 3rd MAX",c)   




