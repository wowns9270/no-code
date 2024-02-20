
# def add (num1, num2):
#     return num1 + num2

# def numPrint(num):
#     print(num)

# # 굳이 함수를 줄이기 위해 두 기능을 합칠 필요는 없다. 

# def addPrint(num1, num2)
#     num = num1 + num2
#     print(num)
#     return num

# -------------------------------------------------------------

class Cat : 
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def eat(self, food):
        pass

    def walk(self):
        pass

    def speak(self):
        pass

# 고양이가 아래 두 동작을 하는건 single responsibility에 맞지 않다.  

    # def print(self):
    #     print(f"age:{self.age} name:{self.name} " )

    # def log(self, logger):
    #     logger.log(f"age:{self.age} name:{self.name} ")
    #     logger.log(datetime.now())

    def repr(self):
        return f"age:{self.age} name:{self.name} "


# 단일 책임. 
kitty = Cat(12, 'jjlee')
print(kitty.repr())
