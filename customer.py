class Customer():
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.street_name = ""
        self.street_number = 0
        self.zipcode = ""
        self.city = ""


    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_first_name(self):
        return self._first_name

    first_name = property(get_first_name, set_first_name)

    def set_last_name(self, last_name):
        self._last_name = last_name

    def get_last_name(self):
        return self._last_name

    last_name = property(get_last_name, set_last_name)

    def set_street_name(self, street_name):
        self._street_name = street_name

    def get_street_name(self):
        return self._street_name

    street_name = property(get_street_name, set_street_name)

    def set_street_number(self, street_number):
        self._street_number = street_number

    def get_street_number(self):
        return self._street_number

    street_number = property(get_street_number, set_street_number)

    def set_zipcode(self, zipcode):
        self._zipcode = zipcode

    def get_zipcode(self):
        return self._zipcode   

    zipcode = property(get_zipcode, set_zipcode)     

    def set_city(self, city):
        self._city = city

    def get_city(self):
        return self._city    

    city = property(get_city, set_city)    

customer_list = []  

def display_customer():
    for customer in customer_list:
         print("Naam klant: {} {}. Adres: {} {}, Postcode: {} te {}".format(customer.get_first_name(), customer.get_last_name(), customer.get_street_name(), customer.get_street_number(), customer.get_zipcode(), customer.get_city()))

def main():

    # customer_list.append(Customer("Barry", "Pompe", "Harklaan", 124, "4523 KI", "Maastricht"))
    # customer_list.append(Customer("Henk", "de Vries", "Fietsweg", 22, "6969 SX", "Amsterdam"))

    Wilhelm = Customer()
    Wilhelm.set_first_name("Wilhelm")
    Wilhelm.set_last_name("De Ridder")
    Wilhelm.set_street_name("Kerkstraat")
    Wilhelm.set_street_number(12)
    Wilhelm.set_zipcode("2436 KL")
    Wilhelm.set_city("Maastricht")

    customer_list.append(Wilhelm)

    display_customer()

if __name__ == '__main__': main()    