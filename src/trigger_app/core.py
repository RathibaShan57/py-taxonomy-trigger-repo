"""Complexity, branch/path, defs/uses, and typed functions for Crosshair."""


def add(left: int, right: int) -> int:
    total = left + right
    return total


def nested(value: int) -> int:
    result = 0
    if value > 0:
        if value > 1:
            if value > 2:
                result = value * 2
            else:
                result = value
        else:
            result = 1
    return result


def decide(flag: bool, extra: bool) -> str:
    """Two independent conditions so pymcdc has MC/DC requirements."""
    if flag and extra:
        return "both"
    if flag:
        return "flag"
    if extra:
        return "extra"
    return "none"


def score_bucket(n: int) -> str:
    """Extra branches left untested so coverage-py reports missing lines/branches."""
    if n < 0:
        return "neg"
    if n == 0:
        return "zero"
    if n < 10:
        return "small"
    if n < 100:
        return "mid"
    return "large"
