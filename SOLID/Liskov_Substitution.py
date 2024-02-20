class Cat:
    def speak(self) :
        print("moew")



class BlackCat(Cat) :
    def speak(self) :
        print("black moew")



def speak(cat:Cat):
    cat.speak()


class Fish(Cat):
    def speak(self):
        raise Exception("fish cannot speak")


cat = Cat()
speak(cat)

blcat = BlackCat()
speak(blcat)

# fish = Fish()
# speak(fish) 

#  fish와 같은 잘못된 설계로 인한 리스코프 치환법칙 오류
#  애초에 설계를 잘했어야한다..? 

