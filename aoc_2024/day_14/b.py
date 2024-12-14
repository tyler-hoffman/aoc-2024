from dataclasses import dataclass
from aoc_2024.day_14.parser import Parser
from aoc_2024.day_14.tree_determiner_determiner import TreeDeterminer
from aoc_2024.utils.point import Point


@dataclass
class Day14PartBSolver:
    robots: list[tuple[Point, Point]]
    width: int
    height: int
    tree_determiner: TreeDeterminer

    @property
    def solution(self) -> int:
        seconds = 0

        while True:
            robot_positions = [
                self.get_end_position(p, v, seconds) for p, v in self.robots
            ]
            if self.tree_determiner.is_tree(
                seconds=seconds,
                width=self.width,
                height=self.height,
                points=robot_positions,
            ):
                return seconds
            seconds += 1

    def get_end_position(self, p: Point, v: Point, s: int) -> Point:
        end = p.add(v.multiply(s))
        return Point(end.x % self.width, end.y % self.height)


class HumanTreeDeterminer(TreeDeterminer):
    def is_tree(
        self,
        seconds: int,
        width: int,
        height: int,
        points: list[Point],
    ) -> bool:
        if self.has_tip(
            points,
            width=width,
            height=height,
        ):
            line_break = "\n" + "=" * width + "\n"
            grid: list[list[str]] = []
            for _ in range(height):
                grid.append([])
                for _ in range(width):
                    grid[-1].append(" ")
            for p in points:
                grid[p.y][p.x] = "X"

            print(line_break)
            for line in grid:
                print("".join(line))
            print(line_break)

            answer = input(f"{seconds}: is it a tree? ")
            return answer == "y"
        else:
            return False

    def has_tip(self, points: list[Point], width: int, height: int) -> bool:
        """Check if we have what might be the top of a tree somewhere, e.g.

        .......
        ...X...
        ..X.X..
        .......

        """
        mid = width // 2
        as_set = set(points)
        for y in range(height - 1):
            if all(
                [
                    Point(mid, y) in as_set,
                    Point(mid - 1, y + 1) in as_set,
                    Point(mid + 1, y + 1) in as_set,
                ]
            ):
                return True
        return False


def solve(
    input: str, tree_determiner: TreeDeterminer, width: int = 101, height: int = 103
) -> int:
    data = Parser.parse(input)
    solver = Day14PartBSolver(
        robots=data,
        tree_determiner=tree_determiner,
        width=width,
        height=height,
    )

    return solver.solution


def get_solution(tree_determiner: TreeDeterminer = HumanTreeDeterminer()) -> int:
    with open("aoc_2024/day_14/input.txt", "r") as f:
        input = f.read()
    return solve(input, tree_determiner)


if __name__ == "__main__":
    print(get_solution())
