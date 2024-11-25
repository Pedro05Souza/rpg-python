import pytest
from entities import Character
from item import Item
from constants import MAX_INVENTORY_SLOTS, MAX_EQUIPS
from copy import deepcopy


@pytest.fixture
def character() -> Character:
    character = Character(level=1)
    character.max_health = character.level * 2
    character.damage = character.level * 2
    character.defense = 2
    character.health = character.max_health
    character.name = "Hero"
    return deepcopy(character)


@pytest.fixture
def item() -> Item:
    return Item(name="Sword", damage_boost=10, defense_boost=5, health_boost=20)


def test_add_item(character: Character, item: Item) -> None:
    character.add_item(item)
    assert item in character.inventory


def test_equip_item_max_equips(character: Character) -> None:

    for item in range(MAX_INVENTORY_SLOTS):
        item = Item(name=f"Item{item}")
        character.add_item(item)

    for item in range(MAX_EQUIPS):
        character.equip_item(item)

    assert character.equip_item(2) == False


def test_unequip_item(character: Character, item: Item):
    character.add_item(item)
    character.equip_item(0)
    assert character.unequip_item(0) == True


def test_unequip_item_not_equiped(character: Character, item: Item):
    character.add_item(item)
    assert character.unequip_item(0) == False


def test_remove_item(character: Character, item: Item):
    character.add_item(item)
    character.remove_item(0)
    assert item not in character.inventory


def test_remove_item_invalid_index(character: Character, item: Item):
    character.add_item(item)
    assert character.remove_item(-1) == False


def test_equip_item(character: Character, item: Item):
    character.add_item(item)
    character.equip_item(0)
    assert item.is_equiped


def test_add_item_inventory_full(character: Character, item: Item):
    for i in range(MAX_INVENTORY_SLOTS):
        item = Item(name=f"Item{i}")
        character.add_item(item)

    assert character.add_item(item) == False
