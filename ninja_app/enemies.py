class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0

class Raider(Enemy):
    def __init__(self):
        super().__init__(name="Add a description.", hp=10, damage=2)