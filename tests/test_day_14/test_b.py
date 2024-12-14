from aoc_2024.day_14.b import get_solution
from aoc_2024.day_14.from_prompt import SOLUTION_B
from aoc_2024.day_14.tree_determiner_determiner import TreeDeterminer
from aoc_2024.utils.point import Point


class AllKnowingTreeDeterminer(TreeDeterminer):
    """Really finding the answer required a real live human being to interpret the picture.

    That human being has imparted his knowledge of the solution to this TreeDeterminer.

    Does this make the test worthless? ✅
    Are we still doing it? ✅
    """

    def is_tree(
        self,
        seconds: int,
        width: int,
        height: int,
        points: list[Point],
    ) -> bool:
        return seconds == SOLUTION_B


def test_my_solution():
    tree_determiner = AllKnowingTreeDeterminer()
    assert get_solution(tree_determiner) == SOLUTION_B
