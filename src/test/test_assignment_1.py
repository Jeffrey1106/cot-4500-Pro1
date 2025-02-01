import math
from src.main.assignment_1 import approximate_sqrt_two, bisection_method, fixed_point_iteration, newton_raphson

# Test Approximation Algorithm for sqrt(2)
def test_approximate_sqrt_two():
    print("Running Approximation Algorithm for sqrt(2)...\n")
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


# Test Bisection Method
def test_bisection_method():
    print("Running Bisection Method for f(x) = x^3 + 4x^2 - 10...\n")
    f = lambda x: x**3 + 4*x**2 - 10
    left, right = 1, 2
    tol = 1e-3
    iter_count = 0

    while abs(right - left) > tol:
        iter_count += 1
        p = (left + right) / 2
        print(f"Iteration {iter_count}: p = {p}")

        if f(left) * f(p) < 0:
            right = p
        else:
            left = p

    print(f"\nBisection Method converged to {p} after {iter_count} iterations\n")


# Test Fixed-Point Iteration
def test_fixed_point_iteration():
    print("Running Fixed-Point Iteration for g(x) = (10 - x^3)^(1/2) / 2...\n")
    g = lambda x: math.sqrt(10 - x**3) / 2
    p0 = 1.5
    tol = 1e-6
    max_iter = 20
    iter_count = 0

    while iter_count < max_iter:
        p = g(p0)
        print(f"Iteration {iter_count + 1}: p = {p}")

        if abs(p - p0) < tol:
            print(f"\nSuccess after {iter_count + 1} iterations\n")
            return

        iter_count += 1
        p0 = p

    print("\nFailure after 20 iterations\n")


# Test Newton-Raphson Method
def test_newton_raphson():
    print("Running Newton-Raphson Method for f(x) = cos(x) - x...\n")
    f = lambda x: math.cos(x) - x
    df = lambda x: -math.sin(x) - 1
    p0 = math.pi / 4
    tol = 1e-10
    max_iter = 20
    iter_count = 0

    print(f"Iteration {iter_count}: p = {p0}")

    while iter_count < max_iter:
        if df(p0) == 0:
            print("\nFailure: Derivative is zero\n")
            return

        p_next = p0 - f(p0) / df(p0)
        iter_count += 1
        print(f"Iteration {iter_count}: p = {p_next}")

        if abs(p_next - p0) < tol:
            print(f"\nSuccess after {iter_count} iterations\n")
            return

        p0 = p_next

    print("\nFailure: Maximum iterations reached\n")


if __name__ == '__main__':
    test_approximate_sqrt_two()
    test_bisection_method()
    test_fixed_point_iteration()
    test_newton_raphson()
