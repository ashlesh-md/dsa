class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno, self.lap.brand)

    class Laptop:
        def __init__(self):
            self.brand = "MacBook"

        def show(self):
            print(self.brand)


s1 = Student("Ash", 1)
s1.lap.brand = "Macbook Air"
s1.lap.show()
s1.show()