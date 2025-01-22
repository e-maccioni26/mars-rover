import unittest
from src.rover import Rover
from src.plateau import Plateau

class TestRover(unittest.TestCase):
    def setUp(self):
        self.plateau = Plateau(5, 5)

    def test_initial_position(self):
        rover = Rover(1, 2, 'N', self.plateau)
        self.assertEqual((rover.x, rover.y, rover.direction), (1, 2, 'N'))

    def test_rotation_left(self):
        rover = Rover(1, 2, 'N', self.plateau)
        rover.rotate_left()
        self.assertEqual(rover.direction, 'W')

    def test_rotation_right(self):
        rover = Rover(1, 2, 'N', self.plateau)
        rover.rotate_right()
        self.assertEqual(rover.direction, 'E')

    def test_move(self):
        rover = Rover(1, 2, 'N', self.plateau)
        rover.move()
        self.assertEqual((rover.x, rover.y), (1, 3))

    def test_instruction_sequence(self):
        rover = Rover(1, 2, 'N', self.plateau)
        rover.execute_instructions("LMLMLMLMM")
        self.assertEqual((rover.x, rover.y, rover.direction), (1, 3, 'N'))

if __name__ == "__main__":
    unittest.main()
