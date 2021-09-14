from genericpath import isdir
import glob
import os
import getpass

print(" ------------------------\n| Piggy's Trolling Tools: |\n| :-: Folder Clearer :-:  |\n ------------------------\n")


where = input("Folder Directory: ")

os.chdir(where)

os.system("cls")

file_list = glob.glob("*")
print(f"Loaded {file_list.__len__()} files and folders:\n")
print(file_list)

getpass.getpass(prompt="\nPress enter to delete\n")


def delete(file):
    try:
      if isdir(file) == True:
            os.rmdir(file)
      elif isdir(file) == False:
            os.remove(file)
      return True
    except NotADirectoryError: 
      return False
    except FileNotFoundError:
       return None

while file_list != []:
   for file_ in file_list: 
      try:
            os.chdir(where)
            resp = delete(file_)
            if resp == True or None:
                print(f"Removed: | \"{file_}\" |")
                file_list.remove(file_)    
            else: 
                 exit()
      except OSError as error:
            print(f"Clearing | {file_} |")
            os.chdir(f"{file_}")
            glob2 = glob.glob("*")
            for file in glob2:
                e = os.path.realpath(file)
                file_list.append(e)
            pass
      except FileNotFoundError:
            pass



print("\nFinished.\n")


