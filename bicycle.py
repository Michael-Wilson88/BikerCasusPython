class Bicycle:
    def __init__(self):
        self._bike_number = 0
        self._bike_type = ""
        self._brand = ""
        self._sex = ""
        self._rental_price = 0     

    def set_bike_number(self, bike_number):
        self._bike_number = bike_number

    def get_bike_number(self):
        return self._bike_number    

    bike_number = property(get_bike_number, set_bike_number)

    def set_bike_type(self, bike_type):
        self._bike_type = bike_type

    def get_bike_type(self):
        return self._bike_type    

    bike_type = property(get_bike_type, set_bike_type)    

    def set_brand(self, brand):
        self._brand = brand        

    def get_brand(self):
        return self._brand

    brand = property(get_brand, set_brand)    

    def set_sex(self, sex):
        self._sex = sex

    def get_sex(self):
        return self._sex    

    sex = property(get_sex, set_sex)

    def set_rental_price(self, rental_price):
        self._rental_price = rental_price

    def get_rental_price(self):
        return self._rental_price

    rental_price = property(get_rental_price, set_rental_price)
    
bicycle_list = []

def diplay_bike():
     for bicycle in bicycle_list:
        print("Fiets nummer: {} is {} van het merk {}, het is een {} fiets. De huurprijs bedraagt: €{} per dag.".format(bicycle.get_bike_number(), bicycle.get_bike_type(), bicycle.get_brand(), bicycle.get_sex(), bicycle.get_rental_price()))

def main():
    # bike1 = Bicycle(1,"Electrisch", "Gazelle", "Heren", 25)
    # bike2 = Bicycle(2, "Manueel", "Giant", "Vrouwen", 15)

    # bicycle_list.append(bike1)
    # bicycle_list.append(bike2)

    bike3 = Bicycle()
    bike3.set_bike_number(3)
    bike3.set_bike_type("Elektrisch")
    bike3.set_brand("Gazelle")
    bike3.set_rental_price(50)
    bike3.set_sex("Dames")

    # bike3.bike_number = 3
    # bike3.bike_type = "Elektrisch"
    # bike3.brand = "Gazelle"
    # bike3.rental_price = 200
    # bike3.sex = "Dames"

    bicycle_list.append(bike3)

    diplay_bike()


if __name__ == '__main__': main()