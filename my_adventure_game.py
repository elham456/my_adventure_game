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
