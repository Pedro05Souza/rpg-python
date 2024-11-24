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

def test_inventory_handling():
    # Arrange
    item1 = Item(name="Sword", damage_boost=10, defense_boost=5, health_boost=0)
    item2 = Item(name="Shield", damage_boost=0, defense_boost=10, health_boost=5)
    character = Character(level=1, inventory=[item1, item2])

    # Act & Assert
    # Test adding an item
    item3 = Item(name="Helmet", damage_boost=0, defense_boost=5, health_boost=10)
    assert character.add_item(item3) == True
    assert len(character.inventory) == 3

    # Test equipping an item
    assert character.equip_item(0) == True
    assert character.inventory[0].is_equiped == True

    # Test removing an item
    assert character.remove_item(1) == True
    assert len(character.inventory) == 2
    assert character.inventory[0].name == "Sword"
    assert character.inventory[1].name == "Helmet"