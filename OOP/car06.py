class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.speed = 0

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 10

    def get_speed(self, unit="mph"):
        if unit == "mph":
            return self.speed
        elif unit == "kmh":
            return round(self.speed * 1.60934, 2)
        else:
            raise ValueError("Invalid unit")

    def set_speed(self, value):
        value = int(
            value
        )  # 만약 string으로 들어와도 int로 받을 수 있도록 하거나, error 처리를 해줄 수도 있을 것이다.
        self.speed = value


car = Car("볼보", "white")
car.accelerate()

print(car.speed)
print(car.get_speed("mph"))  # 10
print(car.get_speed("kmh"))  # 16.09
car.set_speed(100)  # car.speed = '100' 하는 것 보다 안전하다.
print(car.get_speed())  # 100

"""
getter와 setter
외부에서 직접 접근하지 못하도록 하는 메서드
"""
