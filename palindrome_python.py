def string_palindrome(strg):
    if strg[::-1].capitalize()==strg.capitalize():
        return "Palindrome"

    else:
        return "Not a palindrome"

print(string_palindrome("Rahul"))
print(string_palindrome("Malayalam"))