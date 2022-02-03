from robot import Robots

class Dinos:

    def __init__ (self,name,attack_power,attack_name):
        self.name = name
        self.health = 80
        self.attack_power = attack_power
        self.attack_name = attack_name


    def attack (self,robots):
        robots.health -= self.attack_power
        print(f'{self.name} is attacking {robots.name}, {self.name} used {self.attack_name} and did {self.attack_power} damage, {robots.name} has {robots.health} points remaining')
        



