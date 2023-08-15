class Car:
    def __init__(self, color):  # 인자, 파라미터
        self.color = color  # 속성


my_car = Car("blue")
your_car = Car("red")

print(my_car.color)  # blue
print(your_car.color)  # red
