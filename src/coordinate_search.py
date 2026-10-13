"""Basic coordinate search for a real-valued objective."""


def minimize(function, start, step=1.0, tolerance=1e-6, max_iterations=10000):
    if step <= 0 or tolerance <= 0 or max_iterations <= 0:
        raise ValueError("step, tolerance, and max_iterations must be positive")
    point = list(start)
    if not point:
        raise ValueError("start must contain at least one coordinate")
    value = function(point)
    for _ in range(max_iterations):
        improved = False
        for i in range(len(point)):
            for direction in (-1, 1):
                candidate = point.copy()
                candidate[i] += direction * step
                candidate_value = function(candidate)
                if candidate_value < value:
                    point, value, improved = candidate, candidate_value, True
        if not improved:
            step /= 2
            if step < tolerance:
                break
    return point, value
