from multiprocessing import *

def hello(name):
    print("Hola Eloy")

if __name__ == '__main__':
    p = Process(target=hello, args=("Paco",))
    p.start()
    p.join()
    print("Adiós Eloy")