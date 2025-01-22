from typing import List
from rover import Rover
from plateau import Plateau
import time
from colorama import init, Fore, Back, Style

init(autoreset=True)  

def display_plateau(plateau: Plateau, rovers: List[Rover]) -> None:
    """Affiche une représentation visuelle du plateau avec les rovers."""
    print("\n📍 Légende :")
    print(f"{Fore.GREEN}N{Style.RESET_ALL} : Rover orienté vers le Nord")
    print(f"{Fore.GREEN}E{Style.RESET_ALL} : Rover orienté vers l'Est")
    print(f"{Fore.GREEN}S{Style.RESET_ALL} : Rover orienté vers le Sud")
    print(f"{Fore.GREEN}W{Style.RESET_ALL} : Rover orienté vers l'Ouest")
    print(f"{Fore.BLUE}·{Style.RESET_ALL} : Case vide\n")

    # axes
    print(f"{Fore.CYAN}Axe Y ↑{Style.RESET_ALL}")
    
    # coordonnées X
    print("    " + " ".join(f"{Fore.YELLOW}{x:2d}{Style.RESET_ALL}" for x in range(plateau.width + 1)))
    
    # plateau
    print("  +" + "---" * (plateau.width + 1) + "+")
    for y in range(plateau.height, -1, -1):
        print(f"{Fore.YELLOW}{y:2d}{Style.RESET_ALL} |", end=" ")
        for x in range(plateau.width + 1):
            rover_here = next((r for r in rovers if r.x == x and r.y == y), None)
            if rover_here:
                print(f"{Fore.GREEN}{rover_here.direction:1s}{Style.RESET_ALL} ", end="")
            else:
                print(f"{Fore.BLUE}·{Style.RESET_ALL} ", end="")
        print("|")
    print("  +" + "---" * (plateau.width + 1) + "+")
    print(f"{' ' * 4}{Fore.CYAN}Axe X →{Style.RESET_ALL}\n")

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
    display_plateau(plateau, rovers)

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

        try:
            rover = Rover(x, y, direction, plateau)
            print(f"🚀 Déplacement du Rover {rover_count} en cours...")
            time.sleep(1)  
            try:
                rover.execute_instructions(instructions)
                rovers.append(rover)
                print(f"✅ Rover {rover_count} déplacé avec succès à la position : {rover.x} {rover.y} {rover.direction}\n")
            except ValueError as e:
                print(f"⚠️ {str(e)}")
                print(f"Le Rover {rover_count} reste à sa dernière position valide : {rover.x} {rover.y} {rover.direction}\n")
            display_plateau(plateau, rovers)
        except ValueError as e:
            print(f"❌ Erreur : {str(e)}")
            rover_count -= 1
            continue

    print("\n🌟 Résultat final :")
    for idx, rover in enumerate(rovers, start=1):
        print(f"Rover {idx} : {rover.x} {rover.y} {rover.direction}")

    print("\nMerci d'avoir utilisé le Simulateur de Rover Martien ! 🛸👽")

if __name__ == "__main__":
    main()
