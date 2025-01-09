"""1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты 
(например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, 
которые наследуют от класса `Animal`. Добавьте специфические атрибуты и 
переопределите методы, если требуется (например, различный звук для `make_sound()`).
3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, 
которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
4. Используйте композицию для создания класса `Zoo`, который будет содержать 
информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, 
которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
class """

class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def make_sound(self):
        pass

    def eat(self, food):
        print(f"{self.name} is eating {food}.")

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name, "ZooKeeper")

    def feed_animal(self, animal, food):
        print(f"{self.name} is feeding {animal.name} with {food}.")
        animal.eat(food)

class Veterinar(Employee):
    def __init__(self, name):
        super().__init__(name, "Veterinar")

    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []  
        self.employees = []  
    
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Added animal: {animal.name}, age: {animal.age}, species: {animal.species}")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added employee: {employee.name}, position: {employee.position}")

    def show_all_animals(self):
        print("\nAnimals in the zoo:")
        for animal in self.animals:
            print(f"{animal.name}, age: {animal.age}, species: {animal.species}")

    def show_all_employees(self):
        print("\nEmployees in the zoo:")
        for employee in self.employees:
            print(f"{employee.name}, position: {employee.position}")

    def save_to_file(self, filename):
        """Сохраняет информацию о животных и сотрудниках зоопарка в файл."""
        with open(filename, 'w') as file:
            file.write(f"Zoo: {self.name}\n")
            file.write("\nAnimals:\n")
            for animal in self.animals:
                file.write(f"{animal.name}, age: {animal.age}, species: {animal.species}\n")
            file.write("\nEmployees:\n")
            for employee in self.employees:
                file.write(f"{employee.name}, position: {employee.position}\n")
        print(f"Zoo information saved to {filename}")

bird = Animal("Krig", 5, "Bird")
mammal = Animal("Frosik", 1, "Mammal")
reptile = Animal("Pedro", 45, "Reptile")
zookeeper = ZooKeeper("Sandro")
veterinar = Veterinar("Alehandro")
zoo = Zoo("Trakazoo")

zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)
zoo.add_employee(zookeeper)
zoo.add_employee(veterinar)

zoo.show_all_animals()
zoo.show_all_employees()

zoo.save_to_file("zoo_info.txt")
