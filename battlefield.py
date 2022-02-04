from herd import Herd
from fleet import Fleet
from robot import Robots
from random import Random


def get_random (self,random_team):
        random_opponent = Random.choice()


class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        

    def display_welcome(self):
         print('Welcome to the THUNDA DOME!!')
         
    def show_robo_oppent_options (self):
        print(self.herd)

    def robo_turn (self):

        attacking_robot = Random.choice (self.fleet.fleet_list)

        robots_attack = Random.choice (self.herd.herd_list)


    def show_dino_opponent_opt (self):
        
        dino_from_list =(""):
        if self.herd.herd_list = [0]:
            print(self.herd.herd_list[0])
        elif self.herd.herd_list = [1]:
            print (self.herd.herd_list[1])
        else:
            self.herd.herd_list = [2]:
            print(self.herd.herd_list [2])



    def dino_turn (self):
        
        attacking_dino = Random.choice (self.herd.herd_list)

        dino_attack = Random.choice (self.fleet.fleet_list)



    # def display_winner (self):
    #     print('Congradulations! You have done it, and have shown the world whos the best!! BOOYAH)




    def run_game(self):
        self.fleet.fleet_list[2].attack(self.herd.herd_list[1])
        
        self.herd.herd_list[2].attack(self.fleet.fleet_list[1])


        
