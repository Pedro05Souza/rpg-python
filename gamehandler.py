from entities import Character, Enemy
from item import Item
from name_generator import name_generator
from random import randint

def event_loop(character: Character) -> None:

  while character.health > 0:

    menu()
    user_input = int(input("Insira a escolha desejada:"))

    match user_input:

      case 1:
        enemy = enemy_creator(character.level)
        combat(character, enemy)

      case 2:
        character.retrieve_character_status()

      case 3:
        print(character.inventory)

      case 4:
        print("Saindo do jogo...")
        break

      case _:
        print("Opção inválida.")
  
def menu() -> None:
  print(
      "--- Menu ---\n" +
    "[1]. Atacar Inimigos\n" +
    "[2] Ver Atributos\n" +
    "[3]. Ver Inventário\n" +
    "[4]. Sair\n"
    )

def enemy_creator(player_level: int) -> Enemy:
  min_range = max(1, player_level // 1.5)
  max_range = int(player_level * 2)
  enemy_level = randint(min_range, max_range)

  enemy_name = name_generator()
  enemy_drops = randint(0, 3)
  created_items = [item_creator(enemy_level) for _ in range(enemy_drops)]
  return Enemy(enemy_name, enemy_level, created_items)

def character_creator() -> Character:
  character_name = input("Insira o nome do personagem:")
  return Character(character_name)

def item_creator(character_level: int) -> Item:
  item_name = name_generator()
  max_range = character_level * 4

  damage_boost = randint(1, max_range)
  defense_boost = randint(1, max_range)
  health_boost = randint(1, max_range)

  return Item(item_name, damage_boost, defense_boost, health_boost)

def combat(c: Character, e: Enemy) -> None:

  while c.health > 0 and e.health > 0:
    print(
      "\n--- Menu de Batalha ---\n" +
      "[1]. Atacar\n" +
      "[2]. Fugir\n"
      )
    user_input = int(input("Insira a escolha desejada:"))

    match user_input:

      case 1:
        print(c.attack(e))
        print(e.attack(c))

      case 2:
        runaway_chance = randint(0, 3)
        if runaway_chance == 0:
          print("Você fugiu com sucesso!")
          break
        else:
          print("Você não conseguiu fugir!")
          print(e.attack(c))

      case _:
        print("Opção inválida.")