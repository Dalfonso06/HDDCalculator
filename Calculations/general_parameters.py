import math
import pipe_parameters

class GeneralParameters:

    DENSITY_OF_WATER = 1000/16.0184634

    def empty_pipe_weight(self, outside_diameter: float, inside_diameter: float, specific_HDPE_gravity: float):
        """Calculate weight of the empty pipe.

        Args:
            outside_diameter (float): Outside diameter of pipe in inches.
            inside_diameter (float): Inside diameter of pipe in inches.
            specific_HDPE_gravity (float): Specific gravity of HDPE in DI.

        Returns:
            float: Weight of empty pipe in Lbs/foot.
        """
        current_pipe = pipe_parameters.PipeParameters()
        pipe_cross_section = current_pipe.ACS(outside_diameter, inside_diameter)
        return ((pipe_cross_section / 144) * specific_HDPE_gravity * self.DENSITY_OF_WATER)

    def filled_pipe_weight(self, empty_pipe: float, to_fill: float, Yib: float, inside_diameter: float):
        """Calculate weight of pipe filled with fluid.

        Args:
            empty_pipe (float): Weight of empty pipe using empty_pipe_weight() in Lbs/foot.
            to_fill (float): Pipe section to fill with fluid in DI.
            Yib (float): Specific gravity of ballast fluid during tie-in in DI.
            inside_diameter (float): Inside diameter of pipe in inches.

        Returns:
            float: The weight of pipe filled with fluid in Lbs/foot
        """
        current_pipe = pipe_parameters.PipeParameters()
        pipe_cross_section = current_pipe.AIS(inside_diameter)
        return (empty_pipe + (to_fill * Yib * self.DENSITY_OF_WATER) * (pipe_cross_section / 144))

    def upward_buoyant_force(self, filled_pipe: float, outside_diameter: float, Yb: float):
        """Calculate the net upward buoyant force on pipe.

        Args:
            filled_pipe (float): The weight of the filled pipe using filled_pipe_weight().
            outside_diameter (float): Outside diameter of the pipe in inches
            Yb (float): Specific gravity of mud slurry in DI

        Returns:
            float: Net upward buoyant force on pipe in Lbs/foot
        """
        pi = math.pi
        return (pi * math.pow(outside_diameter/12, 2) / 4) * (self.DENSITY_OF_WATER * Yb) - filled_pipe

    