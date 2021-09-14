import glob
import os
import getpass
import os.path

print(" ------------------------\n| Piggy's Trolling Tools: |\n| :-: Folder Deleter :-:  |\n ------------------------\n")

where = input("Input directory where folders should be deleted: ")
regex = input("Enter regex to match folders (example: important*): ")

os.chdir(where)

os.system("cls")

folder_list = glob.glob(regex)

for possible_folder in folder_list:
    if os.path.isdir(possible_folder) == False:
        folder_list.remove(possible_folder)

print(f"Loaded {folder_list.__len__()} Folders:\n")
print(folder_list)

getpass.getpass(prompt="\nPress enter to delete\n")

for folder_ in folder_list: 
  try:
        os.rmdir(folder_)
        print(f"Removed: \"{folder_}\"|")
  except Exception as error:
        print(error)
        pass

print("\nFinished.\n")


