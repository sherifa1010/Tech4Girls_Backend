class car:
    def __init__(self, make, model, year):
        """initializing the instance variables."""
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        """print car's details"""
        print(f"car make: {self.make}")
        print(f"car model: {self.model}")
        print(f"car year: {self.year}") 
my_car = car("benz" , "lexuxe", 2025)
my_car.display_info()