from dataclasses import dataclass

from aoc_2024.utils.point import Point


@dataclass(frozen=True)
class ArcadeGame:
    a: Point
    b: Point
    prize: Point
