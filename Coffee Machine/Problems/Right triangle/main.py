class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here

    def get_area(self):
        if (self.a ** 2) + (self.b ** 2) == (self.c ** 2):
            area = 0.5 * (self.a * self.b)
            print(round(area, 1))
        else:
            print("Not right")


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
triangle = RightTriangle(input_c, input_a, input_b)
triangle.get_area()
