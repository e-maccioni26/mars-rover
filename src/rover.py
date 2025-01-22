from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from plateau import Plateau 


class Rover:
    def __init__(self, x: int, y: int, direction: str, plateau: "Plateau") -> None:
        valid_directions = {'N', 'E', 'S', 'W'}
        if direction not in valid_directions:
            raise ValueError(f"Direction invalide : {direction}. Utilisez l'une des valeurs {valid_directions}.")

        self.x: int = x
        self.y: int = y
        self.direction: str = direction
        self.plateau: "Plateau" = plateau

        if not self.plateau.is_within_bounds(x, y):
            raise ValueError(f"Position initiale ({x}, {y}) hors des limites du plateau.")
        if self.plateau.is_position_occupied(x, y):
            raise ValueError(f"Position initiale ({x}, {y}) déjà occupée.")
        
        self.plateau.mark_position(x, y)

    def rotate_left(self) -> None:
        """
        Fait pivoter le rover de 90° à gauche (sens antihoraire).
        """
        directions = ['N', 'W', 'S', 'E']
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def rotate_right(self) -> None:
        """
        Fait pivoter le rover de 90° à droite (sens horaire).
        """
        directions = ['N', 'E', 'S', 'W']
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def move(self) -> None:
        """
        Déplace le rover d'une unité dans la direction actuelle, si possible.
        """
        new_x, new_y = self.x, self.y
        if self.direction == 'N':
            new_y += 1
        elif self.direction == 'E':
            new_x += 1
        elif self.direction == 'S':
            new_y -= 1
        elif self.direction == 'W':
            new_x -= 1

        if self.plateau.is_within_bounds(new_x, new_y) and not self.plateau.is_position_occupied(new_x, new_y):
            self.plateau.unmark_position(self.x, self.y)
            self.x, self.y = new_x, new_y
            self.plateau.mark_position(new_x, new_y)
        else:
            raise ValueError(f"Le mouvement vers ({new_x}, {new_y}) est impossible (hors limites ou position occupée).")

    def execute_instructions(self, instructions: List[str]) -> None:
        valid_instructions = {'L', 'R', 'M'}
        for instruction in instructions:
            if instruction not in valid_instructions:
                raise ValueError(f"Instruction invalide : {instruction}. Utilisez l'une des valeurs {valid_instructions}.")
            if instruction == 'L':
                self.rotate_left()
            elif instruction == 'R':
                self.rotate_right()
            elif instruction == 'M':
                self.move()
