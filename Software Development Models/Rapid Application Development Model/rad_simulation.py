import time
import sys
import os
import random

class RADProject:
    """
    Simulates the Rapid Application Development (RAD) Model.
    Focuses on:
    1. Parallel Development (Teams working at once)
    2. Time-Boxing (Strict 60-day deadline)
    3. User Feedback Loops
    """
    
    def __init__(self, name):
        self.name = name
        self.deadline_days = 60
        self.current_day = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"INITIALIZING RAD PROJECT: {self.name}")
        print("="*60)
        print("Model: Rapid Application Development")
        print("Constraints: STRICT 60-DAY DEADLINE")
        print("Structure: 3 Parallel Teams")
        print("="*60 + "\n")
        time.sleep(2)

    def _parallel_work(self, day, teams):
        print(f"   [Day {day}] Parallel Sprint Status:")
        for team, task in teams.items():
            progress = random.choice([
                "Building Prototype", "User Feedback Session", 
                "Refining Component", "Automated Testing"
                ])
            print(f"    - {team}: {progress}...")
        time.sleep(0.8)

    def run(self):
        # Phase 1: Requirements Planning (Fast)
        print("+--- PHASE 1: REQUIREMENTS PLANNING")
        print("|    Gathering basic scope...")
        time.sleep(1)
        print("|    [OK] Scope Defined. Launching Parallel Teams.")
        self.current_day += 5
        
        # Phase 2 & 3: User Design & Construction (Combined & Parallel)
        print("\n+--- PHASES 2 & 3: PARALLEL DESIGN & CONSTRUCTION")
        teams = {
            "Team UI": "Frontend",
            "Team DB": "Database",
            "Team API": "Logic"
        }
        
        while self.current_day < 55:
            self._parallel_work(self.current_day, teams)
            self.current_day += 10
            
            # Simulated User Feedback
            print("    >> USER FEEDBACK: 'Change the button layout!' -> Teams Adapting...")
        
        # Phase 4: Cutover
        print("\n+--- PHASE 4: CUTOVER")
        print("|    Integrating Modules...")
        time.sleep(1)
        print("|    Data Migration...")
        print("|    Final Testing...")
        
        if self.current_day <= self.deadline_days:
            remaining = self.deadline_days - self.current_day
            print(f"\n[SUCCESS] Project Delivered ON TIME! ({remaining} days spare)")
        else:
            print(f"\n[FAILURE] Project Overdue! RAD requires strict time management.")

if __name__ == "__main__":
    project = RADProject("Internal Inventory Tool")
    project.run()
