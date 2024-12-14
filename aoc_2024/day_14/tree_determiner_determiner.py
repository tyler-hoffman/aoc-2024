from abc import ABC, abstractmethod

from aoc_2024.utils.point import Point


class TreeDeterminer(ABC):
    """Given some info about the state, determines
    if we have a tree.
    """

    @abstractmethod
    def is_tree(
        self,
        seconds: int,
        width: int,
        height: int,
        points: list[Point],
    ) -> bool: ...
