import time
import sys
import os
import random

class DevelopmentRace:
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("COMPETITION: Team Waterfall VS Team Agile")
        print("="*60)
        print("Goal: Build a Web Browser in 10 Months.")
        print("Event: CEO demands a NEW FEATURE in Month 4.")
        print("="*60 + "\n")
        time.sleep(2)

    def run(self):
        # Initial State
        waterfall_progress = "Planning"
        agile_progress = "v1.0 Released"
        
        print("\n[MONTH 1-3] Early Phase")
        print(f"Team Waterfall: Deep in {waterfall_progress} phase... (0% Code)")
        print(f"Team Agile:     Running Sprints... {agile_progress} (Basic Features)")
        time.sleep(2)
        
        # The Disruption
        print("\n" + "!"*50)
        print("[MONTH 4] EVENT: CEO wants 'Crypto Wallet' feature ASAP!")
        print("!"*50 + "\n")
        time.sleep(2)
        
        # Team Waterfall Reaction
        print("--- TEAM WATERFALL REACTION ---")
        print("Project Manager: \"We are in Design Phase! We can't add this!\"")
        print("Result: Change Request process started... Delays estimated: 2 Months.")
        print("Status: STALLED.")
        time.sleep(2)
        
        # Team Agile Reaction
        print("\n--- TEAM AGILE REACTION ---")
        print("Scrum Master: \"Okay, adding 'Crypto Wallet' to Sprint 9 backlog.\"")
        print("Result: Feature prioritized for next 2 weeks.")
        print("Status: ADAPTING...")
        time.sleep(2)
        
        # Month 10
        print("\n" + "="*60)
        print("[MONTH 10] FINAL DEADLINE")
        print("="*60)
        
        print("Team Waterfall: Delivered v1.0 (Crypto Wallet is MISSING because it was descaled).")
        print("                User Feedback: \"It feels old-fashioned.\"")
        
        print("\nTeam Agile:     Delivered v1.15 (Includes Crypto Wallet + User requested Dark Mode).")
        print("                User Feedback: \"Exactly what we wanted!\"")
        
        print("\nWINNER: TEAM AGILE (Due to adaptability)")

if __name__ == "__main__":
    race = DevelopmentRace()
    race.run()
