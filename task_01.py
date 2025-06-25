import re


def is_palindrome(string):

    if string is None:
        return False

    if not isinstance(string, str):
        string = str(string)


    string = re.sub(r'[^a-z0-9]', '', string.lower())


    for i in range(len(string) // 2):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True




print(is_palindrome("A man, a plan, a canal -- Panama")) # => True
print(is_palindrome("Madam, I'm Adam!")) # => True
print(is_palindrome(333)) # => True
print(is_palindrome(None)) # => False
print(is_palindrome("Abracadabra"))