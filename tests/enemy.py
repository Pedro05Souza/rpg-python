#CLASSE ENEMY.PY NA PASTA UNITYTEST


import pytest
from unittest.mock import patch, MagicMock
from entities.character import Character
from entities.enemy import Enemy
from item import Item

def test_on_enemy_death():
    # Criar personagem e inimigo
    character = Character(name="Hero", level=1, xp=0)
    items = [Item("Sword"), Item("Shield")]
    enemy = Enemy(enemy_name="Goblin", enemy_level=2, drop_items=items)


    initial_xp = character.xp
    initial_level = character.level

    # Simular a morte do inimigo
    with patch('random.random', return_value=0.5):
        dropped_item = enemy.on_enemy_death(character)


    assert character.xp == initial_xp + 100
    assert character.level > initial_level
    assert dropped_item in items

def test_enemy_drop_no_items():
    # Inimigo sem itens para drop
    enemy = Enemy(enemy_name="Skeleton", enemy_level=3, drop_items=[])

    for  in range(10):
        assert enemy._Enemyenemy_drop() is None

def test_enemy_drop_logic():
    # Inimigo com itens para drop
    items = [Item("Potion"), Item("Elixir")]
    enemy = Enemy(enemy_name="Zombie", enemy_level=5, drop_items=items)

    with patch('random.random', return_value=0.2): 
        assert enemy._Enemyenemy_drop() is None

    with patch('random.random', return_value=0.5):
        assert enemy._Enemy__enemy_drop() in items