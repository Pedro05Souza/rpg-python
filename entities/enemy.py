from entities.entity import Entity
from entities.character import Character
from item import Item
from random import random, choice

class Enemy(Entity):

    def __init__(self, enemy_name: str, enemy_level: int, drop_items: list = []):
        super().__init__(enemy_name, enemy_level)
        self.drop_items = drop_items
        self.xp = enemy_level * 100 // 2
        self.scalability()

    def on_enemy_death(self, character: Character):
        character.xp += self.xp
        character.level_up()

    def enemy_drop(self) -> Item:
        drop_chance = random()
        
        if drop_chance <= .3:
            return None
        
        return choice(self.drop_items)