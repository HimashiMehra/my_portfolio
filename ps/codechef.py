# t = int(input())

# for _ in range(t):
#     n = int(input())
#     s = input()

#     count = 0

#     for ch in s:
#         if ch not in "aeiou":
#             count += 1
#         else:
#             count = 0

#         if count >= 4:
#             print("Yes")
#             break
#     else:
#         print("No")
    
    # Number of test cases
t = int(input("Enter a no."))

for _ in range(t):
    n = int(input("Enter a length of array"))
    
    a = list(map(int, input().split()))

    array_min= 100;
    for i in range(n):
         for j in range(i + 1, n):

            if a[i] == a[j]:
                swaps = i + (n - 1 - j)

    
                if swaps < array_min:
                    array_min = swaps
    if array_min==100:
        print(-1)

    else:
        print(array_min)