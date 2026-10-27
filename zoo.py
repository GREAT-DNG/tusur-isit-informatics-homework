from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight

    @abstractmethod
    def sound(self) -> str: pass

    @abstractmethod
    def food_per_day(self) -> float: pass

    def describe(self) -> str:
        return f"{self.name}: {self.sound()}"

class Lion(Animal):
    def sound(self) -> str:
        return "Р-р-р"

    def food_per_day(self) -> float:
        return self.weight * 0.05

class Parrot(Animal):
    def sound(self) -> str:
        return "Привет!"

    def food_per_day(self) -> float:
        return self.weight * 0.1

class Zoo():
    def __init__(self):
        self.animals = []

    def __len__(self):
        return len(self.animals)

    def add(self, animal):
        if not isinstance(animal, Animal): raise TypeError
        self.animals.append(animal)

    def sounds(self):
        result = []
        for i in self.animals:
            result.append(i.describe())
        return result

    def total_food(self):
        result = 0.0
        for i in self.animals:
            result += i.food_per_day()
        return result
