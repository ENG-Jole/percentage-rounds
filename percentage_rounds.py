from timeit import timeit
from itertools import repeat
from random import uniform
from typing import Final


def get_percentage_rounds_if_else(percentage: float) -> str:
    if percentage == 0:
        return "⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️"
    if percentage > 0.0 and percentage <= 0.1:
        return "🔵⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️"
    if percentage > 0.1 and percentage <= 0.2:
        return "🔵🔵⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️"
    if percentage > 0.2 and percentage <= 0.3:
        return "🔵🔵🔵⚪️⚪️⚪️⚪️⚪️⚪️⚪️"
    if percentage > 0.3 and percentage <= 0.4:
        return "🔵🔵🔵🔵⚪️⚪️⚪️⚪️⚪️⚪️"
    if percentage > 0.4 and percentage <= 0.5:
        return "🔵🔵🔵🔵🔵⚪️⚪️⚪️⚪️⚪️"
    if percentage > 0.5 and percentage <= 0.6:
        return "🔵🔵🔵🔵🔵🔵⚪️⚪️⚪️⚪️"
    if percentage > 0.6 and percentage <= 0.7:
        return "🔵🔵🔵🔵🔵🔵🔵⚪️⚪️⚪️"
    if percentage > 0.7 and percentage <= 0.8:
        return "🔵🔵🔵🔵🔵🔵🔵🔵⚪️⚪️"
    if percentage > 0.8 and percentage <= 0.9:
        return "🔵🔵🔵🔵🔵🔵🔵🔵🔵⚪️"

    return "🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵"


def get_percentage_rounds_match_case(percentage: float) -> str:
    pct: int = int(percentage * 10 + 0.5)

    match pct:
        case 0:
            return "⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️"
        case 1:
            return "🔵⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️"
        case 2:
            return "🔵🔵⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️"
        case 3:
            return "🔵🔵🔵⚪️⚪️⚪️⚪️⚪️⚪️⚪️"
        case 4:
            return "🔵🔵🔵🔵⚪️⚪️⚪️⚪️⚪️⚪️"
        case 5:
            return "🔵🔵🔵🔵🔵⚪️⚪️⚪️⚪️⚪️"
        case 6:
            return "🔵🔵🔵🔵🔵🔵⚪️⚪️⚪️⚪️"
        case 7:
            return "🔵🔵🔵🔵🔵🔵🔵⚪️⚪️⚪️"
        case 8:
            return "🔵🔵🔵🔵🔵🔵🔵🔵⚪️⚪️"
        case 9:
            return "🔵🔵🔵🔵🔵🔵🔵🔵🔵⚪️"
        case 10:
            return "🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵"
        case _:
            return "⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️"


def get_percentage_rounds_repeat(percentage: float) -> str:
    return "".join(repeat("🔵", int(percentage * 10))) + "".join(
        repeat("⚪️", 10 - int(percentage * 10))
    )


def get_percentage_rounds_loop(percentage: float) -> str:
    rounds: str = ""
    pct: int = int(percentage * 10)
    for i in range(pct + 1):
        rounds += "🔵"
    for j in range(10 - pct + 1):
        rounds += "⚪️"

    return rounds


def get_percentage_rounds_slice(percentage: float) -> str:
    rounds: Final = "🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️"
    pct: int = int(percentage * 10)
    # fmt: off
    return rounds[
        10 - pct:10 + 10 - pct
    ]  # absolutely do not care if this is actually accurate
    # fmt: on


if __name__ == "__main__":
    if_else: float = timeit(
        "get_percentage_rounds_if_else(uniform(0.0, 1.0))",
        globals=globals(),
        number=5000000,
    )
    match_case: float = timeit(
        "get_percentage_rounds_match_case(uniform(0.0, 1.0))",
        globals=globals(),
        number=5000000,
    )
    repeat_func: float = timeit(
        "get_percentage_rounds_repeat(uniform(0.0, 1.0))",
        globals=globals(),
        number=5000000,
    )
    loop_func: float = timeit(
        "get_percentage_rounds_loop(uniform(0.0, 1.0))",
        globals=globals(),
        number=5000000,
    )
    slice_func: float = timeit(
        "get_percentage_rounds_slice(uniform(0.0, 1.0))",
        globals=globals(),
        number=5000000,
    )

    print(
        f"If Else: {if_else}s\nMatch Case: {match_case}s\nRepeat: {repeat_func}s\nLoop: {loop_func}s\nSlice: {slice_func}s"
    )
