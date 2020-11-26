# Drone Flight Controller, Project 9 MLiS Part I

To get started you need to first setup python on your computer. The version of python used to develop this initial code is Python 3.6.12. The list of modules installed is given in requirements.txt. The only modules you need to run this code are numpy and pygame. You can also install matplotlib if you intend to plot any figures.

Once you have your environment setup, download this repository as a zip file and extract it to a location on your computer. Once you have done this, navigate to this folder in your given code editor. In order to run the project, simply type "python main.py" into a terminal (making sure you are in the right directory and your python installation is accessible through the terminal). Alternatively you can use an editor like Spyder/PyCharm/VS Code to run this code (recommended).

We have included a file "custom_controller.py" for you to write your own algorithm into. In order to run your own algorithm, you need to change the code at the top of main.py as needed.

## Bug Fixes

1. 26/11/2020: A quick fix to the implementations of the drag dynamics on the drone.

## Possible Extensions

1. Increase the difficulty of the simulation by making sure the drone stays within the boundary of the screen.
2. Decrease the value of the drag constants in drone.py to make the simulation more sensitive.
3. Introduce barriers for the drone to avoid while also hitting the target.
4. Extend the simulation to include two drones which avoid colliding with one another, but which still have to hit targets.
