from math import sqrt
class Vector3D:
    def __init__(self,x = 0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z

    def __abs__(self):
        return sqrt(self.x**2+self.y**2+self.z**2)
        