"""
Information System Life Cycle (ISLC) Simulation
===============================================
This script simulates the lifecycle of a large-scale Information System
(e.g., a Hospital Management System) through its various phases.

It demonstrates how a system evolves from a simple idea to a legacy system
that eventually needs retirement or replacement.
"""

import time
import random

class InformationSystem:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.phase = "Concept"
        self.users = 0
        self.data_size_gb = 0
        self.health = 100  # System health percentage
        self.years_active = 0
        
    def log(self, message):
        print(f"[{self.phase.upper()}] {message}")
        time.sleep(0.5)

    def feasibility_analysis(self):
        self.phase = "Feasibility"
        self.log(f"Analyzing economic and technical feasibility for '{self.name}'...")
        if self.budget < 50000:
            print("❌ Budget too low. Project Cancelled.")
            return False
            
        print(f"✅ Feasibility Study Passed. Budget: ${self.budget}")
        return True

    def requirements_collection(self):
        self.phase = "Requirements"
        self.log("Interviewing doctors, nurses, and admins...")
        self.log("Identifying pain points in current paper-based process.")
        requirements = ["Patient Records", "Billing", "Appointments", "Inventory"]
        print(f"   -> Key Requirements Identified: {', '.join(requirements)}")
        return True

    def design_and_development(self):
        self.phase = "Design & Dev"
        self.log("Designing Database Schema (Patients, Doctors, Visits)...")
        self.log("Architecting Microservices...")
        self.log("Coding Application Logic...")
        self.log("Implementing Security Protocols (HIPAA Compliance)...")
        self.data_size_gb = 0.5 # Initial schema size
        return True

    def validation_testing(self):
        self.phase = "Validation"
        self.log("Running Unit Tests...")
        self.log("Performing User Acceptance Testing (UAT) with Hospital Staff...")
        bugs = random.randint(5, 15)
        self.log(f"Found {bugs} bugs. Fixing them...")
        self.health = 100
        print("✅ System Validated & Ready.")
        return True

    def deployment(self):
        self.phase = "Deployment"
        self.log("Migrating legacy data...")
        self.log("Deploying to Production Servers...")
        self.log("Training Staff...")
        self.users = 50 # Initial pilot users
        self.years_active = 1
        print("🚀 SYSTEM GOES LIVE!")
        return True

    def operation_and_maintenance(self):
        self.phase = "Operations"
        print("\n--- Years Passing (Operational Phase) ---")
        
        for year in range(1, 6):
            self.years_active += 1
            
            # Growth
            self.users += random.randint(50, 200)
            self.data_size_gb += random.randint(10, 50)
            
            # Wear and Tear
            health_drop = random.randint(5, 15)
            self.health -= health_drop
            
            print(f"Year {year}: Users: {self.users}, Data: {self.data_size_gb}GB, Health: {self.health}%")
            
            # Maintenance Events
            if self.health < 80:
                self.log("⚠️ Performance degrading. Monitoring alerts triggered.")
                self.perform_maintenance()
            
            if self.users > 500 and self.health > 90:
                self.log("📈 Scaling up infrastructure to handle load...")

    def perform_maintenance(self):
        print("   -> 🔧 Maintenance Team deployed: Patching servers, optimizing queries...")
        recovery = random.randint(10, 20)
        self.health = min(100, self.health + recovery)
        print(f"   -> System Health restored to {self.health}%")

    def retirement(self):
        self.phase = "Retirement"
        print("\n--- End of Life ---")
        self.log("System is now 5+ years old.")
        self.log("Technology is outdated. Maintenance costs are exceeding value.")
        self.log("Planning migration to new Cloud-Based AI System.")
        self.log("Archiving data and Decommissioning servers.")
        print("🪦 System Retired.")

def run_simulation():
    print("==============================================")
    print("   INFORMATION SYSTEM LIFE CYCLE SIMULATION   ")
    print("==============================================")
    
    hms = InformationSystem("City Hospital HMS", 150000)
    
    if hms.feasibility_analysis():
        hms.requirements_collection()
        hms.design_and_development()
        hms.validation_testing()
        hms.deployment()
        hms.operation_and_maintenance()
        hms.retirement()

if __name__ == "__main__":
    run_simulation()
