terms = int(input("Enter the number of terms = "))
if terms <= 0:
    print("Please enter a valid positive number")
else:
    num1, num2 = 0, 1
    for _ in range(terms):
        print(num1, end=" ")
        num1, num2 = num2, num1 + num2 