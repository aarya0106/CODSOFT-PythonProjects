import random

print("=== PASSWORD GENERATOR ===")

# Ask the user for the length
password_length = int(input("How many characters long should the password be? "))

# A simple human-style check to make sure they didn't type 0 or a negative number
if password_length <= 0:
    print("Error: Password length must be greater than 0!")
else:
    all_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    generated_password = ""

    # Loop as many times as the user requested length
    for i in range(password_length):
        random_char = random.choice(all_chars)
        generated_password = generated_password + random_char

    # Print the final result
    print("\nYour new password is:")
    print(generated_password)