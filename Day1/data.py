# Day 1: Data Separation
# Storing our factory parameters in clean Python dictionaries

# Profit per cake (The Objective coefficients: c_j)
profits = {
    "Chocolate": 20,
    "Vanilla": 15
}

# Total available resources (The Right-Hand Side limits: b_i)
available_resources = {
    "Flour": 10,
    "Sugar": 10
}

# Recipe requirements (The constraint coefficients: a_ij)
# Format: recipe[Resource][Cake Type] = amount needed
recipes = {
    "Flour": {
        "Chocolate": 2,
        "Vanilla": 1
    },
    "Sugar": {
        "Chocolate": 1,
        "Vanilla": 2
    }
}
