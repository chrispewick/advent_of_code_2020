import time


# TODO: come up with more mature function names. Or Don't. Whatever.

def get_the_avg_time_to_do_the_thing(function, arg):
    times = [_get_the_time_to_do_the_thing(function, arg) for _ in range(1000)]
    return sum(times) / len(times)


def get_the_avg_time_to_do_the_thing_for_things_in_a_list(function, input_list):
    times = [_get_the_time_to_do_the_thing_for_things_in_list(function, input_list) for _ in range(1000)]
    return sum(times) / len(times)


def _get_the_time_to_do_the_thing(function, arg):
    start = time.perf_counter()
    function(arg)
    end = time.perf_counter()
    return end - start


def _get_the_time_to_do_the_thing_for_things_in_list(function, input_list):
    start = time.perf_counter()
    [function(item) for item in input_list]
    end = time.perf_counter()
    return end - start
