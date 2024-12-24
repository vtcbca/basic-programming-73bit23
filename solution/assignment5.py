string = input("Write string: ")
print(string, "is a palindrome." if string == string[::-1] else "is not a palindrome.")
