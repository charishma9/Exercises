class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    # Method to subtract 2 Vectors
    def __mul__(self, other):
        if isinstance(other, Vector3D):
            return self.x * other.x+ self.y * other.y + self.z*other.z # Point * Point
        return Vector3D(self.x * other, self.y * other ,self.z*other)

    def __rmul__(self, other):
        return Vector3D(self.x * other, self.y * other , self.z * other) 