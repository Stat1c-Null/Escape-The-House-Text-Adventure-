from colorama import Fore, Back, Style
import random
import sys

def reset():
  print(Style.RESET_ALL)

player_location = "start_room"
name = input(Fore.LIGHTYELLOW_EX + "Enter your hero's name: ")
reset()
player_data = {
  "name": name,
  "location_desc": "You are in a small dining room, in the unknown house. There is only dining table in this room, and a few chairs knocked on the ground. On the table you see left over food from someone's dinner. The food is covered in blood and you can see someone's finger on the plate. You better find your way out of this place or you will be the next on this plate. You can walk forward to get to the kitchen and walk to the left to get to the family room.",
  "location_name": player_location,
  "health": 100
}
inventory = []
ShotgunAmmo = 1
room_description = ""
room_text = ""
current_room = ""
#Move between rooms
def next_room(name, description, room_object, moves_text):
  global player_data, current_room, room_text
  player_data["location_name"] = name 
  player_data["location_desc"] = description
  current_room = room_object
  room_text = moves_text  

class Location:
  def __init__(self, moves, actions, keys):
    self.moves = moves
    self.actions = actions
    self.keys = keys
    self.description = "You are in a small dining room, in the unknown house. There is only dining table in this room, and a few chairs. You can walk forward to get to the kitchen and walk to the left to get to the family room. On a table, you can see a big bloody knife. You dont know who used it before you, but you might wanna pick it up to protect yourself later"


#Help function for dumb players
def help_file():
  print(Back.GREEN + "\n-----------------------------------\n")
  print("You will be exploring the house in order to escape it\n")
  print("Use words like 'forward', 'left', 'right', 'back' to move around house\n")
  print("when you want to use an item in the game, just enter the name of the item like 'keys' and see what actions you can do\n")
  print("To see the description of the room again, type in 'description'\n")
  print("To see this help file again, type in 'help'\n")
  print("When you are ready to continue, pree the ENTER to EXIT this screen\n")
  input()
  print("\n-----------------------------------\n")
  reset()

#ROOM 1 - Start Room -------------------------------------------
start_room_keys = {"light" : "off"}
start_room = Location(("forward", "left"), ("light"), start_room_keys)
start_room_text = Fore.LIGHTMAGENTA_EX + "\nCurrent Room: Dinning Room\n" + Fore.BLUE + "\nMoves: forward, left\n\nActions: light\n"
start_room_description = "You are in a small dining room, in the unknown house. There is only dining table in this room, and a few chairs. You can walk forward to get to the kitchen and walk to the left to get to the family room. "

def start_room_moves_actions(player_input):
  if player_input in start_room.moves:
    start_room_moves(player_input)
  elif player_input in start_room.actions:
    start_room_actions(player_input)
  else:
    print("Invalid Move")
    play_game()

def start_room_moves(player_input):
  global player_location, room_description, room_text, current_location_name
  if player_input == "left":
    print("\n--------\nYou walk out to the living room. You are in a strange living room, that looks like a maniac lived in. The floors are covered with dust, dirt, and empty beer cans. Tv is on, but it's only showing static. Couch is soaked in blood and covered with dirty clothes on top of it. On the floor near the couch you can see an ashtray full of cigarettes. On the table next to the couch you can see an old wired phone. The windows in living room are also locked with metal frames. To the right of yourself, you can see a door that looks like it's leading to the basement. To the left of you can see a door that is leading to garage. And you can also see a big metal front door that looks like it's leading outside")
    room_description = "\n--------\nYou are in a strange living room, that looks like a maniac lived in. The floors are covered with dust, dirt, and empty beer cans. Tv is on, but it's only showing static. Couch is soaked in blood and covered with dirty clothes on top of it. On the floor near the couch you can see an ashtray full of cigarettes. On the table next to the couch you can see an old wired phone. To the right of yourself, you can see a door that looks like it's leading to the basement. To the left of you can see a door that is leading to garage. And you can also see a big metal front door that looks like it's leading outside."
    #switch rooms
    next_room("living_room", room_description, living_room, living_room_text)
  elif player_input == "forward":
    print("\n--------\nYou walk into a kitchen, and a nasty smell hits your nose. You look around and you see a fridge, with blood pouring out of it. There is a window in the kitchen, but it's locked with metal frame.")
    room_description = "\n--------\nYou are inside of destroyed kitchen. Cabinets are mostly opened or don't have doors at all. There is a bloody fridge in the corner, sink full of water, and puddles of blood on the floor. On a table, you can see a big bloody knife. You dont know who used it before you, but you might wanna pick it up to protect yourself later"
    #SWITCH ROOMS 
    next_room("kitchen", room_description, kitchen, kitchen_text)


def start_room_actions(player_input):
  if player_input == "light":
    print("\n--------\nIn darkness, you somehow manage to find a light switch, and turn it on. As the lights turn on, you realize that your finger, and lightswitch, and entire dining is in blood")
    start_room.keys["light"] = "on"

#ROOM 1 END ------------------------------------------------

#Kitchen Start ---------------------------------------------
kitchen_keys = {"fridge" : "closed"}
kitchen = Location(("back"), ("fridge", "knife", "cabinets", "sink"), kitchen_keys)
kitchen_text = Fore.LIGHTMAGENTA_EX + "\nCurrent Room: Kitchen\n" + Fore.BLUE + "\nMoves: \n back \nActions:\n fridge, knife ,cabinets ,sink\n"

def kitchen_moves_actions(player_input):
  if player_input in kitchen.moves:
    kitchen_moves(player_input)
  elif player_input in kitchen.actions:
    kitchen_actions(player_input)
  else:
    print("Invalid Move")
    play_game()

def kitchen_moves(player_input):
  if player_input == "back":
    print("\n--------\nYou walked back into a nasty dining room")
    #SWITCH ROOMS
    next_room("start_room", start_room_description, start_room, start_room_text)

def kitchen_actions(player_input):
  if player_input == "knife":
    inventory.append("knife")
    print("\n--------\nWith shaky hands you carefully pick up the knife off the table. The red stains is definitely someone's blood. You gripped the knife in your hand but it slipped through and fell down because of all the blood. That scared you, but you hurried up to pick it back up and this time you hold it better")
  elif player_input == "fridge":
    print("\n--------\nWith shaky hands you grab blody handle and pull the door. Inside the fridge there where bags and bags of bloody organs, probably for sale. This is definitely not a good house to stay for long, cause your organs might join the party in the fridge. Your heartbeat increases, you feel like you going to faint if you keep looking, so you slam the fridge door but you accidentally hit your finger while doing it and it starts bleeding.")
    player_data["health"] -= 5
  elif player_input == "shotgun":
    print("\n--------\nOn top of the counter you see that someone left a pump-action shotgun with a few bullets next to it. This place is definitely dangerous, so you grab a shotgun to help you along the way. Shotgun feels heavy and cold, someone left it here a few hours ago")
    inventory.append("shotgun")
  elif player_input == "cabinets":
    print("\n--------\nYou start searching around the broken cabinets, in hopes of finding something. So far you have only been founding rats and old bread, but luckily in the last cabinet you found a medkit! Nice.")
    inventory.append("medkit")
  elif player_input == "sink":
    print("\n--------\nYou walked up to the kitchen sink and looked in it. The sink was full of dirty water, and you were able to see the reflection of your face. You notice that your face is covered in bruises and blood as well. You must of been kidnapped, beaten and brought over here. You step back in fear")



#Kitchen End -----------------------------------------------------
#Living Room Start -----------------------------------------------
living_room_keys = {"front door" : "locked", "basement door" : "locked", "garage door" : "locked", "phone" : "off", "tv" : "off"}
living_room = Location(("forward", "stairs", "right", "left", "basement door", "garage door", "back"), ("front door", "adjust tv", "use phone"), living_room_keys)
living_room_text = Fore.LIGHTMAGENTA_EX + "\nCurrent Room: Living Room\n" + Fore.BLUE + "\nMoves: \n forward, right, left, back, basement door, garage door, stairs \nActions:\n front door, adjust tv, use phone\n"

def living_room_moves_actions(player_input):
  if player_input in living_room.moves:
    living_room_moves(player_input)
  elif player_input in living_room.actions:
    living_room_actions(player_input)
  else:
    print("Invalid Move")
    play_game()

def living_room_moves(player_input):
  if player_input == "forward" or player_input == "stairs":
    print("\n--------\nYou walk up the stairs")
  elif (player_input == "left" or player_input == "garage door") and living_room.keys["garage door"] == "locked":
    print("\n--------\nYou try to open the garage door, but it seem's to be locked. Try looking around the house for something to open it with. Maybe there is a knife or lockpick somewhere")
  elif (player_input == "left" or player_input == "garage door") and living_room.keys["garage door"] == "open":
    print("\n--------\nYou walk into garage")
  elif (player_input == "right" or player_input == "basement door") and living_room.keys["basement door"] == "locked":
    print("\n--------\nYou attempt to open basement door, but it won't budge. Try looking around the house for something to open it with. Maybe there is a knife or lockpick somewhere")
  elif (player_input == "right" or player_input == "basement door") and living_room.keys["basement door"] == "open":
    print("\n--------\nYou walk into basement and a nasty rotting smell instantly hits your nose. It's impossibly hard to stay in this place, but you have to get through it, because there might be useful things in this basement. The basement looks old and run down, but there are still doors dividing rooms.")
    room_description = "\n--------\nThe basement looks old and run down, but there are still doors dividing rooms. There is a lot of tools throwed around everywhere, rolls of duct tape on the floor, dirty walls everywhere. The rotten smell is very strong down here. There is an old door leading forward right off the stairs. There is a new door to the left of the stairs. And there is another small old door to the left of the stairs. "
    #SWITCH ROOMS
    next_room("basement_room", room_description, basement_room, basement_room_text)
  elif player_input == "back":
    print("\n--------\nYou went back to the dinning room")
    next_room("start_room", start_room_description, start_room, start_room_text)
  

def living_room_actions(player_input):
  global name
  if player_input == "front door" and living_room.keys["front door"] == "locked":
    print("\n--------\nYou happily run to the front door, hoping your hell of a stay in this place will be over soon. But very soon your dreams gets crushed by the metal front door, that wont budge at all, and the only way to open it, is to use a key.")
  elif player_input == "front door" and living_room.keys["front door"] == "open":
    print("\n--------\nYou open the door, and run away like a free bird")
  elif player_input == "adjust tv" and living_room.keys["tv"] == "off":
    print("\n--------\nYou fix antenna on top of the TV, and you adjust channel and volume buttons to broadcast local news channel. The news reporter was telling latest news: And to the other news, we are still searching for " + name + " who has disappeared yesterday night around 9 pm. They left for the bar at 8 30 pm, after 9 pm their phone wasn't available anymore. Last place they were seen is Red Light District. Witnesses say that a suspicios white van was driving around that district at that time. If you have any information related to this case, please call us at 404-394-8567")
    ch = input("\n--------\nWould you like to try and remember this phone? Type Y or N").upper()
    if ch == "Y":
      rand = random.randint(1, 10)
      if rand >= 6:
        print("You repeated phone number in your head a few times and remembered it")
        inventory.append("404-394-8567")
      else:
        print("You tried to remember phone number, but the tv quickly switched the screen to an add and you couldn't remember it")
    else:
      print("You didn't care enough to remember the phone number and screen switched to an add")
    living_room.keys["tv"] = "on"
        
  elif player_input == "adjust tv" and living_room.keys["tv"] == "on":
    print("\n--------\nTV is already on")
  elif player_input == "use phone" and living_room_keys["phone"] == "off":
    print("\n--------\nYou take the phone of the stand and put it next to your ear, but all you can hear is empty static indicating that phone is not connected to the phone line. If you can find where to connect phone to the line, you can call someone for help.")
  elif player_input == "use phone" and living_room_keys["phone"] == "on":
    print("\n--------\nYou pick up the phone, and ones you hear dial tone, you quickly call 911")
    #CHANGE LATER!!!!!!!!!!!!!!!!!!!!!!!!
#Living Room End ------------------------------------------------------------------------------

#Basement Room Start ----------------------------------------------------------------------
basement_room_keys = {"phone" : "off"}
basement_room = Location(("forward", "right", "left", "back"), ("find phoneline", "use computer", "grab shotgun"), basement_room_keys)
basement_room_text = Fore.LIGHTMAGENTA_EX + "\nCurrent Room: Basement Room\n" + Fore.BLUE + "\nMoves: \n forward, right, left, back \nActions:\n \n"

def basement_room_moves_actions(player_input):
  if player_input in basement_room.moves:
    basement_room_moves(player_input)
  elif player_input in basement_room.actions:
    basement_room_actions(player_input)
  else:
    print("Invalid Move")
    play_game()

def basement_room_moves(player_input):
  if player_input == "forward":
    print("\n--------\nYou open the door in front of you, and turn on the light switch. Inside the room, there are tables and toolboxes standing by every wall and every corner of the room. They are filled with all types of instrumets, tools, ropes, knifes, and even a few guns. Right in the middle of the room the was a table with just a shotgun and bullets on it.")
    basement_room_text = Fore.LIGHTMAGENTA_EX + "\nCurrent Room: Basement Room\n" + Fore.BLUE + "\nMoves: \n forward, right, left, back \nActions:\n use computer, follow wires, use phone, grab shotgun \n"
  elif player_input == "left":
    print("\n--------\nYou open the door on the left, and all of a sudden the rotten smell got like 10 times more worse. As you open the door, and light shines on the floor, you can already see big puddles of blood on the floor. As you turn on the switch and old light bulb lights up the room, and you can see stacks of rotten, bloody, naked bodies stacked up on top of each other in the pit. Some of the bodies are fresh, and some are been here for a very long time. You can't stand this horryfing sight for any longer, so you puke on the floor right before closing the door ones and forever. ")
  elif player_input == "right":
    print("\n--------\nYou open the newest door to the right, and for some reason you dont smell anything bad in this room. You walk in and close the door. The room looks like an old office, with computer table and phone, book shelves, warddrobe, and a stack of wires that are leading from computer and the phone on the table, to the back side of the room")
    basement_room_text = Fore.LIGHTMAGENTA_EX + "\nCurrent Room: Basement Room\n" + Fore.BLUE + "\nMoves: \n forward, right, left, back \nActions:\n use computer, follow wires, use phone, grab shotgun \n"


def basement_room_actions(player_input):
  global ShotgunAmmo
  failed = False
  if player_input == "use computer":
    print("\n--------\nYou press on the keyboard, and monitor lights on and shows a full body picture of you taken with a hidden camera. Have this guy been stalking you ? How many photos does he have ? You kept scrolling, but new photos kept on coming up. There was a picture of your house, your car, you on a sunday walk with your family, and a few face shots. You closed the photos and looked into a folder that was dated with your name. There was other pictures and also a text file named 'info', that you decided to open. \n NAME: " + name + "\nAGE: 29\nOCCUPATION: BUSINESS PERSON\nPOSSIBLE GAIN: KIDNAP AND RANSOM\nDESCRIPTION: ")
  elif player_input == "use phone":
    print("\n--------\nYou pick up the phone, but you can't hear any noise in it. You look down and you see the wires going from the phone into the depth of this room. You cant see where wires are connected because it's behind the wall. ")
  elif player_input == "grab shotgun":
    print("\n--------\nYou take stirdy shotgun in your hands and weight it. It feels cold and looks shiny.")
    inventory.append("shotgun")
  elif player_input == "grab ammo":
    print("\n--------\nYou look around the table where the shotgun was, and find 2 shotgun shells. You load one into the shotgun for practice")
    ShotgunAmmo += 2
  elif player_input == "follow wires" and failed == False:
    print("\n--------\nYou follow the stack of red, green, white wires to the back of the basement, and you find yourself standing next to powergenerator. This generator is supplying the entire house with power, and under the section where it says phone line, the plug is taken out. This must be why the phone won't work! But you can see 3 different wires that could potentially work for the phone line. Green, white and red. Which one of the wires is the correct one ?")
    wire = input("Enter color of the correct wire (green, white, red): ")
    if wire == "green":
      print("As soon as you insert the green plug inside, the entire generator starts sparking and burning, and starts making really bad sounds. You run away and hide behind the wall just in time, because generator explodes behind your back. ")
      failed = True
    elif wire == "red":
      print("As soon as you insert red plug inside, it shocks you with volts and you scream and drop the plug on the ground.")
      player_data["health"] -= 40
    elif wire == "white":
      print("Good phone works")

    
#Basement Room End ---------------------------------------------------------------------------
#Inventory Actions
def InventoryActions(player_input):
  global player_data, ShotgunAmmo
  hpRestore = 25
  #Shotgun
  if player_input == "shotgun":
    print("\n--------\nYou take the weapon in your hands and you look over it. So many things you can do with it, what will be one of those things ?")
    print("\n1.Check Ammo \n2. Shoot Locked Door\n3. Take yourself out of a misery")
    ch = int(input("Enter your choice: "))
    #End your sufferings
    if(ch == 3):
      print("\n--------\nYou took stirdy gun in your hands, you take one last look over it, after which you put the ice cold barrel in your mouth, close your eyes, think about last nice things that happened in your life, and with tears in your eyes, you press the trigger.BOOM! Loud shot splash your brains all over the wall")
      player_data["health"] = 0
    #No Locked Doors to shoot
    elif (ch == 2 and player_data["location_name"] != "living_room"):
      print("\n--------\nNo locked doors around")
    #Shoot Locked Door
    elif ch == 2 and player_data["location_name"] == "living_room" and ShotgunAmmo > 0:
      print("\n1. Shoot Garage Door \n2. Shoot Basement Door")
      ch = int(input("Enter your choice: "))
      #Garage Door
      if ch == 1:
        print("\n--------\nYou blasted Garage Door our")
        ShotgunAmmo -= 1
        living_room.keys["garage door"] = "open"
        #Basement Door
      elif ch == 2:
        print("\n--------\nYou blasted Basement Door our")
        ShotgunAmmo -= 1
        living_room.keys["basement door"] = "open"
    #NO AMMO
    elif ch == 2 and player_data["location_name"] == "living_room" and ShotgunAmmo <= 0:
      print("\n--------\nYou attempt to shoot, but shotgun is empty.Find some bullets")
    #Check Ammo
    elif ch == 1:
      print("\n--------\nYou check ammo mag, and find " + str(ShotgunAmmo) + " Shotgun Shells")
  #Medkit
  elif player_input == "medkit":
    if player_data["health"] < 100:
      print("\n--------\nYou take out medkit that you found and you apply first aid to yourself. You gain 25 points of Health")
      player_data["health"] += hpRestore
      inventory.remove("medkit")
      if player_data["health"] >= 100:
        player_data["health"] = 100
    else:
      print("\n--------\nYou are feeling amazing, save your medkit for the future")
  #Knife
  elif player_input == "knife":
    print("\n--------\nYou take bloody knife out and take a look over it.")
    print("\n1. Lock pick the Doorknob\n2. Attack")
    ch = int(input())
    #Choice for knife
    if ch == 1 and player_data["location_name"] == "living_room":
      print("\n--------\nWhich door would you like to open ? 1. Basement door 2. Garage Door")
      ch = int(input())
      #Basement 
      if ch == 1:
        print("\n--------\nYou took out a knife and fiddled with a door knob to unlock it. It took you a few minutes to lockpick it, but you broke the knife in the process.")
        inventory.remove("knife")
        living_room.keys["basement door"] = "open"
      #Garage Door
      elif ch == 2:
        print("\n--------\nYou took out a knife and fiddled with a door knob to unlock it. It took you a few minutes to lockpick it, but you broke the knife in the process.")
        inventory.remove("knife")
        living_room.keys["garage door"] = "open"
    #No Door 
    elif ch == 1 and player_data["location_name"] != "living_room":
      print("\n--------\nNo doors to lockpick!")
    #Attack
    elif ch == 2:
      print("\n--------\nNobody to attack around you")

    


#Start the game 
print("Welcome to Escape the house 3!")

print("Are you ready to start your escape " + name + " ?")
firstChoice = input().lower()
if firstChoice == "no":
  print("Too bad, see you later")
  sys.exit()

#Show players help file at the start so they will know whats going on 
help_file()
#Show start description
room_description = start_room.description
room_text = start_room_text
print(room_description)
def play_game():
  global player_data
  print(room_text)
  print(Fore.RED + "Inventory: " + str(inventory))
  print(str(player_data["health"]) + " Health")
  reset()
  player_input = input("What would you like to do buddy ?\n").lower()
  #Description will print description of the room player is in
  if player_input == "description":
    current_location = player_data["location_desc"]
    print("\n" + str(current_location))
  elif player_input == "help":
    help_file()
  elif player_input == "":
    print("ur okay bruh")
  elif player_input == "shotgun" and player_input in inventory:
    InventoryActions("shotgun")
  elif player_input == "medkit" and player_input in inventory:
    InventoryActions("medkit")
  elif player_input == "knife" and player_input in inventory:
    InventoryActions("knife")
  else:
    #If player use move related to the room
    current_location_name = player_data["location_name"]
    if current_location_name == "start_room":
      start_room_moves_actions(player_input)
    elif current_location_name == "kitchen":
      kitchen_moves_actions(player_input)
    elif current_location_name == "living_room":
      living_room_moves_actions(player_input)
    elif current_location_name == "basement_room":
      basement_room_moves_actions(player_input)

  #Check if the game is over
  if player_data["health"] < 1:
    print(Fore.RED + "HAHAHAHAHA YOU DIED IN TEXT RPG DUDE HOW BAD DO YOU HAVE TO BE")
    reset()
  else:
    play_game()

play_game()

    
  
  
  
  
  
  


