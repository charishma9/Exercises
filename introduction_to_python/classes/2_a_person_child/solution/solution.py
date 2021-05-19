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



jim = person("Jim Brown",45)
suzy = person("Suzy Brown",42)
martha = child("Martha Brown",18,None,[],[jim,suzy])
jim.spouse = suzy
suzy.spouse = jim
suzy.children = [martha]
jim.children = [martha]
print(martha.parents)
