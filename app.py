def hello():
    print('Hello World!')


hello()


def hello2(x):
    print('Hello ' + str(x))


hello2(input("What's your name==>"))


def hello3(x):
    print(f"Hi {x}")


hello3(input("What's your name?"))


def double(number):
    return number * 2


print(double(str(input("Input number==>"))))
