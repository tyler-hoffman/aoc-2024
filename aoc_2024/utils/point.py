from __future__ import annotations
from dataclasses import dataclass
from functools import total_ordering
from typing import Any


@total_ordering
@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, Point):
            return False
        else:
            return abs(self.x) + abs(self.y) < abs(other.x) + abs(other.y)

    def unit(self) -> Point:
        x = 0 if self.x == 0 else self.x // abs(self.x)
        y = 0 if self.y == 0 else self.y // abs(self.y)

        return Point(x, y)

    def add(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    def subtract(self, other: Point) -> Point:
        return Point(self.x - other.x, self.y - other.y)

    def multiply(self, amt: int) -> Point:
        return Point(self.x * amt, self.y * amt)

    def dist(self, other: Point) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    @property
    def neighbors(self) -> set[Point]:
        return {
            Point(self.x, self.y - 1),
            Point(self.x + 1, self.y),
            Point(self.x, self.y + 1),
            Point(self.x - 1, self.y),
        }
