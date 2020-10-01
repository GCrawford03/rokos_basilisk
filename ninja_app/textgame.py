directions = ['north','south','east','west']

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.linkedLocations = {}

    def addLink(self, direction, destination):
        if direction not in directions:
            raise ValueError('Invalid direction')
        elif destination not in locations:
            raise ValueError('Invalid destination')
        else:
            self.linkedLocations[direction] = destination

locations = { 'woods':Location('The woods.', 'You are in the woods'),
              'lake':Location('The lake.', 'You are by the lake') }
            #   other directions

locations['woods'].addLink('north','lake')
locations['lake'].addLink('south','woods')
# other locations
# location [request.session {place}]

# models.py log box. Checks with database input. Better in models.py or textgame.py? Handle directions of textgame

currentLocation = locations['woods']
# store in session

# def game(request):
# yes_no = ["yes", "no"]
# directions = ["west", "east", "north", "south"]

# name = input("What is your name?\n")
# print("Greetings, " + name + ". Let us go on a quest!")
# print("You find yourself on the edge of a dark forest.")
# print("Can you find your way through?\n")

# response = ""
# while response not in yes_no:
#     response = input("Would you like to step into the forest?\nyes/no\n")
#     if response == "yes":
#         print("You head into the forest. You hear crows cawwing in the distance.\n")
#     elif response == "no":
#         print("You are not ready for this quest. Goodbye, " + name + ".")
#         quit()
#     else: 
#         print("I didn't understand that.\n")


# while True:
#     # print(currentLocation.description)
#     for linkDirection,linkedLocation in currentLocation.linkedLocations.items():
#         print(linkDirection + ': ' + locations[linkedLocation].name)
#     command = input('>').lower()
#     if command in directions:
#         if command not in currentLocation.linkedLocations:
#             print('You cannot go that way')
#         else:
#             newLocationID = currentLocation.linkedLocations[command]
#             currentLocation = locations[newLocationID]
#     else:
#         print('Try one of: ' + ', '.join(directions))

# class Location:
#     def __init__(self):
#         self.west = None
#         self.east = None
#         self.south = None
#         self.north = None
#         self.enemy = []

# home = Location()
# forest = Location()
# river = Location()

# home.west = forest
# lab.north = river