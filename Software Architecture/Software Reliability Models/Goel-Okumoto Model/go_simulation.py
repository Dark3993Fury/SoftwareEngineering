"""
Goel-Okumoto (G-O) Model Simulation
===================================
This script simulates the Cumulative Failures m(t) using the G-O Model formula.
It shows how the number of bugs found plateaus over time as 'a' is reached.
"""

import math
import time

def goel_okumoto_mean(t, a, b):
    """
    Calculates m(t) = a * (1 - exp(-b*t))
    """
    return a * (1 - math.exp(-b * t))

def run_simulation():
    print("=========================================")
    print("   GOEL-OKUMOTO MODEL SIMULATION         ")
    print("=========================================")
    print("Simulating a 20-week testing phase...\n")

    # Parameters
    param_a = 150.0  # Total expected faults
    param_b = 0.1    # Detection rate (per week)

    print(f"Parameters:")
    print(f"  Expected Faults (a) : {param_a}")
    print(f"  Detection Rate (b)  : {param_b}")
    print("-" * 55)
    print(f"{'Week':<10} | {'Cumulative Failures (m(t))':<30} | {'Progress'}")
    print("-" * 55)

    previous_m = 0
    
    for t in range(0, 26):
        m_t = goel_okumoto_mean(t, param_a, param_b)
        
        # New bugs found this week
        new_bugs = m_t - previous_m
        previous_m = m_t
        
        # Visual Bar (Total)
        bar = "█" * int(m_t / 5) 
        
        print(f"{t:<10} | {m_t:<30.2f} | {bar}")
        time.sleep(0.1)

    print("-" * 55)
    print("\nAnalysis:")
    print("1. Detection is fast at the beginning (Steep slope).")
    print("2. Detection slows down as 't' increases (Diminishing returns).")
    print("3. Eventually, it approaches 'a' (150).")

if __name__ == "__main__":
    run_simulation()
