import random

n = int(input("enter number of digits: "))
otp = random.randrange(10**(n-1), 10**n)
print("OTP", otp)
