# OR-Daily-Mastery: The 84-Day Operations Research Curriculum 🚀

Welcome to **OR-Daily-Mastery**. 

This repository is a public, open-source learning journey dedicated to mastering Operations Research (OR) and Algorithm Engineering. Going from basic linear algebra to architecting enterprise-grade supply chain algorithms can feel overwhelming. The secret isn't to cram textbooks; the secret is absolute, relentless consistency.

This curriculum is designed around a simple philosophy: **One Concept a Day**. 

For 12 weeks (84 days), this repository will track daily progress from the microscopic foundations of geometric math up to the deployment of massive, containerized optimization microservices. Whether you are a student, a software engineer looking to pivot, or just someone fascinated by how global factories run, this roadmap will take you from zero to Algorithm Engineer.

---

## 🗺️ The 12-Week Master Plan

### Phase 1: The Linear Foundations (Weeks 1–2)
*The goal here is to stop seeing math as numbers and start seeing it as geometric shapes and boundaries.*

**Week 1: The Anatomy of Linear Programming (LP)**
* **Day 1:** **The Core Triad:** Isolate the Objective Function, Decision Variables, and Parameters.
* **Day 2:** **Linearity:** Understand what makes an equation strictly linear.
* **Day 3:** **2D Graphing:** Draw constraints to physically see the "walls" of a problem.
* **Day 4:** **Feasible Regions & Convexity:** Why an LP must have a convex shape.
* **Day 5:** **The Corner Point Theorem:** Proving the optimal answer is always at a sharp vertex.
* **Day 6:** **Standard Form:** Converting $\le$ and $\ge$ equations using Slack and Surplus variables.
* **Day 7:** **The Simplex Algorithm:** How Simplex "walks" from corner to corner.

**Week 2: Economic Intuition & Duality**
* **Day 8:** **Simplex Tableaus:** How computers organize equations into a grid.
* **Day 9:** **Degeneracy:** What happens when the computer gets "stuck" running in circles.
* **Day 10:** **Shadow Prices:** Calculating exactly how much one extra unit of resource is worth.
* **Day 11:** **Reduced Costs:** Calculating how much cheaper a product needs to be to become profitable.
* **Day 12:** **Primal vs. Dual LPs:** Flipping an LP upside down to minimize resource costs.
* **Day 13:** **Strong Duality Theorem:** Why primal profit exactly equals dual cost.
* **Day 14:** **Sensitivity Analysis:** How much a parameter can change before the schedule breaks.

---

### Phase 2: The Integer Reality (Weeks 3–4)
*Real factories don't manufacture 2.5 cars. Here, we force the math to respect whole-number reality.*

**Week 3: Mixed-Integer Programming (MIP)**
* **Day 15:** **The Integrality Gap:** Why rounding fractions is often a disastrous business decision.
* **Day 16:** **Binary Variables ($0$ or $1$):** Using math as "Yes/No" switches.
* **Day 17:** **Big-M Logic (Part 1):** Using massive numbers to turn constraints completely on/off.
* **Day 18:** **Big-M Logic (Part 2):** Linking an action (machine running) to a state (setup cost).
* **Day 19:** **Either/Or Constraints:** Forcing the solver to choose Path A or Path B.
* **Day 20:** **Fixed-Charge Problems:** Modeling flat startup fees.
* **Day 21:** **Absolute Values:** Linearizing $|x - y|$ using two bounding inequalities.

**Week 4: Under the Hood of the Solver**
* **Day 22:** **LP Relaxation:** How solvers pretend integers are decimals for a fast baseline.
* **Day 23:** **Branch and Bound:** Splitting fractional realities into parallel universes.
* **Day 24:** **Pruning:** Intelligently deleting bad search paths to save time.
* **Day 25:** **Cutting Planes:** Shaving off fractional edges of the geometric shape.
* **Day 26:** **Branch and Cut:** Combining tree search with shaving techniques.
* **Day 27:** **Symmetry Breaking:** Stopping the computer from comparing identical machines.
* **Day 28:** **The MIP Gap:** Knowing when to accept a 99% perfect schedule.

---

### Phase 3: Graph Theory & Networks (Weeks 5–6)
*Building the supply chain from a single dot to a global network.*

**Week 5: The Micro-Components of Graphs**
* **Day 29:** **Nodes and Edges:** The absolute basic definitions of a graph.
* **Day 30:** **Directed vs. Undirected Graphs:** One-way vs. two-way streets.
* **Day 31:** **Walks, Trails, and Paths:** Understanding route differences.
* **Day 32:** **Cycles & Trees:** Why a "Tree" guarantees no loops exist.
* **Day 33:** **Eulerian Paths:** Routes traveling every *edge* exactly once.
* **Day 34:** **Hamiltonian Paths:** Routes visiting every *node* exactly once.
* **Day 35:** **Bipartite Graphs:** Graphs divided into two distinct connecting sets.

**Week 6: Network Optimization Models**
* **Day 36:** **Network Flow Conservation:** Flow In minus Flow Out equals Demand.
* **Day 37:** **The Shortest Path Problem:** Formulating Dijkstra's algorithm.
* **Day 38:** **Max Flow / Min Cut Theorem:** Finding absolute bottlenecks.
* **Day 39:** **The Transportation Problem:** Moving goods between factories and warehouses.
* **Day 40:** **The Assignment Problem:** Matching specific workers to specific jobs.
* **Day 41:** **Minimum Spanning Trees:** The cheapest way to connect all nodes.
* **Day 42:** **Time-Expanded Networks:** Duplicating a map to track objects through time.

---

### Phase 4: Enterprise Routing & Heuristics (Weeks 7–8)
*When the math gets too big, we stop looking for perfection and start looking for speed.*

**Week 7: Vehicle Routing**
* **Day 43:** **The Traveling Salesperson Problem (TSP):** Formulating the Hamiltonian cycle.
* **Day 44:** **Subtour Elimination:** Stopping disconnected mini-circles (MTZ Constraints).
* **Day 45:** **The Vehicle Routing Problem (VRP):** Expanding TSP to fleets with capacities.
* **Day 46:** **Time Windows (VRPTW):** Forcing arrivals within specific timeframes.
* **Day 47:** **Multi-Depot Routing:** Managing trucks from different warehouses.
* **Day 48:** **NP-Hardness:** Why VRP breaks standard linear solvers.
* **Day 49:** **Dynamic Programming (DP):** The concept of memoization.

**Week 8: The Art of Guessing (Heuristics)**
* **Day 50:** **Greedy Algorithms:** Making the best immediate choice.
* **Day 51:** **Constructive Heuristics:** Building a "good enough" schedule instantly.
* **Day 52:** **Local Search:** Swapping two jobs to find a cheaper state.
* **Day 53:** **Neighborhood Structures:** Rules for how to "swap" or "move" jobs.
* **Day 54:** **Escaping Local Optima:** Why Local Search gets trapped in a valley.
* **Day 55:** **Simulated Annealing:** Using probability to accept worse schedules temporarily.
* **Day 56:** **Tabu Search:** Using a "memory diary" to avoid repeating bad swaps.

---

### Phase 5: Modern Architecture (Weeks 9–10)
*Entering the realm of the Senior Algorithm Engineer.*

**Week 9: Metaheuristics & AI**
* **Day 57:** **Genetic Algorithms (Part 1):** Defining Chromosomes and Populations.
* **Day 58:** **Genetic Algorithms (Part 2):** Crossover and Mutation.
* **Day 59:** **Ant Colony Optimization:** Using digital "pheromone trails" for routing.
* **Day 60:** **ALNS (Adaptive Large Neighborhood Search):** Ripping and repairing schedules.
* **Day 61:** **ALNS Roulette Wheel:** Teaching the algorithm which repair methods work best.
* **Day 62:** **Constraint Programming (CP):** Using CP Optimizer for exact sequencing.
* **Day 63:** **Interval Variables:** Modeling tasks as blocks of time.

**Week 10: Advanced Decomposition**
* **Day 64:** **The Curse of Dimensionality:** Why massive schedules run out of RAM.
* **Day 65:** **Rolling Horizons:** Freezing near-term schedules and relaxing the future.
* **Day 66:** **Column Generation (Concept):** Generating variables dynamically.
* **Day 67:** **The Master Problem:** The manager algorithm making high-level selections.
* **Day 68:** **The Subproblem:** The worker algorithm generating valid shifts.
* **Day 69:** **Benders Decomposition:** Splitting integer and continuous variables.
* **Day 70:** **Stochastic Programming:** Formulating under uncertainty.

---

### Phase 6: Production Engineering (Weeks 11–12)
*Bridging the gap between textbook math and enterprise software.*

**Week 11: Deployment & APIs**
* **Day 71:** **Data Validation:** Using Python (Pydantic/Pandas) to catch bad ERP data.
* **Day 72:** **Decoupling Logic:** Separating data parsing from the algebraic model.
* **Day 73:** **Building the API:** Wrapping the solver in a FastAPI microservice.
* **Day 74:** **JSON Payloads:** Structuring incoming requests and outgoing schedules.
* **Day 75:** **Dockerization:** Containerizing the solver environment.
* **Day 76:** **Logging & Debugging:** Catching 'Infeasible' errors in production.
* **Day 77:** **The Conflict Refiner:** Programmatically extracting conflicting constraints.

**Week 12: Business Strategy & Wrap-up**
* **Day 78:** **Multi-Objective Trade-offs:** Balancing conflicting KPIs.
* **Day 79:** **Pareto Frontiers:** Generating scenario options for stakeholders.
* **Day 80:** **Dynamic Rescheduling:** Handling real-time machine breakdowns.
* **Day 81:** **State Injection:** Freezing running jobs during a mid-shift re-solve.
* **Day 82:** **Measuring ROI:** Quantifying algorithm savings vs. manual planning.
* **Day 83:** **Human-in-the-Loop:** Translating veteran planner intuition into constraints.
* **Day 84:** **Final Project:** Build and solve a complete end-to-end factory scheduling model.

