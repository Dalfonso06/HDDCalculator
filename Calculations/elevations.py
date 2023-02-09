class Elevations:
    """Class to store elevation measurements."""

    def __init__(self, pointA: float, pointD: float, pointBC: float, bottom_of_river: float, water_table: float, highest_elevation: float):
        """Initialization method for measurements.

        Args:
            pointA (float): Pipe entry (bore exit) in feet.
            pointD (float): Pipe exit (bore entry) in feet.
            pointBC (float): Lowest path elevation in feet.
            bottom_of_river (float): Bottom of river length in feet.
            water_table (float): Water table length in feet.
            highest_elevation (float): Highest elevation of ground along lowest path in feet.
        """
        self.pointA = pointA
        self.pointD = pointD
        self.pointBC = pointBC
        self.bottom_of_river = bottom_of_river
        self.water_table = water_table
        self.highest_elevation = highest_elevation