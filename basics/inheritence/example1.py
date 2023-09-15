# # The above code defines two classes, A and B, where B inherits from A, and demonstrates how to create instances of these
# # classes and call their methods.
# class A:
#     def feature1(self):
#         print("Feature 1")

#     def feature2(self):
#         print("Feature 2")


# class B(A):
#     def feature3(self):
#         print("Feature 3")

#     def feature4(self):
#         print("Feature 4")


# class C(B):
#     def faeture5(self):
#         print("Feature 5")


# a1 = A()
# a1.feature1()
# a1.feature2()


# b1 = B()
# b1.feature3()
# b1.feature4()

# b1.feature1()
# b1.feature2()


# c1 = C()
# c1.feature1()
# c1.faeture5()


# The above code defines two classes, A and B, where B inherits from A, and demonstrates how to create instances of these
# classes and call their methods.
class A:
    def feature1(self):
        print("Feature 1")

    def feature2(self):
        print("Feature 2")


class B:
    def feature3(self):
        print("Feature 3")

    def feature4(self):
        print("Feature 4")


class C(A, B):
    def faeture5(self):
        print("Feature 5")


a1 = A()
a1.feature1()
a1.feature2()


b1 = B()
b1.feature3()
b1.feature4()

# b1.feature1()
# b1.feature2()


c1 = C()
c1.feature1()
c1.faeture5()
