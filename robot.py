from weapons import Weapons


class Robots:

    def __init__ (self,name, phrase):
        self.name = name
        self.health = 75
        self.weapon = Weapons("Blue Lightsaber",35)
        self.phrase = phrase

# when we call attack() on battlefleld we must remember to pass in a dino we are attacking
    def attack (self,dino): 
        dino.health -= self.weapon.attack_power  #use print statment to explain to the user what happend
        print(f'{self.name} is attacking {dino.name}, {self.name} screams  {self.phrase} and did {self.weapon.attack_power} damage, {dino.name} has {dino.health} remaining')
