from math import sqrt
class Vector3D:
    def __init__(self,x = 0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z

    def __lt__(self,other):
        m = sqrt(self.x**2+self.y**2+self.z**2)
        n = sqrt(other.x**2+other.y**2+other.z**2)
        if m<n:
            return True
        else:
            return False
        
    def __gt__(self,other):
        m = sqrt(self.x**2+self.y**2+self.z**2)
        n = sqrt(other.x**2+other.y**2+other.z**2)
        print(m,n)
        if m>n:
            return True
        else:
            return False