from math import sqrt
from random import random

class Entity():
    
    def __init__(self, name: str, level: int = 1):
        if level <= 0:
            raise TypeError('Nível não pode ser negativo ou zero.')

        self.name = name
        self.level = level

    def __str__(self):
        return f'Entidade com {self.health} de vida, com {self.damage} de dano e {self.defense} de defesa.\n'
    
    def attack(self, other) -> str:
        damage_dealt = self.damage - other.defense
        other.health -= max(0, damage_dealt)
        rng_crit = random()

        if rng_crit <= self.crit_chance:
            damage_dealt *= 2
            other.health -= max(0, damage_dealt)
            return f"{self.name} atacou {other.name}, causando {damage_dealt} de dano. Vida restante de {other.name}: {other.health} / {other.max_health}. Foi um golpe crítico!\n"

        return f"{self.name} atacou {other.name}, causando {damage_dealt} de dano. Vida restante de {other.name}: {other.health} / {other.max_health}.\n"

    def scalability(
            self, 
            health_multiplier: int,
            damage_multipler: int,
            defense_multiplier: int
            ) -> None:
        self.health = self.level * health_multiplier
        self.max_health = self.health
        self.damage = self.level * damage_multipler
        self.defense = self.level * defense_multiplier
        self.crit_chance = round((sqrt(self.level * 100) / 100), 2)

    def heal(self) -> None:
        self.health = self.max_health

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

    @property
    def crit_chance(self):
        return self.__crit_chance
    
    @crit_chance.setter
    def crit_chance(self, value):
        self.__crit_chance = value