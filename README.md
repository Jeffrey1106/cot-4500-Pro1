# Programming Assignment 1

## Overview
This project implements four numerical methods to solve root-finding problems:

1. **Approximation Algorithm** - Approximates the square root of 2 using iterative averaging.
2. **Bisection Method** - Finds roots of functions through interval halving.
3. **Fixed-Point Iteration** - Solves equations by iteratively applying a transformation function.
4. **Newton-Raphson Method** - A root-finding algorithm using derivatives for faster convergence.

The code is organized to follow the standard structure as per assignment requirements.

---

## Project Structure
```
PA1/
├── src/
│   ├── main/
│   │   ├── __init__.py
│   │   └── assignment_1.py
│   └── test/
│       ├── __init__.py
│       └── test_assignment_1.py
├── requirements.txt
└── README.md
```

- **`assignment_1.py`**: Contains the implementation of all four algorithms.
- **`test_assignment_1.py`**: Includes test cases with detailed logs, matching the expected output from the slides.
- **`requirements.txt`**: Lists the dependencies (currently none required).
- **`README.md`**: Provides instructions for setup and execution.

---

## Requirements
- **Python 3.x** (Recommended: 3.8+)
- No external libraries are required (uses Python's standard library).

If dependencies are added:
```bash
pip install -r requirements.txt
```

---

## How to Run

### 1. **Running the Algorithms Directly**
If needed, you can import functions from `assignment_1.py` in your own scripts.

### 2. **Running Test Cases**
The tests showcase the output for all four methods with detailed iteration logs:

```bash
python -m src.test.test_assignment_1
```

This will output:
- **Approximation Algorithm** logs (iterations to approximate √2)
- **Bisection Method** logs with iteration details
- **Fixed-Point Iteration** results (success/failure)
- **Newton-Raphson Method** convergence logs

---

## Example Outputs
### Approximation Algorithm:
```
0 : 1.5
1 : 1.4166666667
2 : 1.4142156863
3 : 1.4142135624
4 : 1.4142135624

Convergence after 4 iterations
```

### Bisection Method:
```
Iteration 1: p = 1.5
Iteration 2: p = 1.25
...
Convergence after 9 iterations
```

### Fixed-Point Iteration:
```
Iteration 1: p = 1.2865938
...
Success after 20 iterations
```

### Newton-Raphson Method:
```
Iteration 0: p = 0.7853981635
Iteration 1: p = 0.7395361337
...
Success after 4 iterations
```

---

## Author
Jeffrey Chang 
Course: COT-4500 - Numerical Calculus  
Assignment: Programming Assignment 1

