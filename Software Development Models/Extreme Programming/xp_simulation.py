import time
import sys
import os
import random

class XPSimulation:
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("EXTREME PROGRAMMING (XP) SESSION")
        print("="*60)
        print("Role: You are the 'Driver'.")
        print("Partner: AI Agent (The 'Navigator').")
        print("Task: Implement a 'Stock Price Calculator'.")
        print("method: Test-Driven Development (TDD).")
        print("="*60 + "\n")
        time.sleep(2)

    def run_tdd_cycle(self, feature_name):
        print("\n" + "-"*40)
        print(f"CYCLE START: Feature '{feature_name}'")
        
        # Step 1: Write Test (RED)
        print("[NAVIGATOR]: I've written a failing test for this feature.")
        print(f"             assert {feature_name}(input) == expected_output")
        time.sleep(1)
        print("             RUNNING TESTS...")
        time.sleep(1)
        print("             [X] FAILED (Red State). Function doesn't exist.")
        
        # Step 2: Write Code (GREEN)
        print("\n[DRIVER]: Writing minimal code to pass the test...")
        time.sleep(1.5)
        print("          def calculation(): return expected_value")
        print("          RUNNING TESTS...")
        time.sleep(1)
        print("          [OK] PASSED (Green State).")
        
        # Step 3: Refactor (BLUE)
        print("\n[NAVIGATOR]: Wait, that code is messy. Let's Refactor.")
        print("             Renaming variables... Extracting methods...")
        time.sleep(1.5)
        print("             Code is now CLEAN.")
        print("-"*40)

    def run(self):
        # Feature 1
        self.run_tdd_cycle("Calculate_Profit")
        
        # Feature 2
        print("\n[NAVIGATOR]: Good job partner. Switching roles! You Navigate, I Drive.")
        time.sleep(2)
        
        print("\n" + "-"*40)
        print("CYCLE START: Feature 'Risk_Assessment'")
        print("[YOU]: (Writing failing test...)")
        time.sleep(1)
        print("       [X] Test Failed.")
        
        print("\n[AI DRIVER]: Coding the logic...")
        time.sleep(1.5)
        print("             if risk > 10: return False")
        print("             [OK] Test Passed.")
        print("-"*40)
        
        print("\n[SUCCESS] Session Complete. All features implemented safely.")

if __name__ == "__main__":
    sim = XPSimulation()
    sim.run()
