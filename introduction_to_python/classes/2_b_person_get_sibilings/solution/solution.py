class person:

    def __init__(self,name,age,spouse = None,children = []):
        self.name = name
        self.age = age
        self.spouse = spouse
        self.children = children


class child(person):
    def __init__(self,name,age,spouse = None,children = [],parents =[]):
        person.__init__(self,name,age,spouse,children)
        self.parents = parents

    def __str__(self):
        return str(self.parents)

    def  get_siblings(self):
        sib = []
        par = self.parents
        for i in par:
            fa =i.children
            ma =i.children 
            sib.append(fa)
            sib.append(ma)

                



