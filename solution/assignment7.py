n = int(input("Enter a number: "))

i = 1
while i <= n:
    print('  ' * (n - i), end=' ')
    
    j = 1
    while j < 2 * i:
        print(j, end="  ")
        j += 1
    
    print()
    i += 1
