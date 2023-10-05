class vehicles:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

# Create an instance of the vehicles class
vehicle1 = vehicles("toyota", "TX", "silver")

# Access attributes of the instance
print(vehicle1.make)
print(vehicle1.model)
print(vehicle1.color)

def saycar(self):
    print("your car is a", self.make, self.model, "and it is of color")
    self.colour