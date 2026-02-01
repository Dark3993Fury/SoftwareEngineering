# Scrum Model

> "Inspect and Adapt."

Scrum is the most popular Agile framework. It splits work into fixed-length iterations called **Sprints** (usually 2 weeks). Ideally, at the end of every Sprint, you have a shippable product increment.

## The 3-5-3 Structure
Scrum is defined by **3 Roles, 5 Events, and 3 Artifacts**.

### 3 Roles
1.  **Product Owner (PO)**: Represent the customer. "Owns" the Product Backlog. Defines *what* to build.
2.  **Scrum Master (SM)**: Facilitates the process. Removes blockers. Protects the team.
3.  **Development Team**: The people who do the work (Coding, Testing, Design).

### 3 Artifacts
1.  **Product Backlog**: Ordered list of everything that might be needed in the product.
2.  **Sprint Backlog**: The selected items for *this* Sprint.
3.  **Increment**: The sum of all work completed during the Sprint (must be working software).

### 5 Events
1.  **Sprint**: The container event (1-4 weeks).
2.  **Sprint Planning**: Deciding what to do in this Sprint.
3.  **Daily Scrum (Standup)**: 15-min meeting. "What did I do yesterday? What am I doing today? Blockers?"
4.  **Sprint Review**: Demo the product to stakeholders.
5.  **Sprint Retrospective**: Team reflects on *how* to work better next time.

---

## Real-Life Example: Building an E-Commerce Site

*   **Product Backlog**: 1. Login, 2. Shopping Cart, 3. Checkout, 4. Wishlist.
*   **Sprint 1 (2 Weeks)**:
    *   **Planning**: Team picks "Login" + "Shopping Cart".
    *   **Daily**: "I finished the Login API." / "I'm stuck on the Cart Database."
    *   **result**: At the end of 2 weeks, Login and Cart work perfectly.
    *   **Review**: Stakeholders play with it. "Looks good, but the Cart needs a 'Delete' button."
    *   **Retro**: "We spent too much time in meetings. Let's cut them shorter."
*   **Sprint 2**: Team picks "Checkout" + "Cart Delete Button".

---

## Pros & Cons

| Advantages | Disadvantages |
| :--- | :--- |
| **Transparency**: Everyone knows status daily. | **Meeting Heavy**: Daily meetings can drain energy. |
| **Adaptability**: Change direction every 2 weeks. | **Scope Creep**: Easy to keep adding new features forever. |
| **Quality**: Regular inspection prevents huge failures. | **Requires Maturity**: Hard for inexperienced teams to self-organize. |

---

## Simulation: Daily Scrum Standup

Run the simulation to participate in a specific event: The **Daily Standup**. You will report your status and handle blockers!

```bash
python scrum_simulation.py
```
