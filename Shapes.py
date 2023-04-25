import math


class Shape:
    def __init__(self, name):
        self.name = name
        pass


class Point(Shape):
    def __init__(self, coordinates):
        Shape.__init__(self, 'Point')
        self.coord_x, self.coord_y = coordinates
        pass


class Line(Shape):
    """
    always straight lines
    """
    def __init__(self, length, start_coord, end_coord, orientation):
        """
        length, orientation, and start+end coords are redundant
        :param length: length of line
        :param start_coord: start coords of line - north->south, west->east
        :param end_coord: end coords of line - north->south, west->east
        :param orientation: line orientation - angle between north-south axis
        """
        Shape.__init__(self, name='Line')
        self.length = length
        self.start_coord_x, self.start_coord_y = start_coord
        self.end_coord_x, self.end_coord_y = end_coord
        self.orientation = orientation
        pass


class Circle(Shape):
    def __init__(self, radius, center_coord):
        """

        :param radius: circle radius
        :param center_coord: (x,y) coordinates for circle centre
        """
        Shape.__init__(self, name='Circle')
        self.center_x, self.center_y = center_coord
        self.radius = radius
        pass

    def area(self):
        return math.pi*self.radius**2

    def perimeter(self):
        return math.pi*self.radius


class Rectangle(Shape):
    """can be square"""
    def __init__(self, length, width, top_left_coord, orientation):
        """

        :param length: length of rectangle
        :param width: width of rectangle
        :param top_left_coord: north-west corner coords
        :param orientation: length orientation - angle between north-south axis
        """
        name = 'Rectangle' if length != width else 'Square'
        Shape.__init__(self, name)
        self.length = length
        self.width = width
        self.top_left_x, self.top_left_y = top_left_coord
        self.orientation = orientation
        pass

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return self.length*2 + self.width*2


class Trapezoid(Shape):

    def __init__(self, width, top_base_length, bottom_base_length, top_left_coord, orientation):
        """

        :param width: separation between top and bottom base
        :param top_base_length: top base length - north->south, west->east
        :param bottom_base_length: bottom base length - north->south, west->east
        :param top_left_coord: north-west corner coords
        :param orientation: height orientation - angle between north-south axis
        """
        Shape.__init__(self, name='Trapezoid')
        self.height = width
        self.small_base = top_base_length
        self.big_base = bottom_base_length
        self.top_left_x, self.top_left_y = top_left_coord
        self.orientation = orientation

    def area(self):
        return (self.small_base*self.big_base)/2*self.height

    def perimeter(self):
        return (self.big_base - self.small_base)*self.height/2 + self.small_base*2 + self.big_base*2
