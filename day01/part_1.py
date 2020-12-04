from typing import Tuple

from utils.performance_utils import get_the_avg_time_to_do_the_thing

SUM_GOAL = 2020


def get_numbers_basic(entries) -> Tuple[int, int]:
    for index, x in enumerate(entries):
        for y in entries[index+1:]:
            if x + y == 2020:
                return x, y


def get_numbers_set(entries) -> Tuple[int, int]:
    values = set()
    for entry in entries:
        target = SUM_GOAL - entry
        if target in values:
            return entry, target
        values.add(entry)


def find_solution(entries):
    try:
        x, y = get_numbers_set(entries)
        print(f"Solution entries: {x} x {y} = {x * y}")
    except TypeError:
        print("There is no solution!")


if __name__ == "__main__":
    input_entries = [int(line) for line in open("input.txt", "r")]
    find_solution(input_entries)

    avg_time = get_the_avg_time_to_do_the_thing(get_numbers_set, input_entries)
    print(f"Average time: {avg_time}")
