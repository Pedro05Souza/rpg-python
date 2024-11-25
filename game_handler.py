from math import ceil
from entities import Character, Enemy
from item import Item
from random import randint
from utils import clear_terminal, name_generator, input_validator


def event_loop(character: Character) -> None:

    while character.health > 0:
        menu()
        user_input = input_validator(int, "Insira a escolha desejada:\n")

        match user_input:

            case 1:
                enemy = enemy_creator(character.level)
                combat(character, enemy)

            case 2:
                character.retrieve_character_status()

            case 3:
                character.inventory_handler()

            case 4:
                print("Saindo do jogo...\n")
                break

            case _:
                print("Opção inválida.\n")


def menu() -> None:
    print(
        "--- Menu ---\n"
        + "[1]. Atacar Inimigos\n"
        + "[2]. Ver Atributos\n"
        + "[3]. Ver Inventário\n"
        + "[4]. Sair\n"
    )


def enemy_creator(player_level: int) -> Enemy:
    enemy_level = randint(ceil(player_level / 1.5), player_level)
    enemy_name = name_generator()
    enemy_drops = randint(0, 3)
    created_items = [item_creator(enemy_level) for _ in range(enemy_drops)]
    e = Enemy(enemy_name, enemy_level, created_items)
    e.scalability(30, 15, 5)
    return e


def character_creator() -> Character:
    character_name = input_validator(str, "Insira o nome do seu personagem:\n")
    return Character(character_name=character_name)


def item_creator(character_level: int) -> Item:
    item_name = name_generator()
    max_range = character_level * 4

    damage_boost = randint(1, max_range)
    defense_boost = randint(1, max_range)
    health_boost = randint(1, max_range)

    return Item(item_name, damage_boost, defense_boost, health_boost)


def combat(c: Character, e: Enemy) -> None:

    print(f"Você encontrou um {e.name} de nível {e.level}!\n")

    while c.health > 0 and e.health > 0:
        print("\n--- Menu de Batalha ---\n" + "[1]. Atacar\n" + "[2]. Fugir\n")
        user_input = input_validator(int, "Insira a escolha desejada:\n")

        match user_input:

            case 1:
                print(c.attack(e))
                print(e.attack(c))

            case 2:
                runaway_chance = randint(0, 3)
                if runaway_chance == 0:
                    print("Você fugiu com sucesso!\n")
                    c.heal()
                    break
                else:
                    print("Você não conseguiu fugir!\n")
                    print(e.attack(c))

            case _:
                print("Opção inválida.\n")

        if c.health <= 0 or e.health <= 0:
            death_handler(c, e)


def death_handler(c: Character, e: Enemy) -> None:
    if c.health <= 0:
        print("Você morreu!\n")
        print(f"Você foi morto por {e.name} de nível {e.level}.\n")
        return

    print(f"Você derrotou {e.name} de nível {e.level}!\n")
    item_dropped = e.on_enemy_death(c)
    c.heal()

    if not item_dropped:
        return

    print(f"{e.name} deixou cair um item: {item_dropped.name}.\n")
    print("[1]. Pegar item\n" + "[2]. Deixar item\n")
    user_input = input_validator(int, "Insira a escolha desejada:\n")

    match user_input:

        case 1:
            c.inventory.append(item_dropped)
            print(f"{item_dropped.name} foi adicionado ao seu inventário!\n")

        case 2:
            print(f"{item_dropped.name} foi deixado para trás.\n")

        case _:
            print("Opção inválida.\n")

    clear_terminal()
