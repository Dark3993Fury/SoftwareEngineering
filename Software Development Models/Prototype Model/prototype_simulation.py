import time
import sys
import os
import random

class PrototypeSimulation:
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("PROTOTYPE MODEL SIMULATION")
        print("="*60)
        print("Goal: Build a Login Screen that the Client loves.")
        print("Process: Build -> Show Client -> Get Feedback -> Fix.")
        print("="*60 + "\n")
        time.sleep(2)
        
        self.version = 1
        self.approved = False

    def build_prototype(self):
        print(f"\n--- Building Prototype v{self.version} ---")
        print("    [DEV] Coding quick UI mock-up...")
        time.sleep(1.5)
        print("    [DEV] Done. Sending to client.")

    def client_evaluation(self):
        print(f"\n--- Client Review v{self.version} ---")
        time.sleep(1)
        
        # Simulated Client Feedback Logic
        if self.version == 1:
            print("    [CLIENT]: \"I don't like the color. Make it Blue.\"")
            print("    [DECISION]: REJECTED. Back to design.")
            return False
        elif self.version == 2:
            print("    [CLIENT]: \"Better. But the 'Login' button is too small.\"")
            print("    [DECISION]: REJECTED. Back to design.")
            return False
        else:
            print("    [CLIENT]: \"PERFECT! This is exactly what I wanted.\"")
            print("    [DECISION]: APPROVED! Proceed to final development.")
            return True

    def run(self):
        while not self.approved:
            self.build_prototype()
            if self.client_evaluation():
                self.approved = True
                break
            else:
                print("    [PM]: Note taken. Refining requirements...")
                self.version += 1
                time.sleep(2)
        
        print("\n" + "="*60)
        print("FINAL PHASE: discard prototype code & write Production Code.")
        print("PROJECT SUCCESSFUL.")

if __name__ == "__main__":
    sim = PrototypeSimulation()
    sim.run()
