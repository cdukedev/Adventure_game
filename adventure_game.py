import time
import random
items = []
places = []
enemy = []
#Begin Field Scenes
def fSceneOne():
    print_pause("You were attacked, but luckily you are not wounded badly.")
    print_pause("I suggest taking a break to be able to fight another day.")
    explore()
def fSceneTwo():
    print_pause("You faught valiently and persued the Queen to it's lair,")
    print_pause("and using your ingenuity closed it off leaving 20 pounds of dynamite with Cucaracha.")
    victory()
def fSceneThree():
    print("Unfortunately, you have yet to find the Queen. Continue on my friend")
    explore()
def fSceneFour():
    print("You have been Bitten!")
    bugBite()
def fSceneFive():
    print("You have been Bitten!")
    bugBite()
def fieldScenes():
    options = random.choice(sceneList)
    sceneList.remove(options)
    options()
#End field scenes
def intro():
    print_pause("Welcome to your Incredible Journey. From here you will")
    print_pause("come accross many challeges and face your deepest fears.")
    print_pause("Will you cower away from the posibility of failure or do you persist through to find")
    print_pause("the deeper meaning of your Journey?")
    print_pause("You will have one last opportunity to turn back. If you do you may")
    print_pause("never know your true potential. If you continue forward you have the")
    print_pause("potential to fulfill your life's destiny.")
    print_pause("")
    print_pause("Now your journey will begin in Iowa. Surrounded by thousands of miles of corn.")
    farm_land()

def farm_land():
    #first time in farm_land
    if "bugFirst" not in enemy:
        print_pause("No one has been able to slay the Giant Cucaracha Queen that threatens our farms")
        print_pause("We need your help to take the beast down.")
        enemy.append("bugFirst")
        explore()
    #if you have bitten
    elif "bugBite" in places:
        print_pause("Thank God you are alright.")
        print_pause("You were saved by a flock of crows, who swarmed the beast and chased him away.")
        explore()
def explore():
    while True:
        response = input("Now where do you want to go? The Barn, the field, or the quick stop.\nWhat is your desired destination? :" ).lower()
        if "barn" in response:
            barn()
        elif "quick" in response or "stop" in response:
            quickStop()
        elif "field" in response:
            fieldScenes()
        else:
            print_pause("Sorry I did not understand. Please repeat again where you would like to go.")

def bugBite():
    if "med" in items:
        print_pause("Luckily while at the quick stop, you picked up meds to")
        print_pause("heal you from the Queens bite.")
        items.remove("med")
    elif "bugBite" not in places:
        print_pause("Ok, things are getting a little crazy!\n")
        print_pause("I am sure this is not where you indended to go.\n")
        print_pause("Now you seem to be moving through a dense web\n ")
        print_pause("which moves between reality and perception. Based on\n")
        print_pause("this cognitive dissonace that we relate all our\n")
        print_pause("lifes experiences to. Minimizing the mental impact\n")
        print_pause("we have over our own conciousness. Therefore leading\n")
        print_pause("to an inability to function any further. The harder you\n")
        print_pause("try the deeper you fall. A clear reminder of the importance of clarity\n")
        print_pause("We have reached the point of no return!\n")
        print_pause(" ")
        print_pause(" ")
        places.append("bugBite")
        farm_land()
    elif "bugBite" in places:
        print_pause("The town had high hopes in your impressive resume.")
        print_pause("But this time you were not able to stand up to the Great Cucaracha Queen.")
        print_pause("It is wise to not over estimate your skills, but also do not feel defeated.")
        print_pause("You will have another day")
        print_pause(" ")
        print_pause(" ")
        print_pause(" ")
        print_pause(" ")
        startOver()
def victory():
    print_pause("This day has been long awaited by all of the town folk.")
    print_pause("Today we celebrate you for saving our fields, our buisnesses, and our communities!")
    print_pause("Although we know there will always be more cities to save. Today you can breath in and")
    print_pause("know. That you made a difference.")
    again()
def barn():
    if "barnhouse" not in places:
        print_pause("The town is so thankful for your service that they have set you up")
        print_pause("with 5 star accomodations. You are now rested and have conserved")
        print_pause("your energy for the battle of your life.")
        places.append("barnhouse")
        explore()
    else:
        print_pause("The folks of the town are getting impatient, and are starting to think")
        print_pause("that you are getting cold feet. Are you ready or not?! Let's take Queen Cuca down!!!")
        print_pause("Feeling rushed you go out to the fields to search for her.")
        fieldScenes()
def quickStop():
    if "break" not in places:
        print_pause("We were able to load up on all the goods we need.")
        print_pause("To sustain our energy for the next couple of days.")
        items.append("med")
        places.append("break")
        explore()
    else:
        print_pause("On your way you see movement in the corn fields. This is our moment! You start to pursue the Queen!")
        fieldScenes()
def again():
    while True:
        response = input("Would you like to play again?? Please enter Yes or No:" ).lower()
        if "yes" in response:
            startOver()
        elif "no" in response:
            exit()
        else:
            print_pause("I apologize, we did not understand your selection. Please type again Yes or No.")
def startOver():
    items.clear()
    places.clear()
    enemy.clear()
    for i in range(4):
        sceneList = [fSceneOne, fSceneTwo, fSceneThree, fSceneFour, fSceneFive]
        sceneList.append(i)
    intro()
def print_pause(fname):
    print(fname)
    time.sleep(0)
sceneList = [fSceneOne, fSceneTwo, fSceneThree, fSceneFour, fSceneFive]
intro()
