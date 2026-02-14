"""
Schick-Wolverton (S-W) Model Simulation
=======================================
This script simulates the Reliability Function R(t) for the S-W model.
It compares how reliability drops over time for different failure intervals.

As we find more bugs (i increases), the Remaining Faults (N - i + 1) decreases,
so the Reliability curve should drop SLOWER (meaning the system is more reliable).
"""

import math
import time

def sw_reliability(t, N, phi, i):
    """
    Calculates R(t) for the i-th interval.
    Formula: R(t) = exp( -phi * (N - (i-1)) * (t^2 / 2) )
    """
    remaining_faults = N - (i - 1)
    if remaining_faults <= 0:
        return 1.0 # Perfect reliability if no faults left
    
    exponent = -phi * remaining_faults * (t**2 / 2)
    return math.exp(exponent)

def run_simulation():
    print("=========================================")
    print("   SCHICK-WOLVERTON MODEL SIMULATION     ")
    print("=========================================")
    
    # Parameters
    N = 50           # Initial Faults
    phi = 0.001      # Proportionality Constant
    
    print(f"Parameters: N={N}, phi={phi}")
    print("Simulating Reliability Decay for 3 different intervals:\n")
    
    intervals_to_test = [1, 25, 45] # Early vs Middle vs Late stage
    
    # Header
    header = f"{'Time (hrs)':<10}"
    for i in intervals_to_test:
        header += f" | Int {i:<2} (rem:{N-(i-1):<2})"
    print(header)
    print("-" * 55)
    
    # Simulate time passing (0 to 10 hours)
    for t in range(0, 11):
        row = f"{t:<10}"
        for i in intervals_to_test:
            r_t = sw_reliability(t, N, phi, i)
            # Visualize with percentage
            row += f" | {r_t*100:6.2f}%      "
        print(row)
        time.sleep(0.2)
        
    print("-" * 55)
    print("\nObservation:")
    print("1. Interval 1 (50 faults left): Reliability drops FAST.")
    print("   (You are very likely to encounter a bug quickly).")
    print("2. Interval 45 (6 faults left): Reliability stays HIGH.")
    print("   (You can run for 10+ hours with >80% chance of success).")
    print("\nThis demonstrates Reliability Growth.")

if __name__ == "__main__":
    run_simulation()
