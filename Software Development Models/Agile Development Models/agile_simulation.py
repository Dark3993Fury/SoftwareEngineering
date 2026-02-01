import time
import sys
import os
import random

class AgileSprint:
    """
    Simulates an Agile Sprint Cycle.
    Demonstrates: Backlog Selection -> Development -> Deployment -> User Feedback.
    """
    
    def __init__(self, name):
        self.name = name
        self.backlog = [
            "User Login", "Dark Mode", "Payment Gateway", 
            "Chat System", "Search Bar", "Notifications"
        ]
        self.sprint_count = 1
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"INITIALIZING AGILE PROJECT: {self.name}")
        print("="*60)
        print("Methodology: Scrum / Agile")
        print("Cycle: 2-Week Sprints")
        print("="*60 + "\n")
        time.sleep(2)

    def run_sprint(self):
        if not self.backlog:
            print("\n[!] Product Backlog is Empty! Project Complete.")
            return False

        print(f"\n+--- STARTING SPRINT {self.sprint_count}")
        print(f"|    Product Backlog: {len(self.backlog)} items remaining")
        
        # Sprint Planning: Pick 2 items
        sprint_tasks = self.backlog[:2]
        self.backlog = self.backlog[2:]
        print(f"|    [PLANNING] Selected for this Sprint: {sprint_tasks}")
        time.sleep(1)
        
        # Development
        print("|    [DEV] Coding & Testing...", end="")
        sys.stdout.flush()
        time.sleep(1)
        print(" DONE")
        
        # Deployment
        print("|    [DEPLOY] Releasing v1.{}".format(self.sprint_count))
        
        # Feedback Loop
        print("|    [FEEDBACK] Gathering User Input...")
        time.sleep(1)
        
        feedback = random.choice([
            "Great work! No changes needed.",
            "Great work! No changes needed.",
            "Bug found in payment! (Added to backlog)",
            "We need a 'Share' button! (Added to backlog)"
        ])
        
        print(f"|    >> User says: '{feedback}'")
        
        if "Added to backlog" in feedback:
            new_item = "Bug Fix / New Feature"
            self.backlog.append(new_item)
            print(f"|    [+] '{new_item}' added to backlog.")
            
        print("+-------------------------------------------")
        self.sprint_count += 1
        return True

if __name__ == "__main__":
    project = AgileSprint("Ride Sharing App")
    
    # Run a few sprints
    while project.sprint_count <= 3:
        project.run_sprint()
        time.sleep(1)
    
    print("\n... Sprints continue until backlog is empty ...")
