"""
상속
"""


# 슈퍼, 부모 클래스
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("이 동물은 이런 소리를 내요")


# 서브, 자식 클래스
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        # 부모클래스에서 정의된 init함수를 실행할 때 name, age를 실행한다. 부모의 init과 자식의 init이 둘 다 같이 실행된다.
        self.breed = breed

    def speak(self):
        print("멍멍!")


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("냐앙~")


"""
다형성 : speak() 메서드
메소드 이름이 똑같지만 각 class에서 하는 일은 다르다.
상속 받아서 오버라이딩 한 후 다르게 동작하게 된다.
코드의 가독성과 유지보수성을 높여준다.
"""

chanel = Dog("샤넬", 12, "말티즈")
chanel.speak()  # 멍멍!

dandelion = Cat("들레", 1, "치즈")
dandelion.speak()  # 냐앙~
