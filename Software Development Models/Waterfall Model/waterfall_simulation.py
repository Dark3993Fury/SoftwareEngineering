import time
import sys

class WaterfallProject:
    """
    A simulation of a software project following the Waterfall methodology.
    Enforces strict phase dependencies and sequential execution.
    """
    
    def __init__(self, name):
        self.name = name
        self.current_phase_index = 0
        self.phases = [
            "Requirements Analysis",
            "System Design",
            "Implementation",
            "Verification",
            "Deployment",
            "Maintenance"
        ]
        self.completed_phases = []
        print(f"\n🚀 INITIALIZING WATERFALL PROJECT: {self.name}")
        print("="*60)

    def _log_phase_start(self, phase_name):
        print(f"\n[PHASE {self.current_phase_index + 1}: {phase_name.upper()}]")
        print("-" * 40)

    def _simulate_work(self, tasks):
        for task in tasks:
            print(f"  • {task}...", end="")
            sys.stdout.flush()
            time.sleep(0.8) # Simulating work duration
            print(" DONE")
        print(f"  ✅ {self.phases[self.current_phase_index]} Phase Sign-off Complete.")
        self.completed_phases.append(self.phases[self.current_phase_index])
        self.current_phase_index += 1

    def run_requirements(self):
        if self.current_phase_index != 0:
            raise Exception("❌ VIOLATION: Must start with Requirements!")
        
        self._log_phase_start("Requirements")
        tasks = [
            "Conducting stakeholder interviews",
            "Identifying functional requirements",
            "Analyzing feasibility",
            "Drafting Software Requirement Specification (SRS)",
            "Getting Client Sign-off on SRS"
        ]
        self._simulate_work(tasks)

    def run_design(self):
        if "Requirements Analysis" not in self.completed_phases:
            print("❌ BLOCKED: Cannot start Design. SRS not signed off!")
            return

        self._log_phase_start("Design")
        tasks = [
            "Creating High-Level Architecture (HLD)",
            "Designing Database Schema",
            "Defining API Interfaces (LLD)",
            "Writing Software Design Document (SDD)"
        ]
        self._simulate_work(tasks)

    def run_implementation(self):
        if "System Design" not in self.completed_phases:
            print("❌ BLOCKED: Cannot start Implementation. Design not approved!")
            return

        self._log_phase_start("Implementation")
        tasks = [
            "Setting up development environment",
            " Implementing User Authentication Module",
            "Implementing Core Logic",
            "Performing Unit Testing",
            "Code Review"
        ]
        self._simulate_work(tasks)

    def run_verification(self):
        if "Implementation" not in self.completed_phases:
            print("❌ BLOCKED: Cannot start Testing. Code not ready!")
            return

        self._log_phase_start("Verification")
        tasks = [
            "Performing Integration Testing",
            "Executing System Test Cases",
            "Reporting Defects",
            "Verifying Fixes",
            "User Acceptance Testing (UAT)"
        ]
        self._simulate_work(tasks)

    def run_deployment(self):
        if "Verification" not in self.completed_phases:
            print("❌ BLOCKED: Cannot Deploy. Software not verified!")
            return

        self._log_phase_start("Deployment")
        tasks = [
            "Configuring Production Server",
            "Migrating Database",
            "Deploying Release Build v1.0",
            "Sanity Check"
        ]
        self._simulate_work(tasks)

    def run_maintenance(self):
        if "Deployment" not in self.completed_phases:
            print("❌ BLOCKED: Cannot Maintain. System not live!")
            return

        self._log_phase_start("Maintenance")
        tasks = [
            "Monitoring System Health",
            "Patching Critical Security Bug",
            "Optimizing Database Queries"
        ]
        self._simulate_work(tasks)
        print("\n" + "="*60)
        print("🎉 PROJECT LIFECYCLE COMPLETED SUCCESSFULLY")

if __name__ == "__main__":
    # Correct Execution Flow
    project = WaterfallProject("NextGen Banking System")
    
    try:
        # Example of strict sequential execution
        project.run_requirements()
        project.run_design()
        project.run_implementation()
        project.run_verification()
        project.run_deployment()
        project.run_maintenance()
        
    except Exception as e:
        print(e)
