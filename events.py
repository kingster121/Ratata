from time import sleep

class Rat:
    def __init__(self):
        self.health = 100
        self.filth = 50
        self.size = 1
        self.hunger = 70
        self.rat_gang = []
        self.belongings = {}

rat = Rat()

def meet_hobo(rat: Rat):
    # Dialogue
    print("You have encountered a hobo that finds you cute.")
    sleep(1.5)
    print("He passed you a cheese and went on his way.")
    sleep(1.5)

    # Choices
    print("1. Keep the cheese in your belonging")
    print("2. Eat the cheese")

    # User input
    choice = input("Choose\n")

    match choice:
        case "1":
            rat.belongings["Cheese"] += 1
            print(rat.belongings)

        case "2":
            rat.health += 10
            rat.hunger += 10

meet_hobo(rat)