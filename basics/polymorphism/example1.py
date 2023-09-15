# Duck Typing
x = 5
x = "Ash"


class MyIde:
    def excecute(self):
        print("Excecuting my code")


class Vscode:
    def excecute(self):
        print("Excecuting my code in VsCodex")


class Runner:
    def run(self, ide):
        ide.excecute()


Runner().run(MyIde())
Runner().run(Vscode())


# Operator Overloading
class Mark:
    def __init__(self, m1, m2) -> None:
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        return Mark(self.m1 + other.m1, self.m2 + other.m2)

    def __gt__(self, other):
        return self if self.m1 + self.m2 > other.m1 + other.m2 else other


mark1 = Mark(10, 20)
mark2 = Mark(30, 40)
m3 = mark1 + mark2
print(m3.m1, m3.m2)

print((mark1 > mark2).m1)


# Method Overloading
class Mark:
    def __init__(self, m1, m2) -> None:
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=0, b=0, c=0):
        return a + b + c


mark1 = Mark(10, 20)
print(mark1.sum(1))
print(mark1.sum(1, 2))
print(mark1.sum(1, 2, 3))

# Method Overriding


class A:
    def show(self):
        print("Showing A")


class B(A):
    def show(self):
        print("Showing B")


A().show()
B().show()