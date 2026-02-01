import time
import sys
import os
import random

class SpiralProject:
    """
    Simulates the Spiral Model.
    Focuses on the 'Risk Analysis' quadrant. 
    The project proceeds in loops (Spirals).
    """
    
    def __init__(self, name):
        self.name = name
        self.spiral_count = 1
        self.budget_spent = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"INITIALIZING SPIRAL MODEL PROJECT: {self.name}")
        print("="*60)
        print("This simulation focuses on RISK ANALYSIS.")
        print("Each loop (Spiral) increases in cost and fidelity.")
        print("If Risk Analysis fails, the project can be TERMINATED.")
        print("="*60 + "\n")
        time.sleep(2)

    def _print_quadrant(self, quadrant, message):
        print(f"[SPIRAL {self.spiral_count} - {quadrant}]")
        print(f"   >> {message}")
        time.sleep(0.8)

    def run_spiral(self, objective, estimated_risk):
        print(f"\n" + "="*40)
        print(f"STARTING SPIRAL {self.spiral_count}: {objective}")
        print("="*40)
        
        # Quadrant 1: Objectives
        self._print_quadrant("planning", "Determining objectives and constraints...")
        self._print_quadrant("planning", "Identifying alternative solutions...")

        # Quadrant 2: Risk Analysis (CRITICAL)
        print("\n   [!] ENTERING RISK ANALYSIS SECTOR...")
        time.sleep(1)
        simulated_risk_val = random.random()
        
        # We simulate a prototype creation to mitigate risk
        self._print_quadrant("risk_analysis", f"Building Prototype v{self.spiral_count}.0 to test feasibility...")
        
        if simulated_risk_val < estimated_risk:
            # Risk Realized
            print(f"\n   [X] CRITICAL RISK DETECTED in Spiral {self.spiral_count}!")
            print(f"       Risk Factor: {simulated_risk_val:.2f} (Threshold: {estimated_risk})")
            print("       The prototype failed to validate the core assumptions.")
            
            print("\n   [?] DECISION POINT: Can we mitigate this?")
            time.sleep(1)
            if random.random() > 0.5:
                print("   >> Mitigation plan formulated. Proceeding with CAUTION.")
            else:
                print("   >> Mitigation IMPOSSIBLE. Technology is not mature enough.")
                print("\n   [X] PROJECT TERMINATED DUE TO HIGH RISK.")
                return False
        else:
            print("   >> Risk Analysis PASSED. Prototype validated.")

        # Quadrant 3: Engineering
        print("")
        self._print_quadrant("engineering", "Developing concept/code...")
        self._print_quadrant("engineering", "Testing deliverables...")
        
        # Quadrant 4: Evaluation
        print("")
        self._print_quadrant("evaluation", "Customer evaluating current build...")
        self._print_quadrant("evaluation", "Planning next Spiral...")
        
        self.spiral_count += 1
        return True

if __name__ == "__main__":
    project = SpiralProject("Autonomous Drone Navigation System")
    
    # Spiral 1: Feasibility
    if project.run_spiral("Concept of Operations", estimated_risk=0.2):
        # Spiral 2: Requirements
        if project.run_spiral("Requirements Definition", estimated_risk=0.3):
             # Spiral 3: Design
            if project.run_spiral("High-Level Design", estimated_risk=0.4):
                # Spiral 4: Implementation
                if project.run_spiral("Final Implementation", estimated_risk=0.1):
                    print("\n" + "="*60)
                    print("PROJECT COMPLETED SUCCESSFULLY THROUGH ALL SPIRALS")
