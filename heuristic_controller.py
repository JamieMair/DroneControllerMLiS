import numpy as np
from flight_controller import FlightController
from drone import Drone
from typing import Tuple

class HeuristicController(FlightController):


    def __init__(self):
        """Creates a heuristic flight controller with some specified parameters

        """

        self.ky = 1.0
        self.kx = 0.5
        self.abs_pitch_delta = 0.1
        self.abs_thrust_delta = 0.3

    def get_max_simulation_steps(self):
            return 3000 # You can alter the amount of steps you want your program to run for here


    def get_thrusts(self, drone: Drone) -> Tuple[float, float]:
        """Takes a given drone object, containing information about its current state
        and calculates a pair of thrust values for the left and right propellers.

        Args:
            drone (Drone): The drone object containing the information about the drones state.

        Returns:
            Tuple[float, float]: A pair of floating point values which respectively represent the thrust of the left and right propellers, must be between 0 and 1 inclusive.
        """

        target_point = drone.get_next_target()
        dx = target_point[0] - drone.x
        dy = target_point[1] - drone.y

        thrust_adj = np.clip(dy * self.ky, -self.abs_thrust_delta, self.abs_thrust_delta)
        target_pitch = np.clip(dx * self.kx, -self.abs_pitch_delta, self.abs_pitch_delta)
        delta_pitch = target_pitch-drone.pitch

        thrust_left = np.clip(0.5 + thrust_adj + delta_pitch, 0.0, 1.0)
        thrust_right = np.clip(0.5 + thrust_adj - delta_pitch, 0.0, 1.0)

        # The default controller sets each propeller to a value of 0.5 0.5 to stay stationary.
        return (thrust_left, thrust_right)

    def train(self):
        """A self contained method designed to train parameters created in the initialiser.
        """
        # --- Code snipped provided for guidance only --- #
        # for n in range(epochs):
        #     # 1) modify parameters
            
        #     # 2) create a new drone simulation
        #     drone = self.init_drone()
        #     # 3) run simulation
        #     for t in range(self.get_max_simulation_steps()):
        #         drone.set_thrust(self.get_thrusts(drone))
        #         drone.step_simulation(self.get_time_interval())
        #     # 4) measure change in quality

        #     # 5) update parameters according to algorithm

        pass

    def load(self):
        """Load the parameters of this flight controller from disk.
        """
        try:
            parameter_array = np.load('heuristic_controller_parameters.npy')
            self.ky = parameter_array[0]
            self.kx = parameter_array[1]
            self.abs_pitch_delta = parameter_array[2]
            self.abs_thrust_delta = parameter_array[3]
        except:
            print("Could not load parameters, sticking with default parameters.")

    def save(self):
        """Save the parameters of this flight controller to disk.
        """
        parameter_array = np.array([self.ky, self.kx, self.abs_pitch_delta, self.abs_thrust_delta])
        np.save('heuristic_controller_parameters.npy', parameter_array)
        