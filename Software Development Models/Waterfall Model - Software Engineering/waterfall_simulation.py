import time

class WaterfallProject:
    def __init__(self, project_name):
        self.project_name = project_name
        self.phases = {
            "Requirements": False,
            "Design": False,
            "Development": False,
            "Testing": False,
            "Deployment": False,
            "Maintenance": False
        }
        print(f"--- Initializing Waterfall Project: {self.project_name} ---")

    def _check_dependency(self, previous_phase):
        if previous_phase and not self.phases[previous_phase]:
            print(f"ERROR: Cannot proceed. Previous phase '{previous_phase}' is not complete!")
            return False
        return True

    def start_requirements_analysis(self):
        print("\n[Phase 1] Requirements Analysis & Specification")
        print("   - Gathering customer needs...")
        print("   - Documenting Software Requirement Specification (SRS)...")
        time.sleep(1)
        self.phases["Requirements"] = True
        print("   -> Requirements Phase COMPLETED.")

    def start_design(self):
        if not self._check_dependency("Requirements"): return
        
        print("\n[Phase 2] System Design")
        print("   - Creating High-Level Design (HLD)...")
        print("   - Creating Low-Level Design (LLD)...")
        print("   - Documenting Software Design Document (SDD)...")
        time.sleep(1)
        self.phases["Design"] = True
        print("   -> Design Phase COMPLETED.")

    def start_development(self):
        if not self._check_dependency("Design"): return

        print("\n[Phase 3] Development (Implementation)")
        print("   - Writing source code...")
        print("   - Performing Unit Testing...")
        time.sleep(1)
        self.phases["Development"] = True
        print("   -> Development Phase COMPLETED.")

    def start_testing(self):
        if not self._check_dependency("Development"): return

        print("\n[Phase 4] Testing")
        print("   - Integration Testing...")
        print("   - System Testing...")
        print("   - User Acceptance Testing (Alpha/Beta)...")
        time.sleep(1)
        self.phases["Testing"] = True
        print("   -> Testing Phase COMPLETED.")

    def start_deployment(self):
        if not self._check_dependency("Testing"): return

        print("\n[Phase 5] Deployment")
        print("   - Setting up production environment...")
        print("   - Deploying software...")
        self.phases["Deployment"] = True
        print("   -> Deployment COMPLETED. Software is LIVE.")

    def start_maintenance(self):
        if not self._check_dependency("Deployment"): return

        print("\n[Phase 6] Maintenance")
        print("   - Monitoring system...")
        print("   - Performing Corrective Maintenance (Bug fixes)...")
        print("   - Performing Adaptive Maintenance (Updates)...")
        self.phases["Maintenance"] = True
        print("   -> Maintenance Initiated.")

if __name__ == "__main__":
    # Example Usage
    app = WaterfallProject("Online Food Delivery System")
    
    # Try skipping to Development (Should Fail)
    print("\n--- Testing Strict Sequence ---")
    app.start_development() 
    
    # Correct Sequence
    print("\n--- Execute Correct Flow ---")
    app.start_requirements_analysis()
    app.start_design()
    app.start_development()
    app.start_testing()
    app.start_deployment()
    app.start_maintenance()
