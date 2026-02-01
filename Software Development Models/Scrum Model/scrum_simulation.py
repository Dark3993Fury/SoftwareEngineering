import time
import sys
import os
import random

def daily_standup():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("SCRUM SIMULATION: The Daily Standup")
    print("="*60)
    print("Time: 10:00 AM")
    print("Goal: Answer 3 Questions in 15 mins.")
    print("1. What did you do yesterday?")
    print("2. What will you do today?")
    print("3. Are there any blockers?")
    print("="*60 + "\n")
    time.sleep(2)

    team_members = ["Alice (Frontend)", "Bob (Backend)", "Charlie (QA)", "YOU (Fullstack)"]
    
    for member in team_members:
        print(f"\n--- {member}'s Turn ---")
        time.sleep(1)
        
        if member == "YOU (Fullstack)":
            print("Your Request: Give your update.")
            print("(Simulation auto-filling for you...)")
            time.sleep(1)
            print("YOU: \"Yesterday, I fixed the Login API.\"")
            print("     \"Today, I'm integrating the Payment Gateway.\"")
            
            # Random Chance of Blocker
            if random.random() > 0.5:
                print("     \"BLOCKER: I'm waiting for the API Keys from the Client.\"")
                print("\n[SCRUM MASTER]: \"Thanks. I'll email the client right now to unblock you.\"")
            else:
                print("     \"NO BLOCKERS.\"")
                print("\n[SCRUM MASTER]: \"Great, keep pushing.\"")
        
        else:
            # Random status for bots
            work = ["refactoring CSS", "optimizing DB", "writing test cases", "updating docs"]
            print(f"{member.split()[0]}: \"Yesterday I was {random.choice(work)}.\"")
            print(f"          \"Today I am continuing that.\"")
            print("          \"No blockers.\"")
            
        time.sleep(1.5)
    
    print("\n" + "="*60)
    print("STANDUP COMPLETE (Time: 12 minutes)")
    print("Everyone back to work!")

if __name__ == "__main__":
    daily_standup()
