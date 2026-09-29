class Vehicle:
    # Constructor --> Automatically invoked when an object is created....
    def __init__(self, color, horsepower=40):
        self.color = color  # -->vehicle1.color=Red
        self.horsepower = horsepower  # -->vehicle1.horsepower=500
    # color,horsepower

    def go_forward(self):
        print(f"Moving forward by 1 block.")

    def go_backwards(self):
        print("Moving backward by 1 block.")

    def printColor(self):
        print(f"Color of the vehicle is :{self.color}")


# object_name=Class_name(arguments)
vehicle1 = Vehicle("Red", 500)
# object    class

print(vehicle1.color)  # Printing attribute directly

vehicle1.go_forward()

vehicle1.go_backwards()  # Printing an attribute using a method
