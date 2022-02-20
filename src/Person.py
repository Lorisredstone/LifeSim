import random

def generate_name():
    return "Tom"+str(random.randint(0,100))

class Person:
    def __init__(self) -> None:
        self.name = generate_name()
        