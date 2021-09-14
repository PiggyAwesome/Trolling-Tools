import subprocess
import os
os.system("cls")
print("#"*40)
print(r"    __      __      __     __    __   ")
print(r"   //\\    //\\    //\\   //\\  //\\  ") 
print(r" <      (TROLLING)      (TOOLS)      >")
print(r"   \\//    \\//    \\//   \\//  \\//  ")
print()
print("#"*40)
print("# [1] Overwrite Files                  #")
print("# [2] Clear Folder                     #")
print("# [3] Delete Folders                   #")
print("# [4] Delete Files                     #")
print("# [5] Create Files                     #")
print("# [6] Create Folders                   #")
print("# [7] Startup Troll                    #")
print("# [8] Rickroll                         #")
print("#"*40)          
num = int(input(':: '))

os.system("cls")

if num == 8:
    subprocess.run(f"python tools/rickroll.py")

if num == 7:
    subprocess.run(f"python tools/startup_troll.py")

if num == 6:
    subprocess.run(f"python tools/create_folder.py")

if num == 5:
    subprocess.run(f"python tools/create_file.py")

if num == 4:
    subprocess.run(f"python tools/delete_file.py")

if num == 3:
    subprocess.run(f"python tools/delete_folder.py")

if num == 2:
    subprocess.run(f"python tools/clear_folder.py")

if num == 1:
    subprocess.run(f"python tools/overwrite_file.py")
