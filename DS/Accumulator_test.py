import Accumulator
import pytest


cases = []

seq = [1, 2, 3, 4, 5, 6]
func = lambda x, y: x + y
exp = [1, 3, 6, 10, 15, 21]
cases.append(((seq, func), exp))

seq = []
func = lambda x, y: x + y
exp = []
cases.append(((seq, func), exp))

seq = [-1]
func = lambda x, y: abs(x)
exp = [-1]
cases.append(((seq, func), exp))

seq = [-1, -2]
func = lambda x, y: abs(x)
exp = [-1, 1]
cases.append(((seq, func), exp))


def test_accumulator():
    for pars, exps in cases:
        acc = Accumulator.accumulator(*pars)
        assert list(acc) == exps


if __name__ == "__main__":
    pytest.main(["-v", "ds/Accumulator_test.py"])
