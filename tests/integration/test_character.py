from entities.character import Character
from item import Item
from constants import MAX_INVENTORY_SLOTS

def test_remove_item_success():
    # Arrange
    item1 = Item(name="Sword", damage_boost=10, defense_boost=5, health_boost=0)
    item2 = Item(name="Shield", damage_boost=0, defense_boost=10, health_boost=5)
    character = Character(level=1, inventory=[item1, item2])

    # Act
    result = character.remove_item(0)

    # Assert
    assert result == True
    assert len(character.inventory) == 1
    assert character.inventory[0].name == "Shield"

def test_remove_item_invalid_index():
    # Arrange
    item1 = Item(name="Sword", damage_boost=10, defense_boost=5, health_boost=0)
    character = Character(level=1, inventory=[item1])

    # Act
    result = character.remove_item(1)

    # Assert
    assert result == False
    assert len(character.inventory) == 1

def test_remove_item_empty_inventory():
    # Arrange
    character = Character(level=1, inventory=[])

    # Act
    result = character.remove_item(0)

    # Assert
    assert result == False
    assert len(character.inventory) == 0
