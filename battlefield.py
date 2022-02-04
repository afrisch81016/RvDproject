from herd import Herd
from fleet import Fleet
import random


def get_random (self,random_team):
        random_opponent = random.choice()


class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.display_welcome

    def display_welcome(self):
         print('Welcome to the THUNDA DOME!!')

    def battle(self):
        self.dino_turn()
        self.robo_turn()

        while len(self.fleet.fleet_list) > 0 and len(self.herd.herd_list) > 0:
             self.dino_turn()
             self.robo_turn()

             if len(self.fleet.fleet_list) > 0 and len(self.herd.herd_list) < 0:
                self.display_winner
             elif len (self.herd.herd_list) > 0 and len(self.fleet.fleet_list) < 0:
                 self.display_winner
            
                

        

        self.display_winner()   

    def display_winner (self):
        print("Congrats! You have done it, and have shown the world whos the best!! BOOYAH")

         
    def show_robo_opponent_options (self):

        for robot in (self.fleet.fleet_list):
            print(robot.name,robot.health,"Health")

    def robo_turn (self):

        attacking_robot = random.choice (self.fleet.fleet_list)

        robots_attack = random.choice (self.herd.herd_list)

        attacking_robot.attack(robots_attack)

        if robots_attack.health <= 0:
            self.herd.herd_list.remove (robots_attack)
            self.show_robo_opponent_options()


    def show_dino_opponent_opt (self):

        for dino in (self.herd.herd_list):
            print(dino.name,dino.health,"Health")

    def dino_turn (self):
        
        attacking_dino = random.choice (self.herd.herd_list)
        print(attacking_dino.name)

        dino_attack = random.choice (self.fleet.fleet_list)
        print(dino_attack.name)

        attacking_dino.attack(dino_attack)

        if dino_attack.health <= 0:
            self.fleet.fleet_list.remove (dino_attack)
            self.show_dino_opponent_opt()








    def run_game(self):
        self.battle ()
        