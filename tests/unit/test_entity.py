import pytest
from entities.character import Character
from entities.enemy import Enemy
from item import Item

@pytest.fixture
def character() -> Character:
    character = Character(level=5)
    character.max_health = 100
    character.health = 100
    character.damage = 20
    character.defense = 10
    character.name = "Hero"
    return character

@pytest.fixture
def enemy() -> Enemy:
    enemy = Enemy(name="Goblin", level=3, health=50, damage=15, defense=5)
    return enemy

@pytest.fixture
def item() -> Item:
    return Item(name="Sword", damage_boost=10, defense_boost=5, health_boost=20)

# Testes básicos

def test_character_creation(character: Character):
    assert character.name == "Hero"
    assert character.level == 1
    assert character.health == 100
    assert character.damage == 20
    assert character.defense == 10

def test_enemy_creation(enemy: Enemy):
    assert enemy.name == "Goblin"
    assert enemy.level == 1
    assert enemy.health == 30
    assert enemy.damage == 10
    assert enemy.defense == 5

# Testes de combate

def test_character_attack_enemy(character: Character, enemy: Enemy):
    initial_health = enemy.health
    damage_dealt = max(character.damage - enemy.defense, 0)
    enemy.health -= damage_dealt
    assert enemy.health == initial_health - damage_dealt
    assert enemy.health >= 0

def test_enemy_attack_character(character: Character, enemy: Enemy):
    initial_health = character.health
    damage_dealt = max(enemy.damage - character.defense, 0)
    character.health -= damage_dealt
    assert character.health == initial_health - damage_dealt
    assert character.health >= 0

def test_character_pickup_item(character: Character, item: Item):
    character.add_item(item)
    assert item in character.inventory

def test_character_equip_item(character: Character, item: Item):
    character.add_item(item)
    character.equip_item(0)
    assert item.is_equiped
    assert character.damage == 20 + item.damage_boost
    assert character.defense == 10 + item.defense_boost
    assert character.health == 100 + item.health_boost

def test_character_equip_item_invalid_index(character: Character, item: Item):
    """Testa o personagem tentando equipar um item com índice inválido."""
    character.add_item(item)
    assert not character.equip_item(-1)
    assert not character.equip_item(10)

# Testes de morte

def test_character_death(character: Character, enemy: Enemy):
    """Testa a morte de um personagem ao perder toda a saúde."""
    while character.health > 0:
        damage_dealt = max(enemy.damage - character.defense, 0)
        character.health -= damage_dealt

    assert character.health <= 0
    assert character.is_alive() == False

def test_enemy_death(character: Character, enemy: Enemy):
    """Testa a morte de um inimigo ao perder toda a saúde."""
    while enemy.health > 0:
        damage_dealt = max(character.damage - enemy.defense, 0)
        enemy.health -= damage_dealt

    assert enemy.health <= 0
    assert enemy.is_alive() == False
    
def test_character_vs_enemy_combat(character: Character, enemy: Enemy):
    """Simula um combate completo entre um personagem e um inimigo."""
    while character.is_alive() and enemy.is_alive():
        # Personagem ataca inimigo
        damage_to_enemy = max(character.damage - enemy.defense, 0)
        enemy.health -= damage_to_enemy

        # Inimigo ataca personagem, se ainda vivo
        if enemy.is_alive():
            damage_to_character = max(enemy.damage - character.defense, 0)
            character.health -= damage_to_character

    # Verificar o resultado do combate
    assert not (character.is_alive() and enemy.is_alive())  # Apenas um pode estar vivo
    assert character.is_alive() or enemy.is_alive()
