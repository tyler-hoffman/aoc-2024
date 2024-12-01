from typing import Hashable, Mapping, TypeVar

_T = TypeVar("_T", bound=Hashable)


def freq_map(values: list[_T]) -> Mapping[_T, int]:
    output: dict[_T, int] = {}
    for val in values:
        if val not in output:
            output[val] = 0
        output[val] += 1
    return output
