class Accessory():
    def __init__(self):
        self.helmet = input("Is accessory a Helmet? True/False")
        self.helmet_size = input("If yes, is helmet size; S, M, L ?")
        self.kids_seat = input("Is accessory a kids seat? True/False")
        self.seat_size = input("if yes, what is the seat size?")

    def set_helmet(self, helmet):    
        self._helmet = helmet

    def get_helmet(self):
        return self._helmet

    helmet = property(get_helmet, set_helmet)

    def set_helmet_size(self, helmet_size):
        self._helmet_size = helmet_size

    def get_helmet_size(self):
        return self._helmet_size    

    helmet_size = property(get_helmet_size, set_helmet_size)    

    def set_kids_seat(self, kids_seat):
        self._kids_seat = kids_seat

    def get_kids_seat(self):
        return self._kids_seat

    kids_seat = property(get_kids_seat, set_kids_seat)

    def set_seat_size(self, seat_size):
        self._seat_size = seat_size

    def get_seat_size(self):
        return self._seat_size

    seat_size = property(get_seat_size, set_seat_size)                

accesory_list = []



def display_accessory():
    for accessory in accesory_list:
         print("Helmet: {} --> Size: {}. Kids seat: {} --> Size: {}".format(accessory.get_helmet(), accessory.get_helmet_size(), accessory.get_kids_seat(), accessory.get_seat_size()))


def main():        

    # Helm1 = Accessory()
    # Helm1.set_helmet(True)
    # Helm1.set_helmet_size("L")
    # Helm1.set_kids_seat(False)
    # Helm1.set_seat_size("N.v.t.")

    # Seat1 = Accessory()
    # Seat1.set_helmet(False)
    # Seat1.set_helmet_size("N.v.t.")
    # Seat1.set_kids_seat(True)
    # Seat1.set_seat_size("S")

    # accesory_list.append(Helm1)
    # accesory_list.append(Seat1)
    my_accessory = Accessory(helmet, helmet_size, )
    display_accessory()


if __name__ == '__main__': main()    