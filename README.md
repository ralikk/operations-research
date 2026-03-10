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

**Week 5:
