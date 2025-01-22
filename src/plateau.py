from typing import Set, Tuple


class Plateau:
    def __init__(self, width: int, height: int) -> None:
        """
        Initialise un plateau avec des dimensions données.

        :param width: Largeur du plateau (entier positif).
        :param height: Hauteur du plateau (entier positif).
        """
        if width < 0 or height < 0:
            raise ValueError("La largeur et la hauteur doivent être des entiers positifs.")
        self.width: int = width
        self.height: int = height
        self.occupied_positions: Set[Tuple[int, int]] = set()

    def is_within_bounds(self, x: int, y: int) -> bool:
        """
        Vérifie si une position (x, y) est dans les limites du plateau.

        :param x: Coordonnée x.
        :param y: Coordonnée y.
        :return: True si la position est dans les limites, False sinon.
        """
        return 0 <= x <= self.width and 0 <= y <= self.height

    def is_position_occupied(self, x: int, y: int) -> bool:
        """
        Vérifie si une position (x, y) est occupée par un rover.

        :param x: Coordonnée x.
        :param y: Coordonnée y.
        :return: True si la position est occupée, False sinon.
        """
        return (x, y) in self.occupied_positions

    def mark_position(self, x: int, y: int) -> None:
        """
        Marque une position (x, y) comme occupée.

        :param x: Coordonnée x.
        :param y: Coordonnée y.
        """
        self.occupied_positions.add((x, y))

    def unmark_position(self, x: int, y: int) -> None:
        """
        Démarque une position (x, y) comme occupée.

        :param x: Coordonnée x.
        :param y: Coordonnée y.
        """
        self.occupied_positions.discard((x, y))
