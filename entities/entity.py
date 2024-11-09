
class Entity():
    
    def __init__(self, name: str, level: int = 1):
        if level < 0:
            raise TypeError('Level must be amove 0')
        
        self.name = name
        self.health = 1
        self.max_health = 1
        self.damage = 1
        self.defense = 1
        self.level = level
        self.xp = 0
        self.scalability()

    def __str__(self):
        return f'character with {self.health} hp, with {self.damage} damage and {self.defense}'
    
    def attack(self, other) -> str:
        damage_dealt = self.damage - other.defense
        other.health -= max(0, damage_dealt)
        return f"{self.name} attacked {other.name}, dealing {damage_dealt} of damage."

    def scalability(self):
        self.health = self.level * 100
        self.max_health = self.health
        self.damage = self.level * 5
        self.defense = self.level * 2

    @property
    def health(self):
        return self.__health

    @property
    def damage(self):
        return self.__damage

    @property
    def defense(self):
        return self.__defense

    @health.setter
    def health(self, value):
        self.__health = value

    @damage.setter
    def damage(self, value):
        self.__damage = value

    @defense.setter
    def defense(self, value):
        self.__defense = value

    @property
    def level(self):
        return self.__level
    
    @level.setter
    def level(self, value):
        self.__level = value

    @property
    def xp(self):
        return self.__xp
    
    @xp.setter
    def xp(self, value):
        self.__xp = value
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value