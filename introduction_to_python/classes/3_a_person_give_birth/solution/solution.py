class Person:
    def __init__(self,name,age,spouse = None,children = []):
        self.name = name
        self.age = age
        self.spouse = spouse
        self.children = children

    def give_birth(self,name):
        self.children.append(name)
        if self.spouse is not None:
            self.spouse.children.append(name)
            

class Child(Person):
    def __init__(self,name,age,spouse = None,children = [],parents =[]):
        super().__init__(name,age,spouse,children)
        self.parents = parents