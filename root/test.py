import os

def showinstructions():
    #print a main menu and the commands
    print('''
     Zombie Outbreak
    =================
    Actions:
    Go [direction]
    Get [item]
    Get all required items and escape with the helicopter!
''')

def status():
    print("-----------------")
    print(f"currentRoom: {currentRoom}")
    print(f"inventory: {inventory}")
    if "item" in rooms[currentRoom] and rooms[currentRoom]["item"]:
        room_item = rooms[currentRoom]["item"]
        print(f"you see a {room_item}")


    print("-----------------")

inventory = []
rooms = {
        "Zombie pit"  :{
                        "east": "Blue Room",
                        "item": "zombie hoard"
                     },
        "Hallway"   :{
                        "north": "Weapons Vault",
                        "west": "Red room",
                        "item": "blue key"
                     },
        "Red room"  :{
                        "east": "Hallway",
                        "item": "gasoline",
                        "required": "red key"
                     },
        "Blue Room" :{
                        "east": "Bunker",
                        "west": "Zombie pit",
                        "item": "keycard",
                        "required": "blue key"
                     },
        "Attic"     :{
                        "south": "Bunker",
                        "item": "helicopter key"
                     },
        "Laboratory" :{
                        "west": "Undead Forest",
                        "south": "Test chamber",
                        "item": "red key",
                        "required": "keycard"
                     },
        "Helipad"   :{
                        "north": "Undead Forest",
                        "item": "ammo"
                     },
        "Undead Forest":{
                        "south": "Helipad",
                        "west" : "Bunker",
                        "east": "Laboratory",
                        "item": "grenade launcher"
                     },
        "Bunker"    :{
                        "south": "Weapons Vault",
                        "east": "Undead Forest",
                        "north": "Attic",
                        "west": "Blue Room"

                     },
        "Weapons Vault": {
                        "north": "Bunker",
                        "south": "Hallway",
                        "item": "hunting knife"
                        },
        "Test chamber": {
                        "north": "Laboratory",
                        "item": "zombie hoard"
                        },
        }
currentRoom = "Bunker"

showinstructions()

while True:
    status()
    print(f"You are in the {currentRoom}")
    move = input(">")
    move = move.split(" ", 1)

    #move -> ["go", "south"]
    #also adds the function that makes you have to have certain items for access to rooms and the item obtainment code
    os.system("cls")
    showinstructions()
    if move[0] == "go":
        if move[1] in rooms[currentRoom]:
            nextRoom = rooms[currentRoom][move[1]]

            if "required" in rooms[nextRoom]:
                requiredItem = rooms[nextRoom]["required"]

                if requiredItem in inventory:
                    currentRoom = nextRoom
                    print(f"You are now in the {currentRoom}")
                else:
                    print(f"You need the {requiredItem} to enter!")
            else:
                currentRoom = nextRoom
                print(f"You are now in the {currentRoom}")

        else:
            print(f"You cannot go {move[1]}")
    if move[0] == "get":
        if move[1] == rooms[currentRoom]["item"]:
            print(f"you obtained a {move[1]}")
            inventory.append(move[1])
            rooms[currentRoom]["item"] = " "
        else:
            print(f"You already have the {move[1]}")

    #victory condition 1: escaping the forest and surviving the hoard
    if "hunting knife" in inventory and "ammo" in inventory and "grenade launcher" in inventory and "gasoline" in inventory and "helicopter key" in inventory and currentRoom == "Helipad":
        print("you took the helicopter and escaped the Zombie Hoard, for now....")
        print("VICTORY!!!!!")
        break
    #loss condition: getting eaten by the hoard
    if "item" in rooms[currentRoom] and rooms[currentRoom]["item"] == "zombie hoard":
        print("You were ambushed by the zombie hoard and were eaten")
        print("GAME OVER")
        print("  _____")
        print(" /      \ ")
        print("| () () |")
        print(" \  ^  /")
        print("  |||||")
        print("  |||||")
        break