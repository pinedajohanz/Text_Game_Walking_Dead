#theme: Survival against Zombies
# variables
# comparison operators
# if-else statement
import time
# TITLE OF THE GAME


print(''' 

▀▀█▀▀ ▒█░▒█ ▒█▀▀▀ 　 ▒█░░▒█ ░█▀▀█ ▒█░░░ ▒█░▄▀ ▀█▀ ▒█▄░▒█ ▒█▀▀█ 　 ▒█▀▀▄ ▒█▀▀▀ ░█▀▀█ ▒█▀▀▄ 
░▒█░░ ▒█▀▀█ ▒█▀▀▀ 　 ▒█▒█▒█ ▒█▄▄█ ▒█░░░ ▒█▀▄░ ▒█░ ▒█▒█▒█ ▒█░▄▄ 　 ▒█░▒█ ▒█▀▀▀ ▒█▄▄█ ▒█░▒█ 
░▒█░░ ▒█░▒█ ▒█▄▄▄ 　 ▒█▄▀▄█ ▒█░▒█ ▒█▄▄█ ▒█░▒█ ▄█▄ ▒█░░▀█ ▒█▄▄█ 　 ▒█▄▄▀ ▒█▄▄▄ ▒█░▒█ ▒█▄▄▀ 
 
''')

print()

# enter user's survivor's name
time.sleep(1) # delay on appearance of text
name = input("Please enter your survivor's name: ")
time.sleep(1)
print(f"Welcome to the Apocalypse, {name} live or die")

# variable for entering the game
time.sleep(1)
start = input("Would you continue to survive or die alone? (continue/not) ")
if start.lower() == "continue": # if user input continue he will enter the game
    time.sleep(1)
    print("Good choice survivor! Let's survive this apocalyptic world.")
    time.sleep(2)
    chap1 = input("You woke up in a hospital room. You feel dizzy and don't remember any past memory on how you got here. Do you want to go outside of the room or just stay put? (outside/stay) ")
else: 
    time.sleep(1)
    print("Bad choice! Go die then!")
    quit() # stops the program

if chap1.lower() == "outside": # == a or b
    time.sleep(1)
    print("You go outside of the room. In the hallways, you noticed that there are no signs of persons just messy hospital equipments lying around the long hallway. Do you want to go outside the hospital or go back to your room? ")
    chap2 = input("(outside/room) ")


if chap1.lower() == "stay":
    time.sleep(1)
    print("You waited in the room for a very long time and you starved to death. GAME OVER!")
    quit() # function to stop the program

if chap2.lower() == "outside":
    time.sleep(1)
    print("You see a lot of parked vehicles in front of the hospital. You are planning to go to a police station nearby. Would you go walk or borrow a vehicle going there? ")
    time.sleep(1)
    chap3 = input("(walk/vehicle) ")


if chap2.lower() == "room":
    time.sleep(1)
    print("You waited in the room for a very long time and you starved to death. GAME OVER!")
    quit()

if chap3.lower() == "vehicle":
    time.sleep(1)
    print("You borrowed a private vehicle to go to the police station. You saw a person waving at you in the distance upon getting closer to the person, you saw a bite mark in his arm. Would you help him or passed by him?")
    chap4 = input("(help/pass) ")

if chap3.lower() == "walk":
    time.sleep(1)
    print("You are now walking in the streets going to the police station then suddenly a horde of zombies attacked you behind and then you died. GAME OVER!")
    quit()

if chap4.lower() =="pass":
    time.sleep(1)
    print("You drove by passed the person and went straight to the police station")
    time.sleep(1)
    print("Upon arriving at the police station, you notice some survivors who are barricading themselves inside the police station.")
    time.sleep(1)
    print("You approached them and told them that you've been in a coma for a long time and don't have any memory on what's happening right now.")
    time.sleep(1)
    print("They (other survivors) assisted you and brought you inside the police station then explained to you on what happened in this apocalyptic world.")
    time.sleep(1)
    print("TO BE CONTINUED.....") # good ending


if chap4.lower() == "help":
    time.sleep(1)
    print("You stopped by in front of him and let him in your vehicle then suddenly he bites you that caused you your life. GAME OVER!")