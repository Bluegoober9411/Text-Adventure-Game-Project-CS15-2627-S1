import os
import random
def showinstructions():
    #print a main menu and the commands
    print('''
     Zombie Outbreak
    =================
    Actions:
    Go [direction]
    Get [item]
    Get all required items and escape with the helicopter!
    But be careful, the hoard has taken over one of three rooms...
''')

def status():
    print("-----------------")
    print(f"currentRoom: {currentRoom}")
    print(f"inventory: {inventory}")
    room_items = rooms[currentRoom]["items"]
    if room_items:
        print("You see:")
        for item in room_items:
            print(f" - {item}")
    print("-----------------")

inventory = []
rooms = {
        "Garage"  :{
                        "east": "Blue Room",
                     },
        "Hallway"   :{
                        "north": "Weapons Vault",
                        "west": "Red room",
                     },
        "Red room"  :{
                        "east": "Hallway",
                        "item": "gasoline",
                        "required": "red key"
                     },
        "Blue Room" :{
                        "east": "Bunker",
                        "west": "Garage",
                        "required": "blue key"
                     },
        "Attic"     :{
                        "south": "Bunker",
                     },
        "Laboratory" :{
                        "west": "Undead Forest",
                        "south": "Test chamber",
                        "required": "keycard"
                     },
        "Helipad"   :{
                        "north": "Undead Forest",
                     },
        "Undead Forest":{
                        "south": "Helipad",
                        "west" : "Bunker",
                        "east": "Laboratory",
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
                        },
        "Test chamber": {
                        "north": "Laboratory",
                        },
        }
locked_rooms = {
    room for room in rooms
    if "required" in rooms[room]
}
locked_rooms.add("Helipad")
unlocked_rooms = set(rooms.keys()) - locked_rooms
def spawn_items():
    for room in rooms:
        rooms[room]["items"] = []
    hoard_rooms = ["Garage", "Test chamber", "Attic"]
    selected_hoard_rooms = random.sample(hoard_rooms, 1)
    for room in selected_hoard_rooms:
        rooms[room]["items"].append("zombie hoard")
    safe_rooms = [
        room for room in rooms
        if room not in selected_hoard_rooms
    ]
    blue_key_rooms = [
        room for room in safe_rooms
        if room in [
            "Bunker",
            "Weapons Vault",
            "Hallway",
            "Undead Forest"
        ]
    ]
    keycard_rooms = [
        room for room in safe_rooms
        if room in [
            "Bunker",
            "Weapons Vault",
            "Hallway",
            "Undead Forest",
            "Blue Room",
            "Garage"
        ]
    ]
    red_key_rooms = [
        room for room in safe_rooms
        if room in [
            "Bunker",
            "Weapons Vault",
            "Hallway",
            "Undead Forest",
            "Blue Room",
            "Garage",
            "Laboratory",
            "Helipad",
            "Test chamber"
        ]
    ]
    rooms[random.choice(blue_key_rooms)]["items"].append("blue key")
    rooms[random.choice(keycard_rooms)]["items"].append("keycard")
    rooms[random.choice(red_key_rooms)]["items"].append("red key")
    remaining_items = [
        "gasoline",
        "ammo",
        "grenade launcher",
        "hunting knife"
    ]
    for item in remaining_items:
        room = random.choice(safe_rooms)
        rooms[room]["items"].append(item)
        rooms["Helipad"]["items"] = [
            item for item in rooms["Helipad"]["items"]
            if item != "helicopter key"
        ]

        rooms["Helipad"]["items"].append("helicopter key")
spawn_items()
currentRoom = "Bunker"

showinstructions()

while True:
    status()
    print(f"You are in the {currentRoom}")
    move = input(">")
    move = move.split(" ", 1)

    #move -> ["go", "south"]
    # also adds the function that makes you have to have certain items for access to rooms and the item obtainment code
    os.system("cls")
    showinstructions()
    if move[0] == "go":
        if len(move) < 2:
            print("Go where?")
        elif move[1] in rooms[currentRoom]:
            nextRoom = rooms[currentRoom][move[1]]

            if nextRoom not in unlocked_rooms:

                # Puzzle guarding the Helipad
                if nextRoom == "Helipad":
                    print("A keypad blocks the Helipad!")
                    print("Solve this puzzle to unlock it:")
                    print("What is 7 + 5 * 2?")

                    answer = input("> ").strip()

                    if answer == "17":
                        print("Correct! The Helipad is unlocked!")
                        unlocked_rooms.add("Helipad")
                        currentRoom = nextRoom
                    else:
                        print("Incorrect! The Helipad remains locked.")

                # Key-locked rooms
                else:
                    requiredItem = rooms[nextRoom]["required"]

                    if requiredItem in inventory:
                        inventory.remove(requiredItem)
                        unlocked_rooms.add(nextRoom)
                        currentRoom = nextRoom

                        print(f"You used the {requiredItem}!")
                        print(f"{nextRoom} is now permanently unlocked.")
                    else:
                        print(f"You need the {requiredItem} to enter!")

            else:
                currentRoom = nextRoom
                print(f"You are now in the {currentRoom}")

        else:
            print(f"You cannot go {move[1]}")

    if move[0] == "get":
        item = move[1]

        if item in rooms[currentRoom]["items"]:
            print(f"You obtained a {item}!")
            inventory.append(item)
            rooms[currentRoom]["items"].remove(item)
        else:
            print(f"There is no {item} in this room.")

    #victory condition 1: escaping the forest and surviving the hoard
    if "hunting knife" in inventory and "ammo" in inventory and "grenade launcher" in inventory and "gasoline" in inventory and "helicopter key" in inventory and currentRoom == "Helipad":
        print("you took the helicopter and escaped the Zombie Hoard, for now....")
        print("VICTORY!!!!!")
        break
    #loss condition: getting eaten by the hoard
    if "zombie hoard" in rooms[currentRoom]["items"]:
        print("You were ambushed by the zombie hoard and were eaten")
        print("GAME OVER")
        print("  _____")
        print(" /      \ ")
        print("| () () |")
        print(" \  ^  /")
        print("  |||||")
        print("  |||||")
        break


