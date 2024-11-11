from entities.entity import Entity
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
        
        item = self.inventory[index]
        self.inventory.remove(item)
        print(f"Item {item.name} removido do inventário.")
    
    def equip_item(self, item: Item) -> str:
        current_equips = [item for item in self.inventory if item.is_equiped]
        current_equips = len(current_equips)

        if current_equips == MAX_EQUIPS:
            return print(f"Você não pode equipar mais de {MAX_EQUIPS} itens.")

        self.health += item.health_boost
        self.damage += item.damage_boost
        self.defense += item.defense_boost

        print(f"Item {item.name} equipado.")

    def unequip_item(self, index: int) -> None:
        if index < 0 or index > len(self.inventory) - 1:
            print("Posição inválida.")
        
        item = self.inventory[index]

        if not item.is_equiped:
            print(f"Item {item.name} não está equipado.")
            return
        
        self.health -= item.health_boost
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
        
    def display_inventory(self) -> None:
        if not self.inventory:
            print("Inventário vazio.")
            return
        
        for item in self.inventory:
            print(
                "------------------\n" +
                f"Nome: {item.name}" +
                f"Dano: {item.damage_boost}" +
                f"Defesa: {item.defense_boost}" +
                f"Vida: {item.health_boost}"
                "------------------\n"
                )