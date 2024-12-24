num = int(input("Enter a number to check if it's prime or not = "))

if num <= 1:
    print(num, "is not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is Not Prime")
            break
    else:
        print(num, "is Prime")
