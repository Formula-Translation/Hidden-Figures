from sympy import symbols, Eq, solve
x = symbols('x')
equation = (x**2 + 6*x - 7) * (2*x**2 - 5*x - 3)
equation_zero = Eq(equation, 0)
solutions = solve(equation_zero, x)
print(solutions)
