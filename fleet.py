from msilib.schema import SelfReg
from robot import Robots





class Fleet:

    def __init__(self):
        self.fleet_list = []
        self.create_fleet()

        
    def create_fleet(self):  # need to make 3 robot and append them to the fleet_list above
        gundam = Robots("Gundam VX", "The Force is with me! *Xena battlecry*")
        self.fleet_list.append(gundam)

        autobots = Robots ('Optimus Prime','AUTOBOTS, ROLL OUT on this lizards $%& !')
        self.fleet_list.append(autobots)