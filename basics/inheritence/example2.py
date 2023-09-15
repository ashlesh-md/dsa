class A:
    def __init__(self) -> None:
        print("Class A init")

    def feature1(self):
        print("Feature 1")

    def feature2(self):
        print("Feature 2")


class B:
    def __init__(self) -> None:
        # super().__init__()
        print("Class B init")

    def feature3(self):
        print("Feature 3")

    def feature4(self):
        print("Feature 4")


class C(A, B):
    def __init__(self) -> None:
        # B().__init__()
        A().__init__()
        # super().__init__()


a1 = A()
a1.feature1()
a1.feature2()


b1 = B()
b1.feature3()
b1.feature4()

c1 = C()
