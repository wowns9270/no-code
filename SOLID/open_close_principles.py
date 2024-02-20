# class Animal:
#     def __init__(self, a_type):
#         self.a_type = a_type


# def hey(animal:Animal):
#     if animal.a_type == 'Cat':
#         print('Meow')
#     elif animal.a_type == 'Dog':
#         print('bark')
#     else :
#         raise Error('wrong a_type')

# kitty = Animal('Cat')
# bingo = Animal('Dog')

# animal에 cow, sheet가 추가된다면? 
# 추가된 type에 대해서 hey 함수에서 추가 수정이 필요함.
# 확장에 대한 제약이 있는 좋지 않는 구조.

# hey(kitty)
# hey(bingo)

# --------------------------------------------------------------

class Animal:
    def speak(self):
        pass
    
class Cat(Animal) :
    def speak(self):
        print('moew') 

class Dog(Animal) :
    def speak(self):
        print('bark')

# Sheep에 대한 type이 추가되더라도,
# type에 대한 확장은 자유롭고, hey에 대해서는 닫혀있는 구조를 만들수 있다.

class Sheep(Animal):
    def speak(self):
        print('moo')

def hey(animal:Animal):
    animal.speak()

kitty = Cat()
bingo = Dog()
sheep = Sheep()

hey(kitty)
hey(bingo)
hey(sheep)












