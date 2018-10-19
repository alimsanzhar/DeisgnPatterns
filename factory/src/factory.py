"""
Factory Design Pattern.
"""


class Company(object):

    def factory(type):
        if type == "Google":
            return Google()
        if type == "Apple":
            return Apple()
        raise TypeError("Bad company creation: " + type)

    factory = staticmethod(factory)


class Google(Company):

    def invent(self):
        print("Invent Google Glass")


class Apple(Company):
    def invent(self):
        print("Invent iPhone")


object = Company.factory("G+ASFoogle")
object.invent()
