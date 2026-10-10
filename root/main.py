import os

def showinstructions():
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Actions:
    Go [direction]
    Get [item]
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
                        "east": "Red room",
                        "item": "blue key"
                     },
        "Red room"  :{
                        "west": "Hallway",
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
                        }
        }
currentRoom = "Bunker"

showinstructions()

while True:
    status()
    print(f"You are in the {currentRoom}")
    move = input(">")
    move = move.split(" ", 1)

    #move -> ["go", "south"]

    os.system("cls")
    if move[0] == "go":
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
            print(f"you are now in the {currentRoom}")
        else:
            print(f"you cannot go {move[1]}")
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
        break
    #loss condition: getting eaten by the hoard
    if "item" in rooms[currentRoom] and rooms[currentRoom]["item"] == "zombie hoard":
        print("You succumbed to the hoard and were eaten")
        print("GAME OVER")
        print("  _____")
        print(" /      \ ")
        print("| () () |")
        print(" \  ^  /")
        print("  |||||")
        print("  |||||")
        break


