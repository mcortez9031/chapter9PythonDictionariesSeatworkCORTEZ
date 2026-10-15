print('=========Record Keeping App========')
print('a. Add Data')
print('b. Delete Data')
print('c. End')
info = dict()
counts = 0
try:
    user_input = int(input('Selection Action: '))
    if user_input == 'a':
        user_prompt = input(str('Enter a key: Age '))
        user_in = input('Enter value: ', 0) + 1

        print(user_prompt, user_in)

    if user_input == 'b':
        user_prompt = input('Enter a key: Name')
        print(user_prompt)

    elif user_input == 'c':
        print("THANK YOU. Your program will end now")
        exit()

except ValueError:
        print('Key does not exists!')