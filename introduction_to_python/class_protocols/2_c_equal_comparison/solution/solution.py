class Vector3D:
    def __init__(self,x = 0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self,other):
        if (self.x==other.x)and(self.y==other.y)and(self.z==other.z):
            return True
        else:
            return False