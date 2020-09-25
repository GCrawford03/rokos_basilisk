class Item():
    # the base class for all items/drones
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

# damage and hp is placeholder

class Robot(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class DroneOne(Robot):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value, damage)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class WayneBot(Robot):
    def __init__(self):
        super().__init__(name="Stick",
                         description="That's a big stick.",
                         value=0,
                         damage=5)
 
class DroneThree(Robot):
    def __init__(self):
        super().__init__(name="Drone Three",
                         description="Add a description.",
                         value=10,
                         damage=10)   