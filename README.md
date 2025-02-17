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
   👉 Entrez la taille du plateau (ex : 5 5) : 5 5
   ✅ Plateau de taille 5x5 créé avec succès.
   
   📍 Position initiale du Rover 1 (ex : 1 2 N) : 1 2 N
   📜 Instructions pour le Rover 1 (ex : LMLMLMLMM) : LMLMLMLMM
   ✅ Rover 1 déplacé avec succès à la position : 1 3 N
   
   📍 Position initiale du Rover 2 (ex : 3 3 E) : 3 3 E
   📜 Instructions pour le Rover 2 (ex : MMRMMRMRRM) : MMRMMRMRRM
   ✅ Rover 2 déplacé avec succès à la position : 5 1 E
   
   📍 Entrez la position initiale du rover 3 (ou 'stop' pour terminer) : stop
   
  etc ...

## Example Output
   ```bash
   🌟 Résultat final :
   Rover 1 : 1 3 N
   Rover 2 : 5 1 E
