from entity import Entity

class Character(Entity):

    def __init__(self, level: int = 1, inventory: list = []):
        super().__init__(level)
        self.inventory = inventory

    def __str__(self):
        return f'{self.__name} is a {super().__str__()}'
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    def levelUp(self):
        if self.xp >= self.level * 100:
            self.health += self.health
            self.damage + self.damage
            self.defense += 2
            self.level += 1
            self.xp = 0

    