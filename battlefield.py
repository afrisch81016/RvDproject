from herd import Herd
from fleet import Fleet

class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.fleet.fleet_list[0].attack(self.herd.herd_list[0])
        
        self.herd.herd_list[0].attack(self.fleet.fleet_list[0])
        pass