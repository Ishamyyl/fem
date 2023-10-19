from dataclasses import dataclass


@dataclass
class Point:
    y: int
    x: int


directions = [  # (y, x)
    (-1, 0),  # up
    (0, 1),  # right
    (1, 0),  # down
    (0, -1),  # left
]


def walk(maze: list[str], wall: str, cur: Point, end: Point, seen: list[list[bool]], path: list[Point]) -> bool:
    if cur.x < 0 or cur.x >= len(maze[0]) or cur.y < 0 or cur.y >= len(maze):
        return False
    if maze[cur.y][cur.x] == wall:
        return False
    if cur.x == end.x and cur.y == end.y:
        path.append(cur)
        return True
    if seen[cur.y][cur.x]:
        return False
    seen[cur.y][cur.x] = True
    path.append(cur)
    for y, x in directions:
        if walk(maze, wall, Point(cur.y + y, cur.x + x), end, seen, path):
            return True
    path.pop()
    return False


def solve(maze: list[str], wall: str, start: Point, end: Point) -> list[Point]:
    seen = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    path = []
    walk(maze, wall, start, end, seen, path)
    return path


if __name__ == "__main__":
    # m = [
    #     "#####E#",
    #     "#     #",
    #     "#S#####",
    # ]
    m = [
        "########## #",
        "#        # #",
        "#        # #",
        "# ######## #",
        "#          #",
        "############",
    ]
    e = Point(2, 8)
    s = Point(0, 10)
    print(solve(m, "#", s, e))
