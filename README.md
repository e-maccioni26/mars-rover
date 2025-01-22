### Name : Maccioni Elone, Groupe 02 Master Dev Full Stack.

# Mars Rover Simulation

This project is a simulation of NASA's Mars Rovers navigating a rectangular plateau. Each rover follows a set of instructions to explore the terrain, and the final positions and orientations of the rovers are displayed.

## Features

- **Grid-based plateau navigation**: The plateau is defined as a rectangular grid.
- **Rover movement**: Rovers can move forward and rotate 90 degrees left or right.
- **Custom input**: Users can define the plateau size, rover positions, and movement instructions.
- **Sequential execution**: Rovers execute instructions one at a time.
  

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/e-maccioni26/mars-rover.git

2. Navigate to the project directory:
   ```bash
   cd mars-rover

3. Install any dependencies (if required):
   ```bash
   pip3 install -r requirements.txt

------------------------------------------------------------

# Running the Application

1. Navigate to the src directory:
   ```bash
   cd src

2. Run the main script:
   ```bash
   python3 main.py

3. Follow the prompts (Example Input 👇🏼)
   ```bash
   Enter plateau size (e.g., 5 5): 5 5
   Enter rover position (e.g., 1 2 N) or 'stop': 1 2 N
   Enter instructions (e.g., LMLMLMLMM): LMLMLMLMM
   Enter rover position (e.g., 1 2 N) or 'stop': 3 3 E
   Enter instructions (e.g., LMLMLMLMM): MMRMMRMRRM
   Enter rover position (e.g., 1 2 N) or 'stop': stop

## Example Output
   ```bash
   Final positions:
   1 3 N
   5 1 E
