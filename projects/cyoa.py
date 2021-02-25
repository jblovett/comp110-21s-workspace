__author__ = """730155204"""

import random
int: points
str: name

def main() -> None:
    bool: playing = True
    global points
    points = 33
    while playing:
        name = greet()
        printf("Ground control to major {name}, commencing countdown, engines on!")
        printf("Major {name}, we have a problem! Our guidance systmes are down and we don't know which direction gets you to mars!")
        print("However, Mars Control can ping your distance every 28 minutes. You'll have to guess which direction and hope it's right.")
        print("Or, we can guide you to a wormwhole. I wonder where it leads!")
        str: choice = input("Type <wormwhole> to set course for the great unknown! Type <mars> to set a random course for the read planet. Type <end> to stop playing.")
        if choice == "wormwhole":
            int: result = wormwhole(points)
            if result == -1:
                playing = False
            elif result == 0:
                print("You've died from spagettification!")
                playing = False
            else:
                points = result
                mission_to_mars()

            
        elif choice == "end":
            playing = False
        elif choice == "mars":
            mission_to_mars()




def greet() -> str:
    print("Begin your space oddesey and take the 33 million mile journey to Mars!")
    str: name = input("What's your name?")
    return name

def wormwhole(points: int) -> int:
    print("After months of drifting, you peer through the window and see a gaping whole in the starscape.")
    print("Light shifts and bends around the void. Your space ship begins to drift towards it. Could this actually be a black whole?")
    print("Type <end> to go back to Earth and stop playing.")
    print("Type <orbit> to begin circling the blackness. For physics reasons perhaps?")
    str: choice = input("Type <straight> to fly straight in. What could go wrong?")
    if choice == "end":
        return -1
    elif choice == "straight":
        return 0
    elif choice == "orbit":
        print("You begin circling the black whole. Its gravity pulls you closer, and you increase thrust to maximum capacity.")
        print("The metal around your spaceship rings and jolts.")
        print("It's so fast! Light streatches and becomes imperceptible. Suddenly, all is black.")
        print("...")
        print("Suddenly, starlight returns! Among the stars, the red light of mars glimmers.")
        int: chance = random.randint(1, 3)
        if chance == 1:
            points = points - 15
            return points
        elif chance == 2:
            points = points - 25
            return points
        elif chance == 3:
            points = points - 5
            return points



    
    