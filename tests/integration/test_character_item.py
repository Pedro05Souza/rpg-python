from entities.character import Character
from item import Item
from constants import MAX_INVENTORY_SLOTS


def test_remove_item_success():
    item1 = Item(name="Sword", damage_boost=10, defense_boost=5, health_boost=0)
    item2 = Item(name="Shield", damage_boost=0, defense_boost=10, health_boost=5)
    character = Character(level=1, inventory=[item1, item2])
    result = character.remove_item(0)

    assert result == True
    assert len(character.inventory) == 1
    assert character.inventory[0].name == "Shield"


def test_remove_item_invalid_index():
    item1 = Item(name="Sword", damage_boost=10, defense_boost=5, health_boost=0)
    character = Character(level=1, inventory=[item1])
    result = character.remove_item(1)

    assert result == False
    assert len(character.inventory) == 1


def test_remove_item_empty_inventory():
    character = Character(level=1, inventory=[])
    result = character.remove_item(0)

    assert result == False
    assert len(character.inventory) == 0


def test_add_item_success():
    item = Item(name="Helmet", damage_boost=0, defense_boost=5, health_boost=10)
    character = Character(level=1, inventory=[])
    result = character.add_item(item)

    assert result == True
    assert len(character.inventory) == 1
    assert character.inventory[0].name == "Helmet"


def test_add_item_inventory_full():
    items = [
        Item(name=f"Item{i}", damage_boost=0, defense_boost=0, health_boost=0)
        for i in range(MAX_INVENTORY_SLOTS)
    ]
    character = Character(level=1, inventory=items)
    new_item = Item(name="ExtraItem", damage_boost=0, defense_boost=0, health_boost=0)
    result = character.add_item(new_item)

    assert result == False
    assert len(character.inventory) == MAX_INVENTORY_SLOTS