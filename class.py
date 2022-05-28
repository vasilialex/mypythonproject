

class Hero:
    """class to create hero for our game"""
    def __init__(self, name, level, rase):
        """initiate our hero"""
        self.name = name
        self.level = level
        self.rase = rase
        self.health = 100

    def show_hero(self):
        """print all parameters of hero"""
        description = (self.name + " Level is:" + str(self.level) + " "+ "Rase is:" + self.rase + " " + str(self.health))
        print(description)

    def level_up(self):
        """upgrade level for hero"""
        self.level += 1

    def move(self):
        """start moving hero"""
        print("hero " + self.name + "start moving ...")

    def set_health(self, new_health):
        self.health = new_health
        if new_health <= 0:
            print("hero is die")

my_hero1 = Hero("Vurdalak", 5, "orc")
my_hero2 = Hero("Alexandr", 4, "human")

my_hero1.show_hero()
my_hero1.set_health(0)



