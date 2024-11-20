from entities.entity import Entity
from utils import input_validator
from item import Item
from constants import MAX_INVENTORY_SLOTS, MAX_EQUIPS

class Character(Entity):

    def __init__(self, level: int = 1, inventory: list = []):
        super().__init__(level)
        self.inventory = inventory
        self.xp = 0

    def level_up(self):
        if self.xp >= self.level * 100:
            self.max_health *= 2 
            self.damage =+ self.damage
            self.defense += 2
            self.level += 1
            self.xp = 0
            print("\nVocê subiu de nível! Seu nível atual é: ", self.level)

    def add_item(self, item: Item) -> None:
        if len(self.inventory) > MAX_INVENTORY_SLOTS:
            print(f"Você não pode adicionar mais de {MAX_INVENTORY_SLOTS} itens ao inventário.")

        self.inventory.append(item)
        print(f"Item {item.name} adicionado ao inventário.")
    
    def remove_item(self, index: int) -> None:
        if index < 0 or index > len(self.inventory) - 1:
            print("Posição inválida.")
            return
        
        item = self.inventory[index]
        self.inventory.remove(item)
        print(f"Item {item.name} removido do inventário.")
    
    def __equip_item(self, item: Item) -> None:
        current_equips = [item for item in self.inventory if item.is_equiped]
        current_equips = len(current_equips)

        if current_equips == MAX_EQUIPS:
            print(f"Você não pode equipar mais de {MAX_EQUIPS} itens.")
            return

        self.max_health += item.health_boost
        self.damage += item.damage_boost
        self.defense += item.defense_boost

        print(f"Item {item.name} equipado.")

    def __unequip_item(self, index: int) -> None:
        if index < 0 or index > len(self.inventory) - 1:
            print("Posição inválida.")
        
        item = self.inventory[index]

        if not item.is_equiped:
            print(f"Item {item.name} não está equipado.")
            return
        
        self.max_health -= item.health_boost
        self.damage -= item.damage_boost
        self.defense -= item.defense_boost
        print(f"Item {item.name} desequipado.")
    
    def retrieve_character_status(self) -> None:
        print(
            "--- Status do personagem --- \n" +
            f"Nome: {self.name}\n" +
            f"Nível: {self.level}\n" +
            f"Vida: {self.health} / {self.max_health}\n" +
            f"Dano: {self.damage}\n" +
            f"Defesa: {self.defense}\n" +
            f"XP: {self.xp} / {self.level * 100}"
            )
        
    def __display_inventory(self) -> None:
        for index, item in enumerate(self.inventory):
            print(
                "------------------\n" +
                f"Posição: {index + 1}\n" +
                f"Nome: {item.name}\n" +
                f"Dano: {item.damage_boost}\n" +
                f"Defesa: {item.defense_boost}\n" +
                f"Vida: {item.health_boost}\n"
                f"Equipado: {'Sim' if item.is_equiped else 'Não'}\n" +
                "------------------\n"
                )
            
    def inventory_handler(self) -> None:

        if not self.inventory:
            print("Inventário vazio.")
            return
        user_input = 0
        
        while user_input != 3:
            self.__display_inventory()
            print("O que deseja fazer?\n")
            print("[1]. Equipar item\n")
            print("[2]. Desequipar item\n")
            print("[3]. Sair\n")

            user_input = int(input())

            if user_input == 3:
                break

            item_position = input_validator(int, "Insira a posição do item: ") - 1

            if not self.__index_validator(item_position):
                continue
            
            if user_input == 1:
                self.__equip_item(self.inventory[item_position])
            elif user_input == 2:
                self.__unequip_item(item_position)
            else:
                print("Opção inválida.")

    def __index_validator(self, index: int):
        if index < 0 or index > len(self.inventory) - 1:
            print("Posição inválida.")
            return False
        return True