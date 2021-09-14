import os
import getpass
import random


print(" ------------------------\n| Piggy's Trolling Tools: |\n| :-:  File Creator   :-: |\n ------------------------\n")

where = input("Input directory where files should be created: ")
name = input("Enter file name: ")
ext = input("Enter file extention: ")
message = input("Input message to write inside file: ")
total = int(input("Enter amount of files: "))

os.chdir(where)

os.system("cls")

getpass.getpass(prompt=f"\nPress enter to create {total} files\n")

for i in range(total):
    randomnum = random.randrange(100)
    with open(f"{name}{randomnum}{ext}", "w") as file_:
        file_.write(message)
        print(f"Created: \"{name}{randomnum}{ext}\" & Written \"{message}\" inside |")

print("\nFinished.\n")
