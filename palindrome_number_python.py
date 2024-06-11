def palindrome_number(x):
    if str(x)[::-1]==str(x):
        return "Palindrome"
    else:
        return "Not a Palindrome"

print(palindrome_number(101))