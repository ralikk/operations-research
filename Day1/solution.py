# Day 1: The Execution
from docplex.mp.model import Model
import data

# 1. Initialize the Model
mdl = Model(name="Boutique_Bakery_Optimization")

# 2. Define the Decision Variables (The Dials)
# We use continuous variables here to keep it simple for Day 1
cakes = ["Chocolate", "Vanilla"]
x = mdl.continuous_var_dict(cakes, lb=0, name="Bake")

# 3. Define the Constraints (The Laws of Physics)
# Flour Constraint
mdl.add_constraint(
    mdl.sum(data.recipes["Flour"][c] * x[c] for c in cakes) <= data.available_resources["Flour"],
    ctname="Flour_Limit"
)

# Sugar Constraint
mdl.add_constraint(
    mdl.sum(data.recipes["Sugar"][c] * x[c] for c in cakes) <= data.available_resources["Sugar"],
    ctname="Sugar_Limit"
)

# 4. Define the Objective Function (The Scoreboard)
# Maximize total profit
total_profit = mdl.sum(data.profits[c] * x[c] for c in cakes)
mdl.maximize(total_profit)

# 5. Solve and Output
solution = mdl.solve()

if solution:
    print("--- Optimal Baking Schedule ---")
    for c in cakes:
        print(f"{c} Cakes to bake: {x[c].solution_value}")
    print(f"Total Projected Profit: ${solution.get_objective_value()}")
else:
    print("Solver could not find a feasible solution.")
