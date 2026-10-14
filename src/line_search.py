"""Backtracking line search for a scalar objective and descent direction."""

def backtracking(f, x, direction, alpha=1.0, shrink=0.5, armijo=1e-4, max_steps=50):
    if alpha <= 0 or not 0 < shrink < 1 or not 0 < armijo < 1 or max_steps < 1:
        raise ValueError('invalid line-search parameters')
    fx = f(x)
    for _ in range(max_steps):
        candidate = x + alpha * direction
        if f(candidate) <= fx + armijo * alpha * direction:
            return alpha
        alpha *= shrink
    return alpha
