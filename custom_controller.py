from flight_controller import FlightController
from drone import Drone
from typing import Tuple

class CustomController(FlightController):

    def __init__(self):
        pass
    def train(self):
        pass    
    def get_thrusts(self, drone: Drone) -> Tuple[float, float]:
        return (0.5, 0.5) # Replace this with your custom algorithm
    def load(self):
        pass
    def save(self):
        pass