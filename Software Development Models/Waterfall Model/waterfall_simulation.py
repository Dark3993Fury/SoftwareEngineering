import time
import sys
import os

class WaterfallProject:
    """
    A simulation of a software project following the Waterfall methodology.
    Enforces strict phase dependencies and sequential execution.
    Visualizes the 'Waterfall' flow in the console.
    """
    
    def __init__(self, name):
        self.name = name
        self.phases = [
            "Requirements Analysis",
            "System Design",
            "Implementation",
            "Verification",
            "Deployment",
            "Maintenance"
        ]
        self.completed_phases = []
        self.indent_level = 0
        
        # Clear screen for better visualization
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"INITIALIZING WATERFALL PROJECT: {self.name}")
        print("="*60)
        print("The Waterfall model dictates that each phase must be completed")
        print("fully before the next phase can begin. There is no overlapping.")
        print("="*60 + "\n")

    def _print_waterfall_step(self, phase_name, status):
        """Helper to print the visual cascading effect"""
        indent = " " * (self.indent_level * 6)
        
        if status == "START":
            print(f"{indent}+--- [PHASE {self.indent_level + 1}: {phase_name.upper()}]")
            print(f"{indent}|    Status: IN PROGRESS...")
        elif status == "WORK":
            # Just vertical lines for previous levels to show continuity if we wanted, 
            # but for waterfall, we just focus on current block.
            pass
        elif status == "DONE":
            print(f"{indent}|    Status: COMPLETED (Signed Off)")
            print(f"{indent}V") 

    def _simulate_work(self, tasks, phase_name):
        self._print_waterfall_step(phase_name, "START")
        
        indent = " " * (self.indent_level * 6)
        prefix = f"{indent}|    "
        
        for task in tasks:
            print(f"{prefix}* {task}...", end="")
            sys.stdout.flush()
            time.sleep(0.5) # Simulating work
            print(" DONE")
            
        self._print_waterfall_step(phase_name, "DONE")
        
        self.completed_phases.append(phase_name)
        self.indent_level += 1
        time.sleep(0.5)

    def run_requirements(self):
        phase_name = "Requirements Analysis"
        tasks = [
            "Conducting stakeholder interviews",
            "Analysing user needs",
            "Drafting Requirement Specification (SRS)",
            "Formal Sign-off"
        ]
        self._simulate_work(tasks, phase_name)

    def run_design(self):
        # Strict Dependency Check
        if "Requirements Analysis" not in self.completed_phases:
            print("ERROR: Cannot start Design. Requirements Analysis not done!")
            return

        phase_name = "System Design"
        tasks = [
            "Creating High-Level Architecture",
            " designing Database Schema",
            "Defining Interfaces (SDD)",
            "Design Review"
        ]
        self._simulate_work(tasks, phase_name)

    def run_implementation(self):
        if "System Design" not in self.completed_phases:
            print("ERROR: Cannot start Implementation. Design not done!")
            return

        phase_name = "Implementation"
        tasks = [
            "Writing Code",
            "Unit Testing Modules",
            "Code Review"
        ]
        self._simulate_work(tasks, phase_name)

    def run_verification(self):
        if "Implementation" not in self.completed_phases:
            print("ERROR: Cannot start Verification. Implementation not done!")
            return

        phase_name = "Verification"
        tasks = [
            "Integration Testing",
            "System Testing",
            "Fixing Bugs",
            "User Acceptance Testing (UAT)"
        ]
        self._simulate_work(tasks, phase_name)

    def run_deployment(self):
        if "Verification" not in self.completed_phases:
            print("ERROR: Cannot start Deployment. Verification not done!")
            return

        phase_name = "Deployment"
        tasks = [
            "Server Configuration",
            "Deploying to Production",
            "Sanity Check"
        ]
        self._simulate_work(tasks, phase_name)

    def run_maintenance(self):
        if "Deployment" not in self.completed_phases:
            print("ERROR: Cannot start Maintenance. Deployment not done!")
            return

        phase_name = "Maintenance"
        tasks = [
            "Monitoring System",
            "Handling User Feedback",
            "Patching Security Issues"
        ]
        self._simulate_work(tasks, phase_name)
        
        print("\n" + "="*60)
        print("PROJECT LIFECYCLE COMPLETED SUCCESSFULLY")
        print("Notice how the process flowed downwards like a waterfall?")
        print("="*60)

if __name__ == "__main__":
    project = WaterfallProject("NextGen Banking System")
    
    try:
        project.run_requirements()
        project.run_design()
        project.run_implementation()
        project.run_verification()
        project.run_deployment()
        project.run_maintenance()
    except Exception as e:
        print(f"An error occurred: {e}")

