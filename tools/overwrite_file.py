import glob
import os
import getpass

print(" ------------------------\n| Piggy's Trolling Tools: |\n| :-: File Overwriter :-: |\n ------------------------\n")

where = input("Input directory where files should be overwrited: ")
regex = input("Enter regex to match files (example: important*.txt): ")
message = input("Enter message that should be written inside the files: ")

os.chdir(where)

os.system("cls")

file_list = glob.glob(regex)
print(f"Loaded {file_list.__len__()} files:\n")
print(file_list)

getpass.getpass(prompt="\nPress enter to overwrite\n")

for file_ in file_list: 
  try:
   with open(file_, "w") as overwite:
        overwite.write(message)
        print(f"Written: \"{message}\" inside \"{file_}\" |")
  except Exception as error:
        print(error)
        pass

print("\nFinished.\n")


