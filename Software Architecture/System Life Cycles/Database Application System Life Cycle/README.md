# Database Application System Life Cycle (D-SLC) 🗄️

The **Database Application System Life Cycle** (Micro Life Cycle) focuses specifically on the development and maintenance of the database component within a larger information system. It ensures that the data architecture is robust, scalable, and meets the real-world requirements of the organization.

<img src="./db_lifecycle.svg" alt="Database Application Life Cycle" width="800" />

---

## 🔁 The 8 Phases of D-SLC

### 1. System Definition 📝
Defining the scope and boundaries of the database application.
- **Identify Users**: Who will access the data? (Admins, Customers, Managers).
- **Define Scope**: specific modules (e.g., Inventory, Sales).
- **Determine Constraints**: Response time, Storage needs, processing power.

### 2. Database Design 🏗️
Creating the blueprint for the data.
- **Conceptual Design**: Entity-Relationship Models (ERD).
- **Logical Design**: Normalization, Table structures, Primary/Foreign Keys.
- **Physical Design**: Indexing strategies, Storage allocation, Partitioning.

### 3. Database Implementation ⚙️
Turning the design into reality.
- **DDL (Data Definition Language)**: Creating tables, views, and schemas using SQL.
- **Security**: Setting up roles, permissions, and encryptions.
- **External View**: Creating interfaces/APIs for applications to access data.

### 4. Loading or Data Conversion 📤
Populating the empty database.
- **ETL (Extract, Transform, Load)**: Migrating data from legacy files (Excel, CSV, old DBs).
- **Data Cleaning**: Removing duplicates and correcting errors during import.
- *Critical for existing organizations moving to a new system.*

### 5. Application Conversion 🔄
Migrating the software logic.
- Updating legacy applications to connect to the new database schema.
- Rewriting queries and stored procedures.
- Ensuring the frontend correctly displays the new data format.

### 6. Testing and Validation ✅
Verifying correctness and performance.
- **Data Integrity Testing**: Ensuring constraints (Unique, Not Null) work.
- **Performance Testing**: Checking query speed under load.
- **ACID Testing**: Verifying Atomicity, Consistency, Isolation, and Durability of transactions.

### 7. Operation 🚀
Go-live phase.
- **Parallel Operation**: Running old and new systems simultaneously to ensure safety.
- **Cut-over**: Fully switching to the new system.

### 8. Monitoring and Maintenance 🔧
The longest phase.
- **Monitoring**: Watching for slow queries, deadlocks, and disk space usage.
- **Maintenance**: Re-indexing, Archiving old data, Backups.
- **Feedback Loop**: New requirements lead back to System Definition/Design.

---

## 🔄 Feedback Loops & Interdependency

As shown in the diagram, this is not a strictly linear process.
- **Feedback**: Insights from the *Monitoring* phase often trigger new *System Definitions* or *Designs*.
- **Overlap**: *Design* and *Implementation* often overlap.
- **Legacy vs New**: Activities 4 & 5 (Conversion) are skipped for brand new "Greenfield" projects but are the most critical/expensive parts of "Brownfield" projects.

---

## 🐍 Python Simulation

Run the simulation to see a mock Database Development Lifecycle in action:

```bash
python db_simulation.py
```
