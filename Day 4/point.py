class Point:
    """
    Represents a 2D point with x and y coordinates.

    This class allows you to create and work with points in a 2D space.
    Points can be compared for equality using the '==' operator.

    Attributes:
        x (float or int): The x-coordinate of the point.
        y (float or int): The y-coordinate of the point.

    Methods:
        __init__(self, x, y):
            Initializes a new Point object with the specified x and y coordinates.

        __eq__(self, other):
            Compares this Point object with another Point for equality.
            Two points are considered equal if their x and y coordinates match.

    Example:
        p1 = Point(1, 2)
        p2 = Point(1, 2)
        if p1 == p2:
            print("p1 and p2 are equal.")
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
