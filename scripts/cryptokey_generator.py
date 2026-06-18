from cryptography.fernet import Fernet

new_key = Fernet.generate_key().decode()
print(new_key)

choice = input("Overwrite the cryptokey.txt file? (y/n): ")

if choice == "y":
    with open("../cryptokey.txt", "w", encoding="utf-8") as f:
        f.write(repr(new_key))
elif choice == "n":
    print("Operation cancelled")
else:
    print("Invalid input")