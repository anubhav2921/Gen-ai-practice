def palindrome(string):

    string_value = string.lower().replace(""," ")

    if string_value == string_value [::-1]:
        print("the current string is pslindrom")

# Enter a string = Aba
# the current string is pslindrom

    else:
        print("the current string is not palindrom")


input_string = input("Enter a string = ")     

palindrome(input_string)
            