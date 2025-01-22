class Rover:
    def __init__(self, x, y, direction, plateau):
        self.x = x
        self.y = y
        self.direction = direction
        self.plateau = plateau

        if not self.plateau.is_within_bounds(x, y):
            raise ValueError(f"Initial position ({x}, {y}) is out of bounds.")
        self.plateau.mark_position(x, y)

    def rotate_left(self):
        directions = ['N', 'W', 'S', 'E']
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def rotate_right(self):
        directions = ['N', 'E', 'S', 'W']
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def move(self):
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

    def execute_instructions(self, instructions):
        """
        Exécute une série d'instructions ('L', 'R', 'M') pour déplacer le rover.
        """
        for instruction in instructions:
            if instruction == 'L':
                self.rotate_left()
            elif instruction == 'R':
                self.rotate_right()
            elif instruction == 'M':
                self.move()
