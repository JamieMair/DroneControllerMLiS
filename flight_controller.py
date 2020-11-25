import numpy as np
from drone import Drone
from typing import Tuple


class FlightController():

    @classmethod
    def get_max_simulation_steps(self):
        return 500
    @classmethod
    def get_time_interval(self):
        return 0.01

    @classmethod
    def get_thrusts(self, drone: Drone) -> Tuple[float, float]:
        """Takes a given drone object, containing information about its current state
        and calculates a pair of thrust values for the left and right propellers.

        Args:
            drone (Drone): The drone object containing the information about the drones state.

        Returns:
            Tuple[float, float]: A pair of floating point values which respectively represent the thrust of the left and right propellers, must be between 0 and 1 inclusive.
        """


        # The default controller sets each propeller to a value of 0.5 0.5 to stay stationary.
        return (0.5, 0.5)

    @classmethod
    def train(self):
        pass

    @classmethod
    def init_drone(self) -> Drone:
        """Creates a Drone object initialised with a deterministic set of target coordinates.

        Returns:
            Drone: An initial drone object with some programmed target coordinates.
        """
        drone = Drone()
        drone.add_target_coordinate((0.35, 0.3))
        drone.add_target_coordinate((-0.35, 0.4))
        drone.add_target_coordinate((0.5, -0.4))
        drone.add_target_coordinate((-0.35, 0))
        return drone

    @classmethod
    def load(self):
        """Load the parameters of this flight controller from disk.
        """
        pass

    @classmethod
    def save(self):
        """Save the parameters of this flight controller to disk.
        """
        pass