class Plateau:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.occupied_positions = set()

    def is_within_bounds(self, x, y):
        return 0 <= x <= self.width and 0 <= y <= self.height

    def is_position_occupied(self, x, y):
        return (x, y) in self.occupied_positions

    def mark_position(self, x, y):
        self.occupied_positions.add((x, y))

    def unmark_position(self, x, y):
        self.occupied_positions.discard((x, y))
