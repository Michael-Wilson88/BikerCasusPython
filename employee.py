class Employee:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.role = ""
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

    def set_role(self, role):
        self._role = role

    def get_role(self):
        return self._role    

    role = property(get_role, set_role)       

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


employee_list = []


def display_employee():
     for employee in employee_list:
        print("Naam werknemer: {} {}. Rol: {}. Adres: {} {}. Postcode: {} te {}".format(employee.get_first_name(), employee.get_last_name(), employee.get_role(), employee.get_street_name(), employee.get_street_number(), employee.get_zipcode(), employee.get_city()))

def main():
    # employee_list.append(Employee("Rita", "Franklin", "Baliemedewerker", "Kerkstraat", 23, "2010 WR", "Haarlem"))
    # employee_list.append(Employee("Koos", "Spakenbuiger", "Reperateur", "Hoofdstraat", 68, "3876 KS", "Urk"))

    Koos = Employee()
    Koos.set_first_name("Koos")
    Koos.set_last_name("Spakenbuiger")
    Koos.set_role("Reperateur")
    Koos.set_street_name("Hoofdstraat")
    Koos.set_street_number(68)
    Koos.set_zipcode("2436 KL")
    Koos.set_city("Urk")

    employee_list.append(Koos)

    display_employee()

if __name__ == '__main__': main()   