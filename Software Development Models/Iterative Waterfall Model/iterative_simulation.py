import time
import sys
import os
import random

class IterativeWaterfallProject:
    """
    Simulates the Iterative Waterfall Model.
    Introduces 'Feedback Loops' where a phase might fail validation,
    forcing the project to return to a previous phase.
    """
    
    def __init__(self, name):
        self.name = name
        self.indent_level = 0
        self.phase_map = {
            0: "Requirements",
            1: "Design",
            2: "Implementation",
            3: "Testing",
            4: "Deployment"
        }
        
        # Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"INITIALIZING ITERATIVE PROJECT: {self.name}")
        print("="*60)
        print("This simulation includes RANDOMIZED DEFECTS.")
        print("Watch for '<-- FEEDBACK LOOP' events where the project steps back.")
        print("="*60 + "\n")
        time.sleep(2)

    def _print_step(self, phase_index, status, message=""):
        indent = " " * (phase_index * 6)
        name = self.phase_map[phase_index].upper()
        
        if status == "START":
            print(f"{indent}+--- [PHASE {phase_index + 1}: {name}]")
            print(f"{indent}|    Status: Starting...")
        elif status == "WORK":
            print(f"{indent}|    >> {message}")
            time.sleep(0.6)
        elif status == "DONE":
            print(f"{indent}|    [COMPLETE]")
            print(f"{indent}V")
        elif status == "FAIL":
            print(f"{indent}|    [X] CRITICAL ISSUE FOUND: {message}")
            print(f"{indent}^")
            print(f"{indent}|")
            print(f"{indent}+--- <-- FEEDBACK LOOP TRIGGERED (Reverting...)")
            time.sleep(1.5)

    def run_phase(self, phase_index):
        if phase_index > 4:
            print("\n" + "="*60)
            print("PROJECT DEPLOYED SUCCESSFULLY!")
            return

        self._print_step(phase_index, "START")
        
        # Simulating work
        tasks = [f"Performing {self.phase_map[phase_index]} task {i+1}" for i in range(3)]
        for task in tasks:
            self._print_step(phase_index, "WORK", task)
        
        # Validation Logic (Simulation of Feedback)
        # 30% chance of failure in Design, Implementation, or Testing
        if phase_index in [1, 2, 3] and random.random() < 0.35:
            issue = f"Defect detected in {self.phase_map[phase_index]}!"
            self._print_step(phase_index, "FAIL", issue)
            
            # Recursive Feedback: Go back to previous phase
            print("\n[!] Re-evaluating previous phase due to feedback...")
            time.sleep(1)
            self.run_phase(phase_index - 1)
            
            # After fixing previous phase, we redo THIS phase
            print(f"\n[!] Returning to {self.phase_map[phase_index]} after fixes...")
            self.run_phase(phase_index)
        else:
            self._print_step(phase_index, "DONE")
            self.run_phase(phase_index + 1)

if __name__ == "__main__":
    project = IterativeWaterfallProject("E-Commerce Portal v2.0")
    project.run_phase(0) # Start at Requirements
