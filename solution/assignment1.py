n = int(input("Enter a Number for Factorial = "))
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i += 1
print("The factorial of", n, "is:", fact)
