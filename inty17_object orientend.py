# Object oriented
class Worker():
    name = "Sean"
    sex = "male"

    def eat(self):
        print(self.name, "can lift and he is a", self.sex+".")

    @staticmethod
    def talk():
        print("Workers can talk.")


Worker().eat()

worker1=Worker()
worker1.eat()
worker1.talk()


worker2 = Worker()
worker2.talk()

import random

# Furniture = "Table"
# print(Furniture.upper())
