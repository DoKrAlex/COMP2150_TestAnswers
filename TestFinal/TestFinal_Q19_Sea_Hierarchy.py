class Ocean:
    def __init__(self):
        pass

    def __str__(self):
        return "From the Ocean the biggest------------------------------"

    def m1(self):
        print("I do m1() from the Ocean")

    def m2(self):
        print("I do m2() from the Ocean")

    def m3(self):
        print("I do m3() from the Ocean")

    def m4(self):
        print("I do m4() from the Ocean")


class Lake(Ocean):
    def __str__(self):
        return "From the Lake after the Ocean------------------------------"

    def m3(self):
        print("I do m3() from the Lake")
        super().m3()


class Bay(Lake):
    def __str__(self):
        return "from Bay after the Lake------------------------------"

    def m1(self):
        print("I do m1() from the Bay")

    def m2(self):
        super().m2()
        print("I do m2() from the Bay")
        super().m2()


class Pond(Bay):
    def __str__(self):
        return "From Pond after the Bay------------------------------"

    def m4(self):
        print("I do m4() from the Pond")


# Driver code to display results
# Create 4 objects each class
ocean1 = Ocean()
lake1 = Lake()
bay1 = Bay()
pond1 = Pond()

object_list = [ocean1, lake1, bay1, pond1]

print(object_list[0])
object_list[0].m1()
object_list[0].m2()
object_list[0].m3()
print(object_list[1])
object_list[1].m1()
object_list[1].m2()
object_list[1].m3()
print(object_list[2])
object_list[2].m1()
object_list[2].m2()
object_list[2].m3()
print(object_list[3])
object_list[3].m1()
object_list[3].m2()
object_list[3].m3()
object_list[3].m4()

"""
Results:
From the Ocean the biggest------------------------------
I do m1() from the Ocean
I do m2() from the Ocean
I do m3() from the Ocean
From the Lake after the Ocean------------------------------
I do m1() from the Ocean
I do m2() from the Ocean
I do m3() from the Lake
I do m3() from the Ocean
from Bay after the Lake------------------------------
I do m1() from the Bay
I do m2() from the Ocean
I do m2() from the Bay
I do m2() from the Ocean
I do m3() from the Lake
I do m3() from the Ocean
From Pond after the Bay------------------------------
I do m1() from the Bay
I do m2() from the Ocean
I do m2() from the Bay
I do m2() from the Ocean
I do m3() from the Lake
I do m3() from the Ocean
I do m4() from the Pond
"""
