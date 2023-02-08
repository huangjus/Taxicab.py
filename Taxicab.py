# Author: Justin Huang
# GitHub username: huangjus
# Date: 2/8/23
# Description: The Taxicab class models a cab's location and distance traveled,
# keeping track of the current x-coordinate, y-coordinate, and distance traveled in x_coord, y_coord,
# and odometer data members respectively. It has an __init__ method to initialize the coordinates and odometer,
# three get methods to retrieve the values of each data member, and two methods move_x and move_y to update
# the cab's location and odometer as it moves in the x or y direction.

class Taxicab:

    """
    A class to represent a Taxicab with its current x-coordinate, y-coordinate and odometer reading.
    """

    def __init__(self, x_coord, y_coord):

        """
        Initializes the Taxicab with its starting coordinates and sets the odometer to zero.

        x_coord: The starting x-coordinate of the Taxicab.
        y_coord: The starting y-coordinate of the Taxicab.
        """

        self.x_coord = x_coord
        self.y_coord = y_coord
        self.odometer = 0

    def get_x_coord(self):

        """
        Returns the current x-coordinate of the Taxicab.
        """

        return self.x_coord

    def get_y_coord(self):

        """
        Returns the current y-coordinate of the Taxicab.
        """

        return self.y_coord

    def get_odometer(self):

        """
        Returns the current odometer reading of the Taxicab.
        """

        return self.odometer

    def move_x(self, units):

        """
        Move the Taxicab horizontally by the specified number of units.

        units: The number of units to move the Taxicab horizontally. Can be negative or positive.
        """

        self.x_coord += units
        self.odometer += abs(units)

    def move_y(self, units):

        """
        Move the Taxicab vertically by the specified number of units.

        units: The number of units to move the Taxicab vertically. Can be negative or positive.
        """

        self.y_coord += units
        self.odometer += abs(units)
