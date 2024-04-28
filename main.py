from person import Person

# Creating an instance of the Person class
justin: Person  = Person("Justin", 16, 1.80)

# Accessing attributes of the justin instance
print(justin.name)
print(justin.age)
print(justin.height)

justin.setName("Fleur")

print(justin.getName())