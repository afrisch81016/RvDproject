from dinos import Dinos

class Herd:

    def __init__ (self):
        self.herd_list = []
        self.create_herd()

    def create_herd(self):  # make 3 and append them to the list above 
        ty_rex = Dinos("REXington", 45, "Chompy Chomp")
        self.herd_list.append(ty_rex)

        tri_tops = Dinos ('TRI-SaraClops', 40,"TRI-Horn Barrage")
        self.herd_list.append (tri_tops)









