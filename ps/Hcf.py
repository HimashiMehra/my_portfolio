
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

hcf = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        hcf = i

lcm = (a * b) // hcf

print("HCF =", hcf)
print("LCM =", lcm)

#Write a program to check whether a number is Armstrong or not. (Armstrong number is a number that is equal to the sum of cubes of its digits, for example, 153 = 1^3 + 5^3 + 3^3.)
a=int(input("Enter a number:"))
