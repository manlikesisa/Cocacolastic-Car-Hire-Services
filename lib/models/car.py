class Car:
    def __init__(self, id, make, model, year, is_available=True):
        self.id = id
        self.make = make
        self.model = model
        self.year = year
        self.is_available = is_available

    def __str__(self):
        status = 'Available' if self.is_available else 'Hired'
        return f"<Car {self.id}: {self.make} {self.model} ({self.year}) - {status}>"
