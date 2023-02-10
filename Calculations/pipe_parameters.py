import math

class PipeParameters:
    """Class for Pipe Parameters Section 1"""

    # Minimum wall thickness (1.3)
    def t(self, outside_diameter, dimension_ratio):
        """Calculate minimum wall thickness.

        Args:
            outside_diameter (float): Outside diameter of the pipe in inches
            dimension_ratio (float): Dimension ratio of the pipe in DI

        Returns:
            float: The minimum wall thickness in square inches.
        """
        return outside_diameter / dimension_ratio

    # Pipe External Area (1.5.1)
    def AOS(self, outside_diameter):
        """Calculate the pipe external area.

        Args:
            outside_diameter (float): Outside Diameter of pipe in inches

        Returns:
            float: Pipe external area in square inches.
        """
        pi = math.pi
        return pi * (outside_diameter**2) / 4

    # Pipe Internal Area (1.5.2)
    def AIS(self, inside_diameter):
        """Calculate the pipe internal area.

        Args:
            inside_diameter (float): Inside Diameter of pipe in inches.

        Returns:
            float: Pipe internal area in square inches.
        """
        pi = math.pi
        return pi * (inside_diameter**2) / 4

    # Pipe Cross-section Area (1.5.3)
    def ACS(self, outside_diameter, inside_diameter):
        """Calculate the pipe cross-section area.

        Args:
            outside_diameter (float): Outside diameter of pipe
            inside_diameter (float): Inside diameter of pipe

        Returns:
            float: Pipe cross-section area in square insches.
        """
        return self.AOS(outside_diameter) - self.AIS(inside_diameter)

    # Allowable Tensile Load
    def ATL(self, safe_pull_stress, outside_diameter, inside_diameter):
        """Calculate the allowable tensile load.

        Args:
            safe_pull_stress (_type_): Safe pull stress in psi
            outside_diameter (_type_): Outside diameter of pipe in inches
            inside_diameter (_type_): Inside diameter of pipe in inches

        Returns:
            float: Allowable tensile load in pound force (Lbf)
        """
        return safe_pull_stress * self.ACS(outside_diameter, inside_diameter)

