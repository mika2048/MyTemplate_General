from typing import Iterable, Callable, Iterator


class accumulator:
    """
    前缀和类
    """

    def __init__(self, sequence: list, bin_func: Callable) -> None:
        self.sequence = sequence
        self.operation = bin_func

        self.accumulated = []
        last = None
        for item in sequence:
            if last is None:
                last = item
            else:
                last = self.operation(last, item)
            self.accumulated.append(last)

    def __iter__(self):
        return iter(self.accumulated)
