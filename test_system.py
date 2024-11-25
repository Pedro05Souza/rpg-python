import unittest
from entities.character import Character
from entities.enemy import Enemy
from item import Item
from game_handler import event_loop, character_creator, enemy_creator, item_creator

class TestRPGSystem(unittest.TestCase):

    def test_character_creation(self):
        character = Character("Hero")
        self.assertEqual(character.name, "Hero")
        self.assertEqual(character.level, 1)

    def test_enemy_creation(self):
        enemy = enemy_creator(5)
        self.assertTrue(isinstance(enemy, Enemy))
        self.assertTrue(1 <= enemy.level <= 5)

    def test_item_creation(self):
        item = item_creator(5)
        self.assertTrue(isinstance(item, Item))
        self.assertTrue(1 <= item.damage_boost <= 20)
        self.assertTrue(1 <= item.defense_boost <= 20)
        self.assertTrue(1 <= item.health_boost <= 20)

    def test_combat(self):
        character = Character("Hero")
        enemy = Enemy("Goblin", 1)
        initial_health = character.health
        character.attack(enemy)
        self.assertTrue(character.health <= initial_health)

if __name__ == "__main__":
    unittest.main()
