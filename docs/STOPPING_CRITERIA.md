# Stopping criteria for numerical optimisation

Choose stopping rules before comparing algorithms.

- **Step tolerance:** stop when consecutive iterates differ by less than a threshold.
- **Objective tolerance:** stop when objective improvement is sufficiently small.
- **Gradient norm:** for differentiable methods, check a norm of the gradient.
- **Iteration budget:** impose a finite maximum as a safety bound.
- **Evaluation budget:** count objective calls when evaluations are expensive.

Record which criterion triggered termination and whether convergence was established.