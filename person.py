class Person:
    def __init__(self, name: str, age: int, height: float):
        self.name = name
        self.age = age
        self.height = height

    def getName(self):
        print(f"getting name {self.name}")
        return self.name

    def setName(self, new_name: str):
        print(f"setting name {new_name}")
        self.name = new_name

    def getAge(self):
        print(f"getting age {self.age}")
        return self.age

    def setAge(self, new_age: int):
        print(f"setting age {new_age}")
        self.age = new_age

    def getHeight(self):
        print(f"getting height {self.height}")
        return self.height

    def setHeight(self, new_height: float):
        print(f"setting height {new_height}")
        self.height = new_height
