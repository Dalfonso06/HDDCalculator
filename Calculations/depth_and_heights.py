import elevations

class DepthAndHeights:
    """Depth and Heights Section 2.5."""

    def __init__(self, elevations: elevations.Elevations, outside_diameter: float):
        """Create an instance of the elevations class to use in H calculations.

        Args:
            elevations (elevations.Elevations): Elevation measurements.
            outside_diameter (float): Outside diameter in inches
        """
        self.elevations = elevations
        self.outside_diameter = outside_diameter

    def hpoint_a(self):
        """Calculate the average depth of a path at pipe entry.

        Returns:
            float: Average depth of a path at pipe entry in feet.
        """
        conversion = self.outside_diameter / 24
        return (self.elevations.pointA - self.elevations.pointBC - conversion)

    def hpoint_b(self):
        """Calculate the average depth of path at pipe exit.

        Returns:
            float: Average depth of path at pipe exit in feet.
        """
        conversion = self.outside_diameter / 24
        return (self.elevations.pointD - self.elevations.pointBC - conversion)

    def hc_min(self):
        """Calculate the minimum depth of cover.

        Returns:
            float: Minimum depth of cover in feet.
        """
        conversion = self.outside_diameter / 24
        return (self.elevations.bottom_of_river - self.elevations.pointBC - conversion)

    def hc_max(self):
        """Calculate the maximum depth of cover.

        Returns:
            float: Maximum depth of cover in feet.
        """
        conversion = self.outside_diameter / 24
        return (self.elevations.highest_elevation - self.elevations.pointBC - conversion)

    def hw(self):
        """Calculate height of water over path.

        Returns:
            float: Height of water over path in feet
        """
        conversion = self.outside_diameter / 24
        return (self.elevations.water_table - self.elevations.pointBC - conversion)
    
