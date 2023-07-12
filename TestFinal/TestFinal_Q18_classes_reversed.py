class A:
    def test(self):
        print("test of E called")


class B(A):
    def test(self):
        super().test()  # used to link call the parents’ method
        print("test of B called")


class C(A):
    def test(self):
        super().test()
        print("test of C called")


class D(B, C):
    # positional arguments are flipped compared to the original TestFinal_classes' code to reverse B and C's print
    # statement order in the results
    def test1(self):
        super().test()
        # print("test of D called")


class E(D):
    def test1(self):
        super().test1()
        print("test of A called")


# Driver code to display results
# Create an object of class E
e = E()

# Call the test1() method of class E
e.test1()

"""
Results:
test of E called
test of C called
test of B called
test of A called
"""
