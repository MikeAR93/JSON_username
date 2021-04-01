import json
#variables
filename = 'userName.json'
name = ''
#
try:
    with open(filename,'r') as data:
        name = json.load(data)
except IOError:
    print("First-time login")
if name != "":
    print("Welcome back " + name + "!")
else:
    name = input("Hello! What's your name ")
    print("Welcome " + name + "!")

try:
    with open(filename, 'w') as file:
        json.dump(name, file)
except IOError:
    print("There was a problem writing to the history file.")