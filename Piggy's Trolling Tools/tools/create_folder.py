


import os
import getpass
import random

print(" ------------------------\n| Piggy's Trolling Tools: |\n| :-: Folder Creator  :-: |\n ------------------------\n")

where = input("Input directory where folders should be created: ")
name = input("Enter folder name: ")
total = int(input("Enter amount of Folders: "))

os.chdir(where)

os.system("cls")

getpass.getpass(prompt=f"\nPress enter to create {total} folders\n")
for i in range(total):
   try:

     randomnum = random.randrange(100)
     os.mkdir(f"{name} #{randomnum}")
     print(f"Created: \"{name} #{randomnum}\" |")

   except Exception as error:
      print(error)
      pass

print("\nFinished.\n")
