user_input = input("Enter a string: ")
lowercase = []
uppercase = []

for char in user_input:
    if char.islower():
        lowercase.append(char)
    elif char.isspace():
        continue
    else:
        uppercase.append(char)

print(f'{"".join(lowercase)}{"".join(uppercase)}')
