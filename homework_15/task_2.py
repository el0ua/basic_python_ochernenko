class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def point_position_checker(self, point):
        return (point.x - self.x) ** 2 + (point.y - self.y) ** 2 <= self.radius ** 2


def point_input():
    x = float(input("Enter the x-coordinate of the point: "))
    y = float(input("Enter the y-coordinate of the point: "))
    return Point(x, y)


def circle_input():
    x = float(input("Enter the x-coordinate of the center of the circle: "))
    y = float(input("Enter the y-coordinate of the center of the circle: "))
    radius = float(input("Enter the radius of the circle: "))
    return Circle(x, y, radius)


def main():
    print("Enter the details of the circle:")
    circle = circle_input()
    print("Enter the details of the point:")
    point = point_input()

    is_inside = circle.point_position_checker(point)
    if is_inside:
        print("The point is inside the circle.")
    else:
        print("The point is not inside the circle.")


if __name__ == '__main__':
    main()