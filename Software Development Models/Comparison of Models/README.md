# Comparison of SDLC Models

> "There is no silver bullet."

Choosing the right SDLC model is critical for project success. Using **Waterfall** for a startup idea will kill it (too slow). Using **Big Bang** for a medical device will kill people (too risky).

## Summary Table

| Model | Best For | Pros | Cons | Cost |
| :--- | :--- | :--- | :--- | :--- |
| **Waterfall** | Simple, unchanging projects. | Easy to manage. Clear milestones. | No feedback until end. Rigid. | Low (if no changes) |
| **V-Model** | Safety-critical systems (Medical, Aero). | High reliability. Testing is prioritized. | Very rigid. Expensive to change. | High |
| **Spiral** | High-risk, large projects. | Risk analysis. Iterative. | Complex management. Expensive. | Very High |
| **Agile (Scrum)** | Evolving requirements. Teams < 10. | Rapid feedback. flexible. | Needs experienced team. Scope creep. | Medium |
| **XP** | High quality code. Unstable requirements. | Fewer bugs. Safe to change. | Developer burnout. Expensive pairs. | High |
| **RAD** | Rapid prototyping needed. Strict deadline. | Fast delivery. User involved. | Needs skilled devs. Hard to scale. | High |
| **Prototype** | Unclear requirements ("I'll know it when I see it"). | User satisfaction. Early clarity. | "Throwaway" work. False expectations. | Medium |
| **Big Bang** | Learning, Hackathons, Tiny scripts. | Immediate start. Zero overhead. | High risk. Unmaintainable code. | Very Low (or Infinite if it fails) |

---

## Detailed Comparison

### 1. Waterfall vs. Agile
*   **Waterfall** is like building a house. You need the blueprint (Requirements) before you pour the foundation (Design). modifying the blueprint after the roof is up is very expensive.
*   **Agile** is like gardening. You plant seeds (Features), water them, and prune them as they grow. You can move a plant (Refactor) if it's in the wrong spot.

### 2. V-Model vs. Testing in Waterfall
*   In **Waterfall**, testing happens at the end (Phase 5). If you find a requirement bug there, you have to redo everything.
*   In **V-Model**, every phase has a test plan. You write the "Acceptance Test" *while* you are gathering requirements. You catch bugs on paper before writing code.

### 3. Spiral vs. Prototype
*   **Prototype** builds a dummy UI to check if the *User* likes it.
*   **Spiral** builds a prototype to check if the *Technology* works (Risk Analysis).
    *   *Use Prototype*: If you aren't sure what the screen should look like.
    *   *Use Spiral*: If you aren't sure if the algorithm can handle 1 million users.

### 4. RAD vs. Agile
*   **RAD** is focused on *Speed* (Timeline). "Get it done in 60 days."
*   **Agile** is focused on *Adaptability* (Change). "Get the most important thing done next."

## Decision Matrix: Which one should I use?

1.  **Is the project simple and requirements fixed?** -> *Waterfall*.
2.  **Is human life at risk (Medical/Car)?** -> *V-Model*.
3.  **Are requirements unclear/changing?** -> *Agile (Scrum)*.
4.  **Is tecnical risk very high?** -> *Spiral*.
5.  **Is the timeline very tight (must demo in 1 month)?** -> *RAD*.
6.  **Does the customer not know what they want?** -> *Prototype*.
7.  **Is this a weekend hackathon?** -> *Big Bang*.
