import os
import getpass
import webbrowser

os.system("cls")
print(" ------------------------\n| Piggy's Trolling Tools: |\n|   :-: RickRoller :-:    |\n ------------------------\n")

number = int(input("Enter total number of rickrolls: "))

getpass.getpass(prompt=f"\nPress enter to play {number} rickrolls\n")

for i in range(number): 
      webbrowser.open("https://piggyawesome.com/free-bobux.html")
        

print("\nFinished.\n")


