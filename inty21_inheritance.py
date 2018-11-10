class Father:
    def eat(self):
        print("Father can eat.")
class Mother:
    def walk(self):
        print("Walk like mother")
class G_pa:
    def smile(self):
        print("Smile like grandpa.")
class Son(Father,Mother,G_pa):
    # pass
    def walk(self):
        print()

littleSean=Son()
littleSean.eat()
littleSean.walk()
littleSean.smile()
