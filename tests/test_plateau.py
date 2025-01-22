import unittest
from src.plateau import Plateau

class TestPlateau(unittest.TestCase):
    def test_within_bounds(self):
        plateau = Plateau(5, 5)
        self.assertTrue(plateau.is_within_bounds(3, 3))
        self.assertFalse(plateau.is_within_bounds(6, 5))

    def test_collision_prevention(self):
        plateau = Plateau(5, 5)
        plateau.mark_position(1, 2)
        self.assertTrue(plateau.is_position_occupied(1, 2))

if __name__ == "__main__":
    unittest.main()
