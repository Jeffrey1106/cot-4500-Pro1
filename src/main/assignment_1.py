import math

def approximate_sqrt_two():
    """Approximate sqrt(2) using iterative averaging method."""
    x0 = 1.5  # Initial guess
    tol = 0.000001  # Tolerance level
    iter_count = 0  # Iteration counter
    diff = x0
    x = x0  # Initial value

    print(f"{iter_count} : {x}")

    while diff >= tol:
        iter_count += 1
        y = x  # Store the previous value
        x = (x / 2) + (1 / x)  # Update x based on the approximation formula
        print(f"{iter_count} : {x}")

        diff = abs(x - y)  # Compute the difference

    print(f"\nConvergence after {iter_count} iterations\n")


def bisection_method(f, left, right, tol=1e-6, max_iter=100):
    """Find the root of f(x) using the Bisection Method."""
    iter_count = 0

    while abs(right - left) > tol and iter_count < max_iter:
        iter_count += 1
        p = (left + right) / 2  # Midpoint

        if f(left) * f(p) < 0:  # Root is in left half
            right = p
        else:  # Root is in right half
            left = p

    print(f"\nBisection Method converged to {p} after {iter_count} iterations\n")
    return p


def fixed_point_iteration(g, p0, tol=1e-6, max_iter=100):
    """Find fixed point using Fixed-Point Iteration."""
    iter_count = 0

    while iter_count < max_iter:
        p = g(p0)

        if abs(p - p0) < tol:
            print(f"\nFixed-Point Iteration converged to {p} after {iter_count+1} iterations\n")
            return p

        iter_count += 1
        p0 = p

    print("\nFixed-Point Iteration failed to converge\n")
    return None


def newton_raphson(f, df, p0, tol=1e-6, max_iter=100):
    """Find root using Newton-Raphson Method."""
    iter_count = 0

    while iter_count < max_iter:
        if df(p0) == 0:
            print("\nNewton-Raphson Method failed: Derivative is zero\n")
            return None

        p_next = p0 - f(p0) / df(p0)

        if abs(p_next - p0) < tol:
            print(f"\nNewton-Raphson Method converged to {p_next} after {iter_count+1} iterations\n")
            return p_next

        iter_count += 1
        p0 = p_next

    print("\nNewton-Raphson Method failed to converge\n")
    return None


# if __name__ == "__main__":
#     print("Running Approximation Algorithm for sqrt(2)...\n")
#     approximate_sqrt_two()

#     # Function for Bisection Method (Example: f(x) = x^2 - 2)
#     f = lambda x: x**2 - 2
#     print("Running Bisection Method for sqrt(2)...\n")
#     bisection_method(f, 1, 2)

#     # Function for Fixed-Point Iteration (Example: g(x) = (x + 2/x) / 2)
#     g = lambda x: (x + 2/x) / 2
#     print("Running Fixed-Point Iteration for sqrt(2)...\n")
#     fixed_point_iteration(g, 1.5)

#     # Functions for Newton-Raphson Method (Example: f(x) = x^2 - 2, f'(x) = 2x)
#     df = lambda x: 2*x
#     print("Running Newton-Raphson Method for sqrt(2)...\n")
#     newton_raphson(f, df, 1.5)
