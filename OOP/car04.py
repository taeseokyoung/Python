class Car:
    def __init__(self, model, color, speed):
        self.model = model
        self.color = color
        self.speed = speed

    def accelerate(self, up):
        self.speed += up

    def brake(self, down):
        self.speed -= down

    def get_speed(self):
        print(self.speed)


my_car = Car("볼보", "black", 100)
print(my_car)  # <__main__.Car object at 0x000002123C244FD0>
print(my_car.model)  # 볼보
print(my_car.color)  # black
print(my_car.speed)  # 100

my_car.accelerate(100)
my_car.get_speed()

my_car.brake(50)
my_car.get_speed()
