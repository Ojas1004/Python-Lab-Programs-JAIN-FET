num = int(input("enter a number: "))
if num <= 1:
    print("not a prime number")
else:
    prime= True

    for i in range (2,num):
        if num % i == 0:
            primt = False
            break
    if prime:
        print("Prime Number")
    else:
        print("not a prime number")