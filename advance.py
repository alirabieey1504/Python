class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print("name is ", self.name)

    def get_age(self):
        print("age is %", self.age)

    def get_info(self):
        print("name is %s and age is %i" % (self.name, self.age))


ali = Person("ali", 22)
ali.get_name()
ali.get_info()

name = input("please enter your name :")
age = int(input("please enter your age :"))
your = Person(name, age)
your.get_info()
