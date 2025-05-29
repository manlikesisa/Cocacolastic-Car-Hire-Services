class customer:
    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"<Customer{self.id}: {self.name} ({self.phone})>"
