# Day 1: The Core Triad of Operations Research

Before we write complex algorithms, we must understand the anatomy of a mathematical model. Every Linear Program (LP) consists of three interconnected components, known as the Core Triad.



## 1. Decision Variables (The Dials)
These are the blank boxes the algorithm gets to fill in. They represent the actions we can take.
* **Notation:** Typically represented as $x_j$, where $j$ is an index.
* **Continuous Variables:** $x \ge 0$ (e.g., liters of water).
* **Integer/Binary Variables:** $x \in \{0, 1, 2, ...\}$ (e.g., number of cars, machine ON/OFF).

## 2. The Objective Function (The Scoreboard)
This is the single goal of the algorithm. It mathematically defines what "success" looks like, calculating a total score based on the values chosen for the Decision Variables.
* **Notation:** $\max Z$ or $\min Z$
* **Standard Form:** $$\max Z = \sum_{j=1}^{n} c_j x_j$$
*(Where $$c_j$$ is the profit or cost associated with variable $x_j$)*

## 3. Constraints (The Laws of Physics)
These are the hard limits of reality. The solver must obey these rules while trying to maximize or minimize the Objective Function.
* **Notation:** Inequalities ($\le$, $\ge$) or strict equalities ($=$).
* **Standard Form:** $$\sum_{j=1}^{n} a_{ij} x_j \le b_i \quad \forall i \in \{1, \dots, m\}$$
*(Where $a_{ij}$ is the resource consumed by $x_j$, and $b_i$ is the total resource available)*
