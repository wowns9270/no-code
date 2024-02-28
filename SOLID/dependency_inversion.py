
# 기존 dependency가 생기는 구조 
# class Cat:
#     def speak(self):
#         print("meow")

# class Dog:
#     def speak(self):
#         print("bark")

# # 여러 동물이 추가될 수 있다.
# class Sheep:
#     pass

# class Cow:
#     pass


# class Zoo:
#     def __init__(self):
#         self.cat = Cat()
#         self.dog = Dog()
#         self.sheep = Sheep()
#         self.cow = Cow()

#---------------------------------------------
        
class Animal:
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print("meow")

class Dog(Animal):
    def speak(self):
        print("bark")

class Zoo:
    def __init__(self):
        self.animals =[]

    def addAnimal(self, animal):
        self.animals.append(animal)

    def speakAll(self):
        for animal in self.animals :
            animal.speak()


zoo = Zoo()
zoo.addAnimal(Cat())
zoo.addAnimal(Dog())
zoo.speakAll();