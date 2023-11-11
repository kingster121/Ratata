class Rat:
    def __init__(self):
        self.health = 100
        self.filth = 50
        self.size = 1
        self.hunger = 70
        self.rat_gang = []
        self.belongings = {}

    def display_stats(self):
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")

# rat = Rat()
# rat.display_stats()