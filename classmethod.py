class Person:
    def __init__(self,name):
        self.name = name
    @classmethod
    def repeat(self, nam):
        return nam + " " + nam
harry = Person("Harry")
hari = Person.repeat("Hari")
print(hari)
print(harry.name)

