import time
import sys
import os

class VModelProject:
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("SDLC V-MODEL SIMULATION: Airbag Control System")
        print("="*60)
        print("Goal: Build a Safety-Critical System.")
        print("Rule: For every Design Phase, a Test Plan MUST be created.")
        print("="*60 + "\n")
        time.sleep(2)
        
        self.test_plans = {}

    def phase_verification(self):
        print("--- PHASE 1: VERIFICATION (Down the V) ---")
        
        # Level 1: Requirements
        print("\n[1] Requirements Analysis: 'Airbag must deploy in 20ms.'")
        time.sleep(1)
        print("    >> CREATING COMPANION TEST: User Acceptance Test (UAT) Plan... DONE")
        self.test_plans['UAT'] = "Simulate 50mph crash. Check deployment < 20ms."
        
        # Level 2: System Design
        print("\n[2] System Design: 'Sensors -> ECU -> Inflator'")
        time.sleep(1)
        print("    >> CREATING COMPANION TEST: System Test Plan... DONE")
        self.test_plans['System'] = "Verify ECU triggers Inflator on sensor signal."
        
        # Level 3: Module Design
        print("\n[3] Module Design: 'calculate_impact_force() function'")
        time.sleep(1)
        print("    >> CREATING COMPANION TEST: Unit Test Plan... DONE")
        self.test_plans['Unit'] = "Test calculate_impact_force(500N) returns True."
        
        print("\n" + "="*40)
        print("      POINT OF THE V: CODING PHASE")
        print("      ( writing C++ code... )")
        print("="*40 + "\n")
        time.sleep(2)

    def phase_validation(self):
        print("--- PHASE 2: VALIDATION (Up the V) ---")
        
        # Level 3: Unit Testing
        print("\n[3] Unit Testing (Validating Module Design)...")
        print(f"    EXEC: {self.test_plans['Unit']}")
        time.sleep(1)
        print("    RESULT: [PASS] Function logic is correct.")
        
        # Level 2: System Testing
        print("\n[2] System Testing (Validating System Design)...")
        print(f"    EXEC: {self.test_plans['System']}")
        time.sleep(1)
        print("    RESULT: [PASS] Hardware integration success.")
        
        # Level 1: Customer Testing
        print("\n[1] UAT (Validating Requirements)...")
        print(f"    EXEC: {self.test_plans['UAT']}")
        time.sleep(1.5)
        print("    RESULT: [PASS] Airbag deployed in 18ms.")
        
        print("\n" + "="*60)
        print("PROJECT COMPLETE: System Verified & Validated.")

if __name__ == "__main__":
    project = VModelProject()
    project.phase_verification()
    project.phase_validation()
