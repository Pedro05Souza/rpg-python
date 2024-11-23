import pytest
from unittest.mock import patch
from entities import Enemy, Character
from game_handler import enemy_creator
from copy import deepcopy
from item import Item

@pytest.fixture
def enemy() -> Enemy:
    return deepcopy(enemy_creator(1))

@pytest.fixture
def character() -> Character:
    return deepcopy(Character())

@pytest.fixture
def item() -> Item:
    return Item(name="Sword", damage_boost=10, defense_boost=5, health_boost=20)

def test_on_enemy_death(character: Character, enemy: Enemy) -> None:
    enemy.on_enemy_death(character)
    assert character.xp == enemy.xp

def test_enemy_drop_low_chance(enemy: Enemy, item: Item) -> None:
    enemy.drop_items = [item]

    with patch("entities.enemy.random") as mock_random:
        mock_random.return_value = 0.2
        assert enemy._Enemy__enemy_drop() is None

def test_enemy_drop_high_chance(enemy: Enemy, item: Item) -> None:
    enemy.drop_items = [item]

    with patch("entities.enemy.random") as mock_random:
        mock_random.return_value = 0.8
        assert enemy._Enemy__enemy_drop() == enemy.drop_items[0]