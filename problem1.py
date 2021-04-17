
"""
-------------------------------------------------------------------------------
Name:   forloop.py
Purpose:  find the placement for the players
 
Author: Chan.E
 
Created:  03/03/2021
------------------------------------------------------------------------------
"""

print ("*******Tournament Tracker*******")

#varible
win = ""

#find the wins and losses
print("Enter the wins and losses for your team:")

#loop
for i in range (6):
  result = input("")
  if result == "w":
    wins += result

#find the team
if len(wins) >= 5:
   print ("Your team is in Group 1")
elif len(wins) >= 3 and len(wins) < 5:
   print ("Your team is in Group 2")
elif len(wins) >= 1 and len(wins) < 3:
   print ("Your team is in Group 3")
else:
   print ("Your team has been eliminated from the tournament")
  
