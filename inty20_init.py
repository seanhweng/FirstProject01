
class Workers:
#     name="Bob"
#     age=22
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def walk(self):
        print(self.name,"can walk.")
        print(self.name,"is",self.age)

# worker1=Workers()
# worker1.walk()

w1=Workers("James",15)
w1.walk()