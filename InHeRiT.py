class vehicles:
    def __init__(self, name, max_speed, milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage

class bus(vehicles):
    pass
school_bus = bus("school volvo, 180, 12")
print("vehicle name:", school_bus.name, "speed", school_bus.max_speed, "milage", school_bus.milage)