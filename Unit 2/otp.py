n = int(input("Enter number of terms: "))

a = 0
b = 1

if n >= 1:
    print(a, end=" ")

if n >= 2:
    print(b, end=" ")

for i in range(3, n + 1):
    c = a + b
    print(c, end=" ")

    a = b
    b = c








# import random
# otp = random.randint(100000,999999)
# print("the otp is:", otp)

