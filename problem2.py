
"""
-------------------------------------------------------------------------------
Name:   whileloop.py
Purpose:  find the distance driven per day
 
Author: Chan.E
 
Created:  03/03/2021
------------------------------------------------------------------------------
"""

print ("****Welcome to the DoorDash Distance Tracker****")

#find the distance travelled
print ("**Travel Log***")
total = 0
dis_travel = 0

kilometers = int(input("Enter distance travelled for the day (100 to stop): "))

while kilometers = 100:
 total = total + kilometers
 dis_travel = += 1
 kilometers = int(input("Enter distance travelled for the day (100 to stop): "))

#summary
print ("**Summary**")

average = total/dis_travel

print ("It took " + total + " days to surpass 100km driven." )
print ("the average distance driven per day is " + average + "." ")