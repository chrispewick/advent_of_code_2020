from typing import Tuple

from utils.performance_utils import get_the_avg_time_to_do_the_thing

SUM_GOAL = 2020


def get_numbers_basic(entries) -> Tuple[int, int, int]:
    for index, x in enumerate(entries):
        for y in entries[index+1:]:
            for z in entries[index+2:]:
                if x + y + z == 2020:
                    return x, y, z


def get_numbers_set(entries) -> Tuple[int, int, int]:
    values = set()
    for index, x in enumerate(entries):
        for y in entries[index+1:]:
            target = SUM_GOAL - x - y
            if target in values:
                return x, y, target
            values.add(y)


def find_solution(entries):
    try:
        first, second, third = get_numbers_set(entries)
        print(f"Solution entries: {first} x {second} x {third} = {first * second * third}")
    except TypeError:
        print("There is no solution!")


if __name__ == "__main__":
    input_entries = [int(line) for line in open("input.txt", "r")]
    find_solution(input_entries)

    avg_time = get_the_avg_time_to_do_the_thing(get_numbers_set, input_entries)
    print(f"Average time: {avg_time}")
    # Average time: 0.09263489218999993
