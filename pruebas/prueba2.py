from multiprocessing import *

def suma(num1, num2):
    res = num1+num2
    print ("Suma igual a", res)

def hello(name):
    print("Hola", name)


if __name__ == "__main__":
    p1 = Process(target=suma, args=(3,5))
    p2 = Process(target=hello, args=("Manolo",))
    p1.start()
    p2.start()
