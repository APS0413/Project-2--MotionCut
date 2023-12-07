import time
import random

def introduction():
    print("Welcome to the Text-Based Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious land full of challenges and adventures.")
    time.sleep(1)
    print("Your decisions will shape your destiny. Choose wisely!")

def make_choice(choices):
    print("\nChoose your action:")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def chapter_one():
    print("\n--- Chapter 1: The Mysterious Forest ---")
    time.sleep(1)
    print("You wake up in a dense forest with no memory of how you got there.")
    time.sleep(1)
    print("You see two paths ahead. One leads deeper into the forest, and the other goes towards a distant castle.")

    choices = ["Explore the forest", "Head towards the castle"]
    choice = make_choice(choices)

    if choice == 1:
        print("As you explore the forest, you encounter a group of friendly elves who offer to guide you.")
        time.sleep(1)
        print("They lead you to a hidden village where you learn about a dark force threatening the land.")

    elif choice == 2:
        print("You decide to head towards the castle. On your way, you encounter a mysterious figure.")
        time.sleep(1)
        print("The figure warns you about the dangers ahead and gives you a magical amulet for protection.")

def chapter_two():
    print("\n--- Chapter 2: The Enchanted Cavern ---")
    time.sleep(1)
    print("You reach an enchanted cavern with glowing crystals and a mystical aura.")
    time.sleep(1)
    print("As you explore, you come across a fork in the path. One leads to a treacherous abyss, and the other to a hidden chamber.")

    choices = ["Cross the abyss", "Enter the hidden chamber"]
    choice = make_choice(choices)

    if choice == 1:
        print("You bravely attempt to cross the abyss, but it's too dangerous.")
        time.sleep(1)
        print("You fall into the darkness below, and your adventure comes to an unfortunate end.")

    elif choice == 2:
        print("You enter the hidden chamber and discover a powerful artifact.")
        time.sleep(1)
        print("The artifact grants you the ability to control elements, enhancing your journey.")

def conclusion():
    print("\n--- Conclusion ---")
    time.sleep(1)
    print("Your journey has been filled with challenges and discoveries.")
    time.sleep(1)
    print("The choices you made have shaped your destiny.")

    # Generate a random ending
    endings = ["Congratulations! You become the hero the land needed.", "You succumb to the dark force and become its servant."]
    print(random.choice(endings))

# Main game loop
def play_game():
    introduction()
    chapter_one()
    chapter_two()
    conclusion()

if __name__ == "__main__":
    play_game()
