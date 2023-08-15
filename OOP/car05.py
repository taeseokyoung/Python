class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.speed = 0

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 10

    def get_speed(self):
        return self.speed  # attrebute = 속성


car = Car("볼보", "white")
car.accelerate()
# car.accelerate()
# car.accelerate()
# car.brake()
# car.brake()
# car.brake()
print(car.speed)
print(car.get_speed())
"""
car.speed로도 스피드가 나오는데 왜 get_speed()라는 함수를 만들었을까?
method 만들어서 attrebute 값 리턴하는 이유? .speed vs get_speed()
캡슐화(Encapsulation)
- 데이터 + 메서드 = 캡슐화
- 외부에서 직접 접근할 수 없다. 오직 메서드를 통해서만 조작이 가능하다. 이를 통해 보안성, 안정성을 높일 수 있다.
"""
car.speed = "sdifsf"
car.accelerate()  # 오류

car.get_speed()
