from typing import Hashable, Mapping


def freq_map[T: Hashable](values: list[T]) -> Mapping[T, int]:
    output: dict[T, int] = {}
    for val in values:
        if val not in output:
            output[val] = 0
        output[val] += 1
    return output
