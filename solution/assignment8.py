row = int(input('Enter how many lines? '))
a = 64
i = 1
while i <= row:
    j = 1
    while j <= row - i:
        print(' ', end='')
        j += 1
    
    j = 1
    while j <= i:
        print('%c' % (a + j), end='')
        j += 1
    
    j = i - 1
    while j >= 1:
        print('%c' % (a + j), end='')
        j -= 1
    
    print()
    i += 1
