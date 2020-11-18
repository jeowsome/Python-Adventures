class Sphere:
    PI = 3.1415
    # finish class Sphere here

    def __init__(self, radius):
        self.radius = radius
        self.volume = 1.33333333333 * (Sphere.PI * (radius ** 3))