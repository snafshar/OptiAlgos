"""Utilities for reporting optimization progress."""


def relative_improvement(previous: float, current: float) -> float:
    """Return fractional improvement for a minimization objective."""
    if previous < 0 or current < 0:
        raise ValueError("objective values must be non-negative")
    if previous == 0:
        return 0.0
    return (previous - current) / previous


if __name__ == "__main__":
    print(f"{relative_improvement(100, 82):.1%}")
