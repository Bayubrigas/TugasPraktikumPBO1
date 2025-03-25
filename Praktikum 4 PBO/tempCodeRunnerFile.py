from abc import ABC, abstractmethod

class Animal(ABC):
  def __init__(self, name, age):
    self.__name = name
    self.__age = age

  @abstractmethod
  def make_sound(self):
    pass

  def get_name(self):
    return self.__name

  def set_name(self, name):
    if not name:
      raise ValueError("Name cannot be empty")
    self.__name = name

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if age <= 0:
      raise ValueError("Age must be greater than zero")
    self.__age = age

class Dog(Animal):
  def make_sound(self):
    return "Woof!"

class Cat(Animal):
  def make_sound(self):
    return "Meow!"

class Bird(Animal):
  def make_sound(self):
    return "Chirp!"

def main():
  try:
    dog = Dog("Buddy", 3)
    cat = Cat("Whiskers", 2)
    bird = Bird("Tweety", 1)

    animals = [dog, cat, bird]

    for animal in animals:
      print(f"{animal.get_name()} says {animal.make_sound()}")

    # Example of error handling
    invalid_animal = Dog("", -1)
  except ValueError as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()