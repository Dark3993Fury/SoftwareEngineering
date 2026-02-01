import time
import sys
import os
import random

def run_simulation():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("BIG BANG MODEL SIMULATION")
    print("="*60)
    print("Project: 24-Hour Hackathon")
    print("Plan: NONE. Just Code!")
    print("="*60 + "\n")
    time.sleep(2)
    
    resources = 100
    print(f"Starting Resources: {resources}%")
    
    # Chaos Phase
    for hour in range(1, 25, 4):
        print(f"\n[Hour {hour}] Coding frantically...")
        event = random.choice([
            "Found a cool library! (+Speed)",
            "Wait, what is this variable name? (-Confusion)",
            "Developer A fell asleep. (-Manpower)",
            "Merge Conflict! We overwrote everything! (-Disaster)"
        ])
        print(f"          Event: {event}")
        time.sleep(1)
        
    print("\n" + "-"*40)
    print("DEADLINE REACHED. DEMO TIME.")
    print("-"*40)
    time.sleep(2)
    
    # Random Outcome
    outcome = random.randint(1, 10)
    
    if outcome > 7:
        print("\nRESULT: [SUCCESS!] Useable Software.")
        print("        Against all odds, it actually works.")
        print("        (Code quality is 0/10, but it runs).")
    elif outcome > 3:
        print("\nRESULT: [AVERAGE] Partial Failure.")
        print("        The main feature is broken, but the UI looks nice.")
    else:
        print("\nRESULT: [COMPLETE FAILURE] Crash Loop.")
        print("        Nothing works. The code is unreadable.")
        print("        \"We should have planned this...\"")

if __name__ == "__main__":
    run_simulation()
