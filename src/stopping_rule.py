"""Simple objective-based stopping rule."""


def should_stop(previous, current, tolerance=1e-6):
    if tolerance < 0:
        raise ValueError("tolerance must be non-negative")
    return abs(previous - current) <= tolerance
