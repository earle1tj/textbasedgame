#Taylon Earle


#A dictionary for the simplified dragon text game
#The dictionary links a room to other rooms.
rooms = {
        'Secret Room': {'south': 'Dining Room', 'east': 'Library', 'item': 'net'},
        'Library': {'west': 'Secret Room', 'south': 'Hallway', 'east': 'Basement', 'item': 'flashlight'},
        'Basement': {'west': 'Library', 'item': 'rope'},
        'Hallway': {'west': 'Dining Room', 'south': 'Foyer', 'east': 'Bedroom', 'north':"Library", 'item': 'nothing'},
        'Bedroom': {'west': 'Hallway', 'item': 'sheet'},
        'Foyer': {'east': 'Living Room', 'north': 'Hallway', 'west': 'Kitchen', 'item': 'camera'},
        'Living Room': {'west': 'Foyer', 'item': "nothing"},
        'Kitchen': {'east': 'Foyer', 'north': 'Dining Room', 'item':'snacks'},
        'Dining Room': {'east': 'Hallway', 'north': 'Secret Room', 'south': 'Kitchen', 'item': 'ghost'},
    }

# this is the games state while running
gameStart = True



# this defines how the plyer will move
def move(player, direction):
    global rooms
    current_room = player

    # this checks if there is the direction in that room
    if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]

    # error handling
    else:
        print("You are not going in a good direction!")
        print("----------------")
        return player  # Were going to go back into the room if theres nothing but all

    # this returns where we currenlty are
    return current_room

# this is the rules to follow
def theRules():
    print( "\n Move commands: go South, go North, go East, go West.")
    print("\n To get an item. Say get and the item. For example get ghost")

#this is the game's meat and bones
def gameStart():
    print("Welcome to Ghost Mayhem!")
    print("\n Oh no! During dinner in the dining room a ghost appeared! \n The ghost spooked everybody but you have an idea for a trap. \n Pull together 6 items hidden around the manor to capture the ghost")
    theRules()
    inventory = []
    player = "Hallway"  # Acc. to me player should be a str not  tuple
    while gameStart:
        current_room = player
        if current_room == "exit":
            print("You want to quit? Fineeeee")
            print("----------------")
            break
        if current_room == 'Dining Room':
            if len(inventory) == 6:
                print("\nYou have solved the mystery! Your friends were trying to steal the treasure hidden in the table of the dining room!")
                break
            else:
                print("\nWell, your trap broke! You forgot some supplies.")
                print("\nI guess you will never get to the bottom of this mystery")
                break
        # this reoccurs everytime it loops again
        print("\nYou are located in the", current_room)
        print('\nInventory:', inventory)
        room_dict = rooms[current_room]
        if 'item' in room_dict:
            item = room_dict["item"]
            if item not in inventory:
                print("You see", item)

        # input validation and parsing
        print("----------------")
        player_move = input("So like where do you want to go:\n").lower()

        # this is validating if the player is moving or
        if 'go' in player_move or 'move' in player_move:

            #this splits the string to be able to determine what the player is doing
            action = player_move.split(' ')
            print("You want to", *action)  # displaying what the player wants to do

            #this sets up the go portion
            if action[0] == 'go' or 'move':
                player = move(player, action[1])  # Assigning the value to player

            else:
                print("I'm having trouble understanding")
            # invalid action

        #Validating if a player wants to get something
        elif 'get' in player_move:
            action = player_move.split(' ')
            if action[1] in inventory:
                print('You already have that item!')

             #get item and nothing are put before the actual items just incase to prevent an error
            elif action[1] == 'nothing':
                print('You cant get nothing!')

            elif action[1] == 'item':
                print('Say literally anything but item')

            #this gets the actual item
            elif action[1] == item:
                inventory.append(item)
                print(item, 'collected')

            else:
                print("What do you want me to get?")

        #giving player two different ways to quit
        elif 'exit' in player_move or 'quit' in player_move:
            player = 'exit'

        else:
            print('I think you need to reword that friend.')
            print("----------------")
            continue

#this is what starts the game
gameStart()

#This is what is played after the game ends
print("Thanks for playing!")
print("----------------")