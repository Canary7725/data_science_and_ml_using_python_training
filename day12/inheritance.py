class Animal:  # Parent Class
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def displayColor(self):
        print(self.color)

    def speak(self):
        print("The sound made by this animal: ")


class Dog(Animal):  # Child class  Dog inherits from Animal Class
    # class child_class_name(parent_class_name):
    def __init__(self, color, size, breed):
        super().__init__(color, size)
        self.breed = breed

    def speak(self):
        super().speak()
        print("Bark!!")


dog_obj = Dog("Red", "small", "Lab")
