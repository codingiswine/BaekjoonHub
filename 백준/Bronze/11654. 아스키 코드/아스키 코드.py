user_input = input()

if len(user_input) == 1 and user_input.isalpha():
    ascii_code = ord(user_input)
    print(ascii_code)

elif len(user_input) == 1 and user_input.isdigit():
    ascii_code = ord(user_input)
    print(ascii_code)