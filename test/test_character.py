import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from entities.character import Character
from item import Item
from constants import MAX_INVENTORY_SLOTS, MAX_EQUIPS

@pytest.fixture
def character():
    character = Character(level=1)
    character.max_health = character.level * 2
    character.damage = character.level * 2
    character.defense = 2
    character.health = character.max_health  # Inicializar health
    character.name = "Hero"  # Inicializar name
    return character

@pytest.fixture
def item():
    return Item(name="Sword", damage_boost=10, defense_boost=5, health_boost=20)

def test_add_item(character, item):
    character.add_item(item)
    assert item in character.inventory

def test_equip_item_max_equips(character, item):
    character.inventory = [Item(name=f"Item{i}", damage_boost=0, defense_boost=0, health_boost=0) for i in range(MAX_EQUIPS)]
    for i in range(MAX_EQUIPS):
        character.inventory[i].is_equiped = True
    character.add_item(item)
    character._Character__equip_item(item)
    assert item.is_equiped == False


def test_unequip_item(character, item):
    character.add_item(item)
    character._Character__equip_item(item)
    character._Character__unequip_item(0)
    assert not item.is_equiped


def test_retrieve_character_status(character, capsys):
    character.retrieve_character_status()
    captured = capsys.readouterr()
    assert "Nome: Hero" in captured.out
    assert f"Nível: {character.level}" in captured.out
    assert f"Vida: {character.health} / {character.max_health}" in captured.out
    assert f"Dano: {character.damage}" in captured.out
    assert f"Defesa: {character.defense}" in captured.out
    assert f"XP: {character.xp} / {character.level * 100}" in captured.out

def test_equip_item_max_equips(character, item, capsys):
    character.inventory = [Item(name=f"Item{i}", damage_boost=0, defense_boost=0, health_boost=0) for i in range(MAX_EQUIPS)]
    for i in range(MAX_EQUIPS):
        character.inventory[i].is_equiped = True
    character.add_item(item)
    character._Character__equip_item(item)
    captured = capsys.readouterr()
    assert f"Você não pode equipar mais de {MAX_EQUIPS} itens." in captured.out

def test_unequip_item_not_equiped(character, item, capsys):
    character.add_item(item)
    character._Character__unequip_item(0)
    captured = capsys.readouterr()
    assert f"Item {item.name} não está equipado." in captured.out

def test_display_inventory(character, item, capsys):
    character.add_item(item)
    character._Character__display_inventory()
    captured = capsys.readouterr()
    assert f"Item {item.name}" in captured.out

def test_remove_item(character, item):
    character.add_item(item)
    character.remove_item(0)
    assert item not in character.inventory

def test_remove_item_invalid_index(character, item, capsys):
    character.add_item(item)
    character.remove_item(1)
    captured = capsys.readouterr()
    assert "Posição inválida." in captured.out

def test_equip_item(character, item):
    character.add_item(item)
    character._Character__equip_item(item)
    assert item.is_equiped

def test_level_up(character):
    character.xp = character.level * 100
    character.level_up()
    assert character.level == 2
    assert character.max_health == 4
    assert character.damage == 4
    assert character.defense == 4
    assert character.xp == 0

def test_add_item_inventory_full(character, item, capsys):
    character.inventory = [Item(name=f"Item{i}", damage_boost=0, defense_boost=0, health_boost=0) for i in range(MAX_INVENTORY_SLOTS)]
    character.add_item(item)
    captured = capsys.readouterr()
    assert f"Você não pode adicionar mais de {MAX_INVENTORY_SLOTS} itens ao inventário." in captured.out
    assert item not in character.inventory

def test_inventory_handler_empty_inventory(character, capsys):
    character.inventory_handler()
    captured = capsys.readouterr()
    assert "Inventário vazio." in captured.out

def test_inventory_handler_equip_item(character, item, monkeypatch):
    character.add_item(item)
    inputs = iter([1, 1, 3])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    character.inventory_handler()
    assert item.is_equiped

def test_inventory_handler_unequip_item(character, item, monkeypatch):
    character.add_item(item)
    character._Character__equip_item(item)
    inputs = iter([2, 1, 3])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    character.inventory_handler()
    assert not item.is_equiped