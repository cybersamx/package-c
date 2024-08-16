from pkg_e.arithmetic import (
    add,
    divide,
)


def count(sample: list[float]) -> float:
    return float(len(sample))


def mean(sample: list[float]) -> float:
    tot = 0.0

    for v in sample:
        tot = add(tot, v)

    return divide(tot, count(sample))
