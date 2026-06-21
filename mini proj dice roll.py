#dice the roll game
import random 

total_rolls = 0

while True :
 choice = (input ("roll the dice? (y/n): ")).lower()
 if choice == "y" :
    new_dice = int(input("How many dice you want to roll?"))
    if new_dice <= 0:
      print("Number should be greater than 0.")
      continue
    for i in range (new_dice):
     
     print("You rolled " f"dice {i+1}:{random.randint(1,6)}")
     
    total_rolls += new_dice
    print(f"Total dice rolled so far :{total_rolls}")
       
 elif choice == "n" or choice == "N" :
    print("Thanks for playing!")
    break
 else:
   print("Invalid choice")

