import random
import time

enemies = ['The evil wich', 'the wicked fairie', 'the monster',
           'The giant gorilla', 'the dragon']
weapons = ['dagger', 'small knife', 'stick']




current_enemy = random.choice(enemies)
weapon = random.choice(weapons)
power_level = 3
have_Sword = True


def mean():
    player_name = input("Input your name:\n ")
    print_and_sleep(f"Welcome in my game {player_name}", 1)
    start()
    decision()


def print_and_sleep(msg, waiting):
    print(msg)
    time.sleep(waiting)


def start():
    print_and_sleep("You find yourself standing in an open field, filled with"
                    " grass and yellow wildflowers.", 2)
    print_and_sleep(f"Rumor has it that  {current_enemy} is somewhere around "
                    "here, and has been terrifying the nearby village.", 2)
    print_and_sleep("In front of you is a house.", 2)
    print_and_sleep("To your right is a dark cave.", 2)
    print_and_sleep(f"In your hand you hold your trusty (but not very "
                    f"effective) {weapon}.", 2)
    

def sleep():
    global power_level
    power_level -= 1
    print_and_sleep("", 1)
    print_and_sleep(f"your bower level is {power_level} ", 1)
    print_and_sleep("1 hour left", 1)
    print_and_sleep("2 hour left", 1)
    print_and_sleep("3 hour left", 1)
    print_and_sleep("wake up now ...", 1)
    if power_level == 0:
        print_and_sleep("You sleep more your power is 0 .. you lose ...\n", 2)
        play_again()
    else:
        decision()
        
        
def House_of_horrors():
    print_and_sleep("You approach the door of the house.", 2)
    print_and_sleep(f"You are about to knock when the door opens and out "
                    f"steps {current_enemy}.", 2)
    print_and_sleep(f"Eep! This is  {current_enemy}'s house!", 2)
    Battle_or_escape(weapon)

    
def cave():
    global have_Sword
    global weapon
    print_and_sleep("You peer cautiously into the cave.", 2)
    if have_Sword:
        print_and_sleep("It turns out to be only a very small cave.", 2)
        print_and_sleep("Your eye catches a glint of metal behind a rock.", 2)
        print_and_sleep("You have found the magical Sword of Ogoroth!", 2)
        print_and_sleep(f"You discard your silly old {weapon} and take "
                        "the sword with you.", 2)
        weapon = "sword"
    elif not have_Sword:
        print_and_sleep("You've been here before, and gotten all the good "
                        "stuff. It's just an empty cave now.", 2)
    have_Sword = False
    print_and_sleep("You walk back out to the field.", 2)
    decision()


def Battle_or_escape(c_weapon):
    global weapon
    print_and_sleep(f"The {current_enemy} attacks you!", 2)
    if c_weapon in ['dagger', 'small knife', 'a stick']:
        print_and_sleep(f"You feel a bit under-prepared for this, what with "
                        f"only having a tiny {c_weapon} .", 2)
    opinion = ''
    while opinion not in ['1', '2']:
        opinion = input("Would you like to (1) fight or (2) run away?\n")

    if opinion == '1':
        if c_weapon in weapons:
            print_and_sleep(f"You do your best...", 1)
            print_and_sleep(f"but your {weapon} is no match for the"
                            f" {current_enemy}.", 2)
            print_and_sleep(f"You have been defeated!", 2)
            play_again()
        elif c_weapon == "sword":
            print_and_sleep(f"As the {current_enemy} moves to attack, you"
                            " unsheath your new sword.", 2)
            print_and_sleep(f"The Sword of Ogoroth shines brightly in your"
                            " hand as you brace yourself for the attack.", 2)
            print_and_sleep(f"But the {current_enemy} takes one look at your"
                            " shiny new toy and runs away!", 2)
            print_and_sleep(f"You have rid the town of the {current_enemy}."
                            " You are victorious!\n", 2)
            weapon = random.choice(weapons)
            play_again()
        else:
            print("error here")

    elif opinion == '2':
        print_and_sleep("You run back into the field. Luckily, you don't seem"
                        " to have been followed.", 2)
        decision()


def decision():
    print_and_sleep("", 1)
    print_and_sleep("Enter 1 to knock on the door of the house.", 2)
    print_and_sleep("Enter 2 to peer into the cave.", 2)
    print_and_sleep("Enter 3 to sleep a while.", 2)
    print_and_sleep("What would you like to do?", 0)
    choice = ''
    while choice not in ['1', '2', "3"]:
        choice = input("(Please enter 1 or 2 or 3.)\n")

    if choice == '1':
        House_of_horrors()
    elif choice == '2':
        cave()
    elif choice == '3':
        sleep()


mean()
