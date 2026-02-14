"""
Database Application Life Cycle Simulation
==========================================
This script simulates the lifecycle of building a database for an 
E-commerce platform.

It demonstrates concepts like Schema Design, Data Loading (ETL), 
Validation, and Operational Maintenance.
"""

import time
import random

class DatabaseProject:
    def __init__(self, name):
        self.name = name
        self.phase = "Init"
        self.tables = []
        self.record_count = 0
        self.status = "Planning"

    def log(self, message):
        print(f"[{self.phase.upper()}] {message}")
        time.sleep(0.5)

    def system_definition(self):
        self.phase = "Definition"
        self.log(f"Defining scope for '{self.name}'...")
        self.log("Identified Users: Customers, Sellers, Admins")
        self.log("Storage Requirement: Predicted 1TB/year")

    def database_design(self):
        self.phase = "Design"
        self.log("Creating ER Diagrams...")
        self.log("Normalizing tables to 3NF...")
        self.tables = ["Users", "Products", "Orders", "Payments"]
        print(f"   -> Designed Tables: {', '.join(self.tables)}")

    def implementation(self):
        self.phase = "Implement"
        self.log("Executing DDL Scripts...")
        for table in self.tables:
            print(f"   -> CREATE TABLE {table} (id INT PRIMARY KEY...);")
        self.log("Setting up Indexes and Foreign Keys.")

    def data_conversion_loading(self):
        self.phase = "Data Load"
        self.log("Starting ETL Process from Legacy CSV files...")
        chunks = 5
        for i in range(chunks):
            loaded = random.randint(1000, 5000)
            self.record_count += loaded
            print(f"   -> Loaded Chunk {i+1}/{chunks}: {loaded} records...")
            time.sleep(0.3)
        self.log(f"Data Loading Compelte. Total Records: {self.record_count}")

    def app_conversion(self):
        self.phase = "App Convert"
        self.log("Updating Backend API to use new Connection String...")
        self.log("Rewriting Stored Procedures...")

    def testing_validation(self):
        self.phase = "Testing"
        self.log("Running Data Consistency Checks...")
        
        # Simulate a data error
        if random.choice([True, False]):
            self.log("⚠️ Found Orphaned Records in 'Orders' table.")
            self.log("   -> Fixing Integrity Constraints...")
        
        self.log("Running Query Performance Tests...")
        print("   -> SELECT * FROM Orders WHERE user_id = ? (Index Hit: ✅)")

    def operation(self):
        self.phase = "Operation"
        self.log("System Go-Live!")
        self.log("Parallel Run: Old System ✅ | New System ✅")
        time.sleep(1)
        self.log("Cut-over complete. Old system decommissioned.")

    def maintenance(self):
        self.phase = "Maintenance"
        print("\n--- Operational Maintenance ---")
        events = ["Index Fragmentation", "Disk Space Alert", "Slow Query", "New Requirement"]
        
        for _ in range(3):
            event = random.choice(events)
            self.log(f"Event Detected: {event}")
            if event == "Indexes":
                print("   -> Re-building Indexes...")
            elif event == "New Requirement":
                print("   -> Feedback received. Initiating new Design Cycle...")
            else:
                print("   -> Resolving issue...")
            time.sleep(0.5)

def run_simulation():
    print("===========================================")
    print("   DATABASE LIFE CYCLE SIMULATION          ")
    print("===========================================")
    
    db = DatabaseProject("ShopEasy DB")
    
    db.system_definition()
    db.database_design()
    db.implementation()
    db.data_conversion_loading()
    db.app_conversion()
    db.testing_validation()
    db.operation()
    db.maintenance()

if __name__ == "__main__":
    run_simulation()
