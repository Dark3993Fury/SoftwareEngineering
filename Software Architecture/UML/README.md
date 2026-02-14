# Unified Modeling Language (UML) 📐

**UML** is the standardized general-purpose modeling language for software engineering. It provides a set of graphic notation techniques to create visual models of object-oriented software-intensive systems.

<img src="./uml_overview.svg" alt="UML Overview" width="800" />

---

## Why do we need UML?

1.  **Standardization**: A universal language developers, architects, and stakeholders understand.
2.  **Visualization**: Makes complex systems easier to understand than thousands of lines of code.
3.  **Documentation**: Provides a blueprint for future maintenance.
4.  **Planning**: Allows architectural decisions to be made *before* coding begins (Blueprint vs Construction).

---

## 1. Class Diagram (Structural) 🏗️

The backbone of almost every object-oriented method. It describes the static structure of a system.

*   **Classes**: Attributes and Methods.
*   **Relationships**: Inheritance, Association, Aggregation, Composition.

```mermaid
classDiagram
    Animal <|-- Duck
    Animal <|-- Fish
    Animal : +int age
    Animal : +String gender
    Animal : +isMammal()
    Animal : +mate()
    class Duck{
      +String beakColor
      +swim()
      +quack()
    }
    class Fish{
      -int sizeInFeet
      -canEat()
    }
```

---

## 2. Sequence Diagram (Behavioral) ⏱️

Shows object interactions arranged in **time sequence**. It depicts the objects involved in the scenario and the sequence of messages exchanged.

*   **Lifelines**: Vertical dashed lines representing object existence over time.
*   **Messages**: Arrows showing communication.

```mermaid
sequenceDiagram
    participant User
    participant ATM
    participant BankServer

    User->>ATM: Insert Card
    ATM->>BankServer: Verify Card
    BankServer-->>ATM: Card OK
    ATM->>User: Request PIN
    User->>ATM: Enter PIN 1234
    ATM->>BankServer: Validate PIN
    BankServer-->>ATM: PIN Validated
    ATM->>User: Select "Withdraw $100"
    ATM->>BankServer: Check Balance
    BankServer-->>ATM: Balance Sufficient
    ATM->>User: Dispense Cash
```

---

## 3. Use Case Diagram (Behavioral) 👤

Captures the dynamic behavior of a system. It models the **Actors** (users) and the **Use Cases** (functionalities).

*   **Actor**: Stick figure (User/System).
*   **Use Case**: Oval (Functionality).
*   **System Boundary**: Rectangle around use cases.

```mermaid
graph LR
    User((User))
    Admin((Admin))

    subgraph "Banking System"
        Login(Login)
        CheckBal(Check Balance)
        Transfer(Transfer Funds)
        ManageUsers(Manage Users)
    end

    User --> Login
    User --> CheckBal
    User --> Transfer
    Admin --> Login
    Admin --> ManageUsers
```

---

## 4. Component Diagram (Structural) 🧩

Depicts how components are wired together to form larger components or software systems. It illustrates the architectures of the software components and the dependencies between them.

*   **Component**: Modular part of a system.
*   **Interface**: Connection point (circle/socket).
*   **Dependency**: Dashed arrow.

```mermaid
graph TD
    subgraph "E-Commerce System"
        UI[Web UI Component]
        Order[Order Processing Component]
        Inventory[Inventory Management Component]
        Payment[Payment Gateway Component]
        DB[(Database)]
    end

    UI --> Order
    Order --> Inventory
    Order --> Payment
    Inventory --> DB
    Order --> DB
```

---

## 🐍 Python Simulation

Run the included simulation to see how a model translates to actual object-oriented code:

```bash
python uml_code_mapping.py
```
