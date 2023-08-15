class Car:
    color = "red"

    def drive(self):
        print("부릉부릉")


# Car의 인스턴스
my_car = Car()

# 속성
print(my_car.color)

# 메소드
my_car.drive()

print(type(my_car))
# <class(의 클래스) '__main__(우리가 위치한 파일).Car(Car이다)'>

print(dir(my_car))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'color', 'drive']
