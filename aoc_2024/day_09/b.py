from dataclasses import dataclass
from typing import Optional
from aoc_2024.day_09.parser import Parser


@dataclass
class Segment:
    id: Optional[int]
    start: int
    length: int
    removed: bool = False


@dataclass
class Day09PartBSolver:
    input: list[int]

    @property
    def solution(self) -> int:
        segments = self.get_segments(self.input)
        self.defrag(segments)
        disk_list = self.segments_to_disk_list(segments)
        return self.checksum(disk_list)

    def checksum(self, disk: list[Optional[int]]) -> int:
        output = 0
        for i, val in enumerate(disk):
            if val:
                output += i * val
        return output

    def defrag(self, segments: list[Segment]) -> None:
        val_segments = [val for val in segments if val.id is not None][::-1]
        for val_segment in val_segments:
            insert_index: Optional[int] = None

            # find index
            for i, segment in enumerate(segments):
                if segment.id is None:
                    if val_segment.start < segment.start:
                        break
                    else:
                        if val_segment.length <= segment.length:
                            insert_index = i
                            break

            # update segments
            if insert_index is not None:
                blank_segment = segments[insert_index]
                if blank_segment.length == val_segment.length:
                    blank_segment.id = val_segment.id
                else:
                    blank_segment.start += val_segment.length
                    blank_segment.length -= val_segment.length
                    segments.insert(
                        insert_index,
                        Segment(
                            id=val_segment.id,
                            start=val_segment.start,
                            length=val_segment.length,
                        ),
                    )
                val_segment.removed = True

    def segments_to_disk_list(self, segments: list[Segment]) -> list[Optional[int]]:
        output: list[Optional[int]] = []
        for segment in segments:
            val = segment.id if not segment.removed else None
            output += [val] * segment.length
        return output

    def get_segments(self, inputs: list[int]) -> list[Segment]:
        segments: list[Segment] = []
        current_id = 0
        current_length = 0
        file_mode = True
        for x in inputs:
            if file_mode:
                segments.append(Segment(id=current_id, length=x, start=current_length))
                current_id += 1
            else:
                segments.append(Segment(id=None, length=x, start=current_length))
            file_mode = not file_mode
            current_length += x
        return segments


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day09PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_09/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
