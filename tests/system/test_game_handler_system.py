from math import ceil
from entities.character import Character
from entities.enemy import Enemy
from game_handler import enemy_creator, item_creator, character_creator
import pytest


@pytest.fixture
def character(monkeypatch) -> Character:
    monkeypatch.setattr("builtins.input", lambda _: "TestCharacter")
    character = character_creator()
    character.scalability(30, 15, 5)
    return character


@pytest.fixture
def enemy() -> Enemy:
    enemy = enemy_creator(1)
    return enemy


def test_character_creation(character: Character):
    assert character.level == 1
    assert character.name == "TestCharacter"


def test_enemy_creation_level(enemy: Enemy, character: Character):
    assert ceil(character.level / 1.5) <= enemy.level <= character.level


def test_item_creation():
    item = item_creator(5)
    assert 1 <= item.damage_boost <= 20
    assert 1 <= item.defense_boost <= 20
    assert 1 <= item.health_boost <= 20


def test_combat(character: Character, enemy: Enemy):
    character.attack(enemy)
    assert enemy.health < enemy.max_health


def test_character_level_up(character: Character):
    character.xp = character.level * 100

    assert character.level_up() == True


def test_enemy_damage(character: Character, enemy: Enemy):
    enemy.attack(character)
    assert character.max_health > character.health

def test_character_health_after_combat(character: Character, enemy: Enemy):
    initial_health = character.health
    enemy.attack(character)
    assert character.health < initial_health


def test_enemy_health_after_combat(character: Character, enemy: Enemy):
    initial_health = enemy.health
    character.attack(enemy)
    assert enemy.health < initial_health


def test_character_level_up_xp_reset(character: Character):
    character.xp = character.level * 100
    assert character.level_up()
    assert character.xp == 0


def test_enemy_level_scaling(enemy: Enemy, character: Character):
    assert enemy.level >= ceil(character.level / 1.5)
    assert enemy.level <= character.level


def test_character_full_health_recovery(character: Character):
    character.health = character.max_health // 2
    character.health = character.max_health 
    assert character.health == character.max_health


def test_enemy_health_never_negative(enemy: Enemy):
    while enemy.health > 0:
        enemy.health -= 10
    assert enemy.health == 0
