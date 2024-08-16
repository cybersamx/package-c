import math
import unittest
from dataclasses import dataclass

from pkg_c.stats import (
    count,
    mean,
)


@dataclass
class StatsTestCase:
    m: list[float]
    count_expect: float
    mean_expect: float


def compare(a: float, b: float) -> bool:
    epsilon = 0.00001
    return math.fabs(a-b) < epsilon


class TestStats(unittest.TestCase):
    tcs = [
        StatsTestCase([1, 2, 3, 4], 4, 2.5),
        StatsTestCase([610, 450, 160, 420, 310], 5, 390),
    ]

    def test_count(self):
        for tc in self.tcs:
            res = count(tc.m)
            expect = tc.count_expect
            self.assertEqual(res, expect)

    def test_mean(self):
        for tc in self.tcs:
            res = mean(tc.m)
            expect = tc.mean_expect
            self.assertEqual(res, expect)


if __name__ == '__main__':
    unittest.main()
