from room import Room
from flashlight import Flashlight
from character import Enemy
from container import Container

heldItems = []
myHealth = 95
visitedRooms = []

# ********************************* SET UP THE ROOMS *********************************

# Kitchen
#
# Room descriptions should include interactive containers like CABINET, BIN, DESK, SHELF, SHOEBOX that contain/hide other interactive items
Gym = Room("Gym","A big, empty, dark room with a bunch of boxes everywhere. On the floor there is a KNIFE and a FIRST AID")

# The kitchen has a CUPBOARD object that contains/hides 3 interactive items, a sponge, a plate, a can of soup
# Once this container is open, the interactive items will no longer be hidden in the container
Gym.box = Container("box right next to you",["basketball","shoe","tennis ball"])
# The kitchen has a CABINET object that contains/hides 2 interactive items, a knife and a twinkie
# Once this container is open, the interactive items will no longer be hidden in the container
Gym.box2 = Container("a closed, shiny box near the gym door",["Diary of A Wimpy Kid book","baseball helmet"])

# Create an interactive item that's show in a room (not hidden in a container) with create_room_item()
Gym.create_room_item("knife")
Gym.create_room_item("first aid")

# Classroom
#
classroom = Room("Classroom","A dark room with rows of desks and posters on the walls. There are items on some of the desks and a BOX in the corner of the room. You can READ a poster. You can Take at the items on the DESKS. There is a red flashlight near the door.")
classroom.desk = Container("desks",["scissors","notebook paper"])
classroom.box = Container("box",["sheet of bubble wrap","notebooks","markers"])
classroom.create_room_item("Scissors")
redFlashlight = Flashlight("red",0,False)

# Laboratory
#
aud = Room("Auditorium","A huge room that has very little lighting. You can hear the echos of mice running, and the support beams creaking. There is a CHEST behind stage that looks like it would have some clothing in it.")
# The lab has a SHELF object that contains 3 interactive items. Shelf gets a third argument because you'd say ON the shelf, not IN the shelf
aud.chest = Container("In the chest you see a ROBIN HOOD COSTUME, a BOW, and some ARROWS.",["Robinhood Costume","Long Bow","quiver with arrows"],"in ")
aud.create_room_item("Cars Flashlight")
carsFlashlight = Flashlight("Cars",1,True)

# Janitor Closet
#
janitorcloset = Room("Janitor Closet","A small dark room with a musty smell. On one side is a filing CABINET and a large plastic BIN. On the other side is a SHELF with supplies and a SHOEBOX.")
janitorcloset.cabinet = Container("cabinet",["holy water","bible"])
janitorcloset.shelf = Container("shelf",["shank"])
# Create a fake room called locked that represents all permenently locked doors
#
locked = Room("locked","")

# Connect rooms. These are one-way connections.

Gym.link_room(locked, "EAST")
Gym.link_room(smalloffice, "SOUTH")
Gym.link_room(locked, "WEST")
janitorcloset.link_room(smalloffice, "EAST")
classroom.link_room(kitchen, "NORTH")
classroom.link_room(aud, "EAST")
classroom.link_room(locked, "SOUTH")
classroom.link_room(supplycloset, "WEST")
aud.link_room(locked, "SOUTH")
aud.link_room(classroom, "WEST")
current_room = Gym




# Set up characters
ojsimpson = Enemy("OJ Simpson", "A big man, who committed multiple murders. He is a prisoner in the school and his way out is killing you.")
ojsimpson.set_speech("Absolutely, 100 percent not guilty.")
ojsimpson.set_weaknesses(["Diary of a Wimpy Kid Book","knife","Sulfuric Acid"])
#classroom.set_character(ojsimpson)

# This is a procedure that simply prints the items the player is holding and tells them if they can do something with that item
def playerItems():
    # Print out the player's Held Items and let player know if they can USE an item to fight a character or something
    if len(heldItems) == 1:
        print("You are holding a "+heldItems[0])
        print("You can DROP "+heldItems[0].upper())
        if current_room.character is not None:
            print("You can USE "+heldItems[0].upper()+" to fight "+current_room.character.name)
    elif len(heldItems) >= 2:
        print("Your hands are full. You must drop something before you can pick anything else up.")
        print("You are holding a "+heldItems[0]+" and a "+heldItems[1])
        print("You can DROP "+heldItems[0].upper()+" or DROP "+heldItems[1].upper())
        if current_room.character is not None:
            print("You can USE "+heldItems[0].upper()+" to fight "+current_room.character.name+" or USE "+heldItems[1].upper())
    # ********************************* SPECIAL ITEM INTERFACES *********************************
    # If holding a special item, then display the item's interface with get_interface()
    if "red flashlight" in heldItems:
        redFlashlight.get_interface(heldItems,current_room)
    if "yellow flashlight" in heldItems:
        yellowFlashlight.get_interface(heldItems,current_room)

# This fuction checks the player's command and then runs the corresponding method
def checkUserInput(current_room,command,heldItems):
    # Convert it to ALL CAPS
    command = command.upper()
    # All possible user input commands go here
    print("\n")
    
    # ********************************* SPECIAL USER INPUT *********************************
    # If holding a special item, then check for that item's UI keywords with check_input()
    if "red flashlight" in heldItems and "RED FLASHLIGHT" in command:
        redFlashlight.check_input(command,heldItems,current_room)
    elif "yellow flashlight" in heldItems and "YELLOW FLASHLIGHT" in command:
        yellowFlashlight.check_input(command,heldItems,current_room)

    # ********************************* USE, TAKE, DROP *********************************
    # Use an item to fight an enemy
    elif "USE " in command and current_room.get_character() is not None:
        # command[4:] is used to get the characters typed after "USE "
        enemyHealth = current_room.character.fight(command[4:])
        if enemyHealth < 1:
            print(current_room.character.name+" is dead")
            current_room.remove_character() # If the enemy is dead, then remove them from the room
    # Take lets you pick up an item
    elif "TAKE " in command:
        # command[5:] is used to get the characters typed after "TAKE "
        heldItems = current_room.take_room_item(command[5:],heldItems)
    # Drop lets you set down an item
    elif "DROP " in command:
        # command[5:] is used to get the characters typed after "DROP "
        heldItems = current_room.add_room_item(command[5:],heldItems)
    # Talk and Fight aren't currently used in this version of the game, but could be implemented in your version of the game
    elif "TALK" in command and current_room.get_character() is not None:
        current_room.character.talk()
    elif "FIGHT" in command and current_room.get_character() is not None:
        current_room.character.talk()
    
    # ********************************* ROOM SPECIFIC USER INPUTS *********************************
    # Interactive containers look like this...   elif current_room.name == "Laboratory" and command == "SHELF"
    elif current_room.name == "Gym" and command == "BOX":
        # Open kitchen.cupboard and concat each of the contents to the end of room_items
        current_room.room_items += Gym.box.open()
    # Can only open cabinet if holding a flashlight that isOn
    elif current_room.name == "Gym" and command == "BOX" and ("knife" in heldItems):
        # Open kitchen.cabinet and concat each of the contents to the end of room_items
        print("You use knife to open up box.")
        current_room.room_items += Gym.box2.open()
    elif current_room.name == "Gym" and command == "SHINY BOX":
        print("You check the cabinet, but it's too dark to see if there is anything inside.")
<<<<<<< HEAD
    elif current_room.name == "Classroom" and command == "Box":
        # Open classroom.desk and concat each of the contents to the end of room_items
        current_room.room_items += classroom.package.open()
    elif current_room.name == "Classroom" and command == "READ":
        print("It is about a field trip from 10 years ago.")
    elif current_room.name == "Classroom" and command == "DESKS" and "Scissors" in heldItems:
        # Open classroom.desk and concat each of the contents to the end of room_items
        current_room.room_items += classroom.desk.open()
=======
    elif current_room.name == "Small Office" and command == "PACKAGE":
        # Open smalloffice.desk and concat each of the contents to the end of room_items
        current_room.room_items += smalloffice.package.open()
    elif current_room.name == "Small Office" and command == "READ":
        print("POCCNR??? You can't read it. It's written is some strange Cyrillic script.")
    elif current_room.name == "Small Office" and command == "DESK" and "brass key" in heldItems:
        # Open smalloffice.desk and concat each of the contents to the end of room_items
        print("You use the brass key to unlock the desk.")
        current_room.room_items += smalloffice.desk.open()
    elif current_room.name == "Small Office" and command == "DESK":
        print("The desk drawer is locked.")
    elif current_room.name == "Janitor Closet" and command == "SHELF":
        # Open lab.shelf and concat each of the contents to the end of room_items
        current_room.room_items += janitorcloset.shelf.open()
    elif current_room.name == "Janitor Closet" and command == "CABINET":
        # Open lab.shelf and concat each of the contents to the end of room_items
<<<<<<< HEAD
        current_room.room_items += aud.chest.open()
>>>>>>> cca23ae0903a9f81da87007d9874fd234c4662a2
=======
        current_room.room_items += janitorcloset.cabinet.open()
>>>>>>> 1774cf6415c6004e32c6523b0fb3a2d52348a39e
    elif current_room.name == "Auditorium" and command == "CHEST":
        # Open lab.shelf and concat each of the contents to the end of room_items
        current_room.room_items += aud.chest.open()

    # ********************************* MOVE *********************************
    else:
        current_room = current_room.move(command,visitedRooms) # If it was none of those commands, assume it was a direction. Try to move.
    return current_room


#THE LOOP
while True:
    print("\n")
    # Print current room info
    myHealth = current_room.info(heldItems,myHealth,visitedRooms) # this returns myHealth cuz an enemy in the room could hurt you
    if myHealth <= 0:
        print("You died.\nGAME OVER")
        break
    # Print player items
    playerItems()
    # Get user input
    command = input("> ")
    # Check the user input
    current_room = checkUserInput(current_room,command,heldItems)
