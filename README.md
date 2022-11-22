# Drone Flight Controller, Project 9 MLiS Part I

To get started you need to first setup python on your computer. The version of python used to develop this initial code is Python 3.6.12. The list of modules installed is given in requirements.txt. The only modules you need to run this code are `numpy` and `pygame`. You can also install `matplotlib` if you intend to plot any figures.

We recommend that the group doing this project using this repository as a template to create their own and invite all members. Collaboration via Git is the best way to let each member work on the code at the same time. Refer to the Git video on Moodle if you are not familiar with Git or GitHub.

Once everyone has access to the repository on GitHub, clone your repository to your own computer. You can use [GitHub Desktop](https://desktop.github.com/) to make this very easy.

## Installing Python packages

Once you have cloned the repository, open up the folder in your code editor. We recommend you to use [VS Code](https://code.visualstudio.com/). Open the folder where you downloaded the repository. Now, in VS Code, open a terminal by choosing `Terminal -> New Terminal`. This should open in the root folder of the repository. From here, install the dependencies with the command:
```sh
pip install -r requirements.txt
```

## Running the code

In order to run the code, open up a terminal and run
```sh
python main.py
```
You can also run this in the normal way supported by your IDE.

In order to run your own algorithm with the visualisation, you need to change the code at the top of `main.py`, which is detailed in the comments.

## Task

We have included a file `custom_controller.py` for you to write your own custom controller. You can also create any new files you need for scripts in order to train your controller. You can simulate your own environments and even change the way in which targets are spawned in order to more effectively train your agent. An example of the code needed to run your controller is given below:

```python
# Number of time steps
max_time = 1000
# Create the drone
drone = controller.init_drone()
for i in range(max_time):
    # Controller decides on an action
    action = controller.get_thrusts(drone)
    # Apply the action to the environment
    drone.set_thrust(action)
    # Update the simulation
    drone.step_simulation(delta_time)
    # TODO: Add in any code for calculating a reward
```

## Bug Fixes

1. 26/11/2020: A quick fix to the implementations of the drag dynamics on the drone.

## Possible Extensions

1. Increase the difficulty of the simulation by making sure the drone stays within the boundary of the screen.
2. Decrease the value of the drag constants in drone.py to make the simulation more sensitive.
3. Introduce barriers for the drone to avoid while also hitting the target.
4. Extend the simulation to include two drones which avoid colliding with one another, but which still have to hit targets.
