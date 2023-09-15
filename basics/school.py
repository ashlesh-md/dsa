class School:
    name = "School Name"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        print("Average : ", (self.m1 + self.m2 + self.m3) / 3)

    @staticmethod
    def message():
        print("This is a school")

    @classmethod
    def school(cls):
        print(cls.name)


school1 = School(10, 20, 30)
school1.message()

school1.school()

school1.avg()
