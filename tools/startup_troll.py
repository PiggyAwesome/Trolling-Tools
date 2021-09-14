import getpass
import random
import os


print(" ------------------------\n| Piggy's Trolling Tools: |\n| :-:  Startup Troll  :-: |\n ------------------------\n")


folder = input("Create files or folders?: ")
if "file" in folder:
  folder = False
elif "folder" in folder:
  folder = True

total = int(input("Enter number of files/folders that should be created: "))
name = input("Enter name of files/folders: ")

# FILE  SPECIFIC ##
if folder == False:
 ext = input("Enter the extention that the files shoud have (example: .txt, .py): ")
 message = input("Enter message that should be written inside the files: ")
# # # # # # # # # #


computer_name = getpass.getuser()
startup = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % computer_name


def add_to_startup(name, ext):
  try:
    if folder == False:         
             randomnum = random.randrange(100)
             with open(f"{startup}\{name}{randomnum}{ext}", "w") as file_:
                 file_.write(message)
                 print(f"Created: \"{name}{randomnum}{ext}\" & Written \"{message}\" inside |")
         
    if folder == True:         
             randomnum = random.randrange(100)
             os.mkdir(f"{startup}\{name} #{randomnum}")
             print(f"Created: \"{name}{randomnum}\" |")
  except Exception as err:
       print(err)
       pass


for i in range(total):
    add_to_startup(name,ext) 