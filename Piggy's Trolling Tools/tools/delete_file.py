import glob
import os
import getpass

print(" ------------------------\n| Piggy's Trolling Tools: |\n|  :-: File Deleter :-:   |\n ------------------------\n")

where = input("Input directory where files should be deleted: ")
regex = input("Enter regex to match files (example: important*.txt): ")

os.chdir(where)

os.system("cls")

file_list = glob.glob(regex)
print(f"Loaded {file_list.__len__()} files:\n")
print(file_list)

getpass.getpass(prompt="\nPress enter to delete\n")

for file_ in file_list: 
  try:
        os.remove(file_)
        print(f"Removed: \"{file_}\"|")
  except Exception as error:
        print(error)
        pass

print("\nFinished.\n")


