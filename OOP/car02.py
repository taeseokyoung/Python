class Car:
    def drive(self):
        print("부릉부릉")

    """
    __str__
    print()했을 때 어떤 글을 보여줄 것인지를 정의하는 것이다. 
    기본값 : <__main__.Car object at 0x0000022EC6E91FD0>)
    현재 return의 글자가 출력된다.
    """

    def __str__(self):
        return "나는 꼬마자동차 뿌뿌"

    """
    init은 만들 때 바로 실행된다.
    """

    def __init__(self):
        print("car의 __init__ 실행중입니다.")


my_car = Car()
# print(my_car)
