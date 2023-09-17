from state import *

OPEN = " "
OUTER_WALL = "#"
INNER_WALL = "@"
BEGIN = "R"
END = "T"
FLOW = ["↑", "→", "↓", "←"]
ROUTE = ["☝", "☞", "☟", "☜"]

DIRECTION = 4

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

MAZE = [
    [
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
    ],
    [OUTER_WALL, OPEN, OPEN, OPEN, OPEN, OPEN, OPEN, OPEN, OPEN, OUTER_WALL],
    [OUTER_WALL, OPEN, OPEN, OPEN, OPEN, OPEN, OPEN, INNER_WALL, OPEN, OUTER_WALL],
    [OUTER_WALL, OPEN, OPEN, OPEN, OPEN, OPEN, OPEN, INNER_WALL, END, OUTER_WALL],
    [
        OUTER_WALL,
        OPEN,
        INNER_WALL,
        INNER_WALL,
        INNER_WALL,
        INNER_WALL,
        OPEN,
        INNER_WALL,
        OPEN,
        OUTER_WALL,
    ],
    [
        OUTER_WALL,
        OPEN,
        INNER_WALL,
        OPEN,
        OPEN,
        OPEN,
        OPEN,
        INNER_WALL,
        OPEN,
        OUTER_WALL,
    ],
    [
        OUTER_WALL,
        OPEN,
        INNER_WALL,
        OPEN,
        OPEN,
        OPEN,
        OPEN,
        INNER_WALL,
        OPEN,
        OUTER_WALL,
    ],
    [
        OUTER_WALL,
        BEGIN,
        INNER_WALL,
        OPEN,
        OPEN,
        OPEN,
        OPEN,
        INNER_WALL,
        OPEN,
        OUTER_WALL,
    ],
    [OUTER_WALL, OPEN, OPEN, OPEN, OPEN, OPEN, OPEN, OPEN, OPEN, OUTER_WALL],
    [
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
    ],
]

DIFFERENCE = [[-1, 0], [0, 1], [1, 0], [0, -1]]

temp = 0


def main():
    print_map(MAZE)

    return


class Solver:
    State = State()

    w = 0
    h = 0
    done = False
    cancelled = False
    age = 0
    maze = []

    def set(self, x, y, maze):
        pass

    def step(self, n):
        n = n or 1
        states = [None, None, None, None]

        while ():
            self.age += 1
            changes = 0
            for y in range(self.h):
                for x in range(self.w):
                    states[0] = self.get(self, x + 0, y + -1)
                    states[1] = self.get(self, x + 1, y + 0)
                    states[2] = self.get(self, x + 0, y + 1)
                    states[3] = self.get(self, x + -1, y + 0)

                    current = self.get(self, x, y)
                    next = State.next(current, states)

                    if current != next:
                        changes += 1
                    self.set(x, y, next)

    def get(self, x, y):
        if x >= 0 and x < self.w and y >= 0 and self.h:
            return self.maze[y][x]
        else:
            return State.WALL


def print_map(map_matrix):
    for row in map_matrix:
        print(" ".join(row))


if __name__ == "__main__":
    main()
