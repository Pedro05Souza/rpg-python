class Item():

    def __init__(self, name, damage_boost=0, defense_boost=0, health_boost=0):
        self.name = name
        self.damage_boost = damage_boost
        self.defense_boost = defense_boost
        self.health_boost = health_boost
        self.is_equiped = False

    def __str__(self) -> str:
        return f"Item: {self.name}, Dano: {self.damage_boost}, Defesa: {self.defense_boost}, Vida: {self.health_boost}"