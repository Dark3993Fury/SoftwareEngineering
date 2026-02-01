import time
import sys
import os

class IncrementalProject:
    """
    Simulates the Incremental Process Model (Staged Delivery).
    The system is built in 3 increments, each adding specific features.
    """
    
    def __init__(self, name):
        self.name = name
        self.current_features = []
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"INITIALIZING INCREMENTAL PROJECT: {self.name}")
        print("="*60)
        print("Strategy: Staged Delivery")
        print("Goal: Build a full User Management System in steps.")
        print("="*60 + "\n")
        time.sleep(2)

    def _run_stage(self, stage_name):
        print(f"   [-->] {stage_name}...", end="")
        sys.stdout.flush()
        time.sleep(0.6)
        print(" DONE")

    def deliver_increment(self, increment_number, features_to_add):
        print(f"\n+--- STARTING INCREMENT {increment_number}")
        print(f"|    Features to build: {', '.join(features_to_add)}")
        print("|    -------------------------------------------")
        
        # 1. Requirement Analysis for this chunk
        self._run_stage("Requirement Analysis")
        
        # 2. Design & Development
        self._run_stage("Design & Development")
        
        # 3. Testing (New + Regression)
        self._run_stage("Unit Testing")
        if self.current_features:
            self._run_stage("Regression Testing (Checking old features)")
            
        # 4. Implementation
        print("|    [+] DEPLOYING INCREMENT...")
        time.sleep(1)
        
        self.current_features.extend(features_to_add)
        print(f"|    [OK] INCREMENT {increment_number} RELEASED!")
        print(f"|    CURRENT SYSTEM STATE: {self.current_features}")
        print("+-------------------------------------------")
        time.sleep(2)

if __name__ == "__main__":
    project = IncrementalProject("Enterprise Auth System")
    
    # Increment 1: The Core
    project.deliver_increment(1, ["Login", "Register"])
    
    # Increment 2: User Profile
    project.deliver_increment(2, ["Upload Avatar", "Edit Profile", "Change Password"])
    
    # Increment 3: Admin Features
    project.deliver_increment(3, ["Ban User", "View Analytics", "Export Data"])
    
    print("\n" + "="*60)
    print("FINAL PRODUCT DELIVERED SUCCESSFULLY")
