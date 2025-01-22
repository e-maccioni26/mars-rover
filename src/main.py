from rover import Rover
from plateau import Plateau
import time

def main():
    print("🌌 Bienvenue dans le Simulateur de Rover Martien ! 🚀")
    print("Vous allez explorer un plateau martien avec plusieurs rovers.")
    print("Pour commencer, définissez la taille du plateau.")
    print("Astuce : Entrez 'stop' à tout moment pour terminer l'ajout des rovers.\n")

    plateau_size = input("👉 Entrez la taille du plateau (ex : 5 5) : ")
    width, height = map(int, plateau_size.split())
    plateau = Plateau(width, height)
    print(f"✅ Plateau de taille {width}x{height} créé avec succès.\n")

    rovers = []
    rover_count = 0 

    while True:
        rover_count += 1
        position = input(f"📍 Entrez la position initiale du Rover {rover_count} (ex : 1 2 N) ou 'stop' pour terminer : ")
        if position.lower() == 'stop':
            rover_count -= 1 
            break
        try:
            x, y, direction = position.split()
            x, y = int(x), int(y)
        except ValueError:
            print("❌ Format incorrect ! Veuillez entrer la position sous la forme : 'x y direction'.")
            rover_count -= 1 
            continue

        if not (0 <= x <= width and 0 <= y <= height):
            print(f"❌ Les coordonnées ({x}, {y}) sont hors des limites du plateau ({width}, {height}). Réessayez.")
            rover_count -= 1 
            continue

        instructions = input(f"📜 Entrez les instructions pour le Rover {rover_count} (ex : LMLMLMLMM) : ").upper()
        if not all(c in "LRM" for c in instructions):
            print("❌ Les instructions ne doivent contenir que les lettres 'L', 'R' ou 'M'. Réessayez.")
            rover_count -= 1  
            continue

        rover = Rover(x, y, direction, plateau)
        print(f"🚀 Déplacement du Rover {rover_count} en cours...")
        time.sleep(1)  
        rover.execute_instructions(instructions)
        rovers.append(rover)
        print(f"✅ Rover {rover_count} déplacé avec succès à la position : {rover.x} {rover.y} {rover.direction}\n")

    print("\n🌟 Résultat final :")
    for idx, rover in enumerate(rovers, start=1):
        print(f"Rover {idx} : {rover.x} {rover.y} {rover.direction}")

    print("\nMerci d'avoir utilisé le Simulateur de Rover Martien ! 🛸👽")

if __name__ == "__main__":
    main()
