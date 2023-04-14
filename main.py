import math

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def cosine_similarity(self, other):
        dot = self.dot_product(other)
        len1 = self.length()
        len2 = other.length()
        return dot / (len1 * len2)

v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

v3 = v1 + v2
print(v3.x, v3.y, v3.z)  # 5 7 9

v4 = v2 - v1
print(v4.x, v4.y, v4.z)  # 3 3 3

dp = v1.dot_product(v2)
print(dp)  # 32

len1 = v1.length()
print(len1)

cos = v1.cosine_similarity(v2)
print(cos)
