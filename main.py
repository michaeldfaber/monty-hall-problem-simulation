import random

games = 1000
switchWins = 0
switchLosses = 0
noSwitchWins = 0
noSwitchLosses = 0

def playSwitchGames():
    global switchWins
    global switchLosses
    switchGames = games

    while (switchGames > 0):
        doors = getDoors()
        chosen = random.randint(0,2)
        openedDoor = openDoor(chosen, doors)
        switchedDoor = -1

        if (chosen == 0):
            if (openedDoor == 1):
                switchedDoor = 2
            if (openedDoor == 2):
                switchedDoor = 1
        
        if (chosen == 1):
            if (openedDoor == 0):
                switchedDoor = 2
            if (openedDoor == 2):
                switchedDoor = 0
        
        if (chosen == 2):
            if (openedDoor == 0):
                switchedDoor = 1
            if (openedDoor == 1):
                switchedDoor = 0

        if (doors[switchedDoor]):
            switchWins = switchWins + 1
        else:
            switchLosses = switchLosses + 1
        
        switchGames = switchGames - 1

def playNoSwitchGames():
    global noSwitchWins
    global noSwitchLosses
    noSwitchGames = games

    while (noSwitchGames > 0):
        doors = getDoors()
        chosen = random.randint(0,2)

        if (doors[chosen]):
            noSwitchWins = noSwitchWins + 1
        else:
            noSwitchLosses = noSwitchLosses + 1

        noSwitchGames = noSwitchGames - 1

def getDoors():
    doors = [False, False, False]
    winner = random.randint(0,2)
    doors[winner] = True
    return doors

def openDoor(chosen, doors):
    i = 0
    for door in doors:
        if door == False and i != chosen:
            return i
        else:
            i = i+1

def printResults():
    global games
    global noSwitchGames
    global noSwitchWins
    global noSwitchLosses

    print(str(games) + " games were 'played' where the switch door option WAS chosen:\n")
    print(str(switchWins) + " games were won")
    print(str(switchLosses) + " games were lost\n")

    print(str(games) + " games were 'played' where the switch door option WAS NOT chosen:\n")
    print(str(noSwitchWins) + " games were won")
    print(str(noSwitchLosses) + " games were lost\n")

def playGames():
    playSwitchGames()
    playNoSwitchGames()
    printResults()

playGames()