from typing import Tuple

from utils.performance_utils import get_the_avg_time_to_do_the_thing_for_things_in_a_list


def check_password(item: str) -> bool:
    parts = item.split(":")
    first_pos, second_pos, character = get_rule_parts(parts[0].strip())
    password = parts[1].strip()
    return (character in password[first_pos]) != (character in password[second_pos])


def get_rule_parts(rule: str) -> Tuple[int, int, str]:
    rule_parts = rule.replace("-", " ").split()
    first_pos = int(rule_parts[0]) - 1
    second_pos = int(rule_parts[1]) - 1
    character = rule_parts[2]
    return first_pos, second_pos, character


if __name__ == "__main__":
    input_entries = [line.strip() for line in open("input.txt", "r")]
    print(len(list(filter(check_password, input_entries))))

    avg_time = get_the_avg_time_to_do_the_thing_for_things_in_a_list(check_password, input_entries)
    print(f"Average time: {avg_time}")
