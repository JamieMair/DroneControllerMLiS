import numpy as np
from typing import Tuple


class Drone():


    def __init__(self):
        self.x = 0
        self.y = 0
        self.t = 0
        self.thrust_left = 0.5
        self.thrust_right = 0.5
        self.velocity_y = 0
        self.velocity_x = 0
        self.velocity_drag = 3.0
        self.pitch = 0
        self.pitch_velocity = 0
        self.pitch_drag_constant = 0.3
        self.target_coordinates = []
        self.max_thrust = 1.0
        self.turning_constant = 1.0
        self.mass = 1.0
        self.g = -1.0/self.mass
        self.t = 0
        self.game_target_size = 0.1

        self.has_reached_target_last_update = False
    def add_target_coordinate(self, point: Tuple[float, float]):
        self.target_coordinates.append(point)

    
    def get_pitch(self):
        return self.pitch

    def set_thrust(self, thrust_percentage: Tuple[float, float]):
        assert(len(thrust_percentage) == 2)
        assert(0<=thrust_percentage[0]<=1)
        assert(0<=thrust_percentage[1]<=1)
        self.thrust_left = thrust_percentage[0] * self.max_thrust
        self.thrust_right = thrust_percentage[1] * self.max_thrust

    
    def get_next_target(self) -> Tuple[float, float]:
        return (0,0) if len(self.target_coordinates)==0 else self.target_coordinates[0]


    def step_simulation(self, delta_time: float):
        # Set the target reached flag to false
        self.has_reached_target_last_update = False
        self.t += delta_time

        thrust_vec_x = np.sin(self.pitch)
        thrust_vec_y = np.cos(self.pitch)
        velocity_size = np.sqrt(self.velocity_x*self.velocity_x+self.velocity_y*self.velocity_y)

        total_thrust = self.thrust_left+self.thrust_right
        total_torque = (self.thrust_left - self.thrust_right)*self.turning_constant

        acc_y_h = (total_thrust * thrust_vec_y) / self.mass + self.g - velocity_size*thrust_vec_y
        acc_x_h = (total_thrust * thrust_vec_x) / self.mass - velocity_size*thrust_vec_x
        theta_acc_h = (total_torque) / self.mass - self.pitch_drag_constant * np.abs(self.pitch_velocity)

        vel_x_h = self.velocity_x + acc_x_h * delta_time/2
        vel_y_h = self.velocity_y + acc_y_h * delta_time/2
        theta_vel_h = self.pitch_velocity + theta_acc_h * delta_time / 2

        x_h = self.x + vel_x_h * delta_time / 2
        y_h = self.y + vel_y_h * delta_time / 2
        theta_h = self.pitch + theta_vel_h * delta_time / 2

        thrust_vec_x = np.sin(theta_h)
        thrust_vec_y = np.cos(theta_h)
        velocity_size = np.sqrt(vel_x_h*vel_x_h+vel_y_h*vel_y_h)

        acc_y_f = (total_thrust * thrust_vec_y) / self.mass + self.g - velocity_size*thrust_vec_y
        acc_x_f = (total_thrust * thrust_vec_x) / self.mass - velocity_size*thrust_vec_x
        theta_acc_f = (total_torque) / self.mass - self.pitch_drag_constant * np.abs(self.pitch_velocity)

        self.velocity_x = vel_x_h + acc_x_f * delta_time/2
        self.velocity_y = vel_y_h + acc_y_f * delta_time/2
        self.pitch_velocity = theta_vel_h + theta_acc_f * delta_time / 2

        self.x = x_h + self.velocity_x * delta_time / 2
        self.y = y_h + self.velocity_y * delta_time / 2
        self.pitch = theta_h + self.pitch_velocity * delta_time / 2

        # Updates the target list
        target_point = self.get_next_target()
        distance_x = self.x - target_point[0]
        distance_y = self.y - target_point[1]
        distance_to_target = np.sqrt(distance_x*distance_x+distance_y*distance_y)
        if distance_to_target < self.game_target_size:
            if len(self.target_coordinates) > 0:
                self.target_coordinates.pop(0)
                self.has_reached_target_last_update = True






    
