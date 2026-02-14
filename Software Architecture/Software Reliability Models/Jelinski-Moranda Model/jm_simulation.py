"""
Jelinski-Moranda (J-M) Model Simulation
=======================================
This script simulates the Time Between Failures for a software system.
As we fix bugs, the 'Lambda' (Failure Rate) decreases, 
and the 'MTBF' (Mean Time Between Failures) increases.
"""

import random
import math
import time

def simulate_failure_time(failure_rate):
    """
    Generates a random time interval based on Exponential Distribution.
    t = -ln(U) / lambda
    """
    if failure_rate <= 0:
        return float('inf') # No more failures possible!
    
    u = random.random()
    return -math.log(u) / failure_rate

def run_simulation():
    print("=========================================")
    print("   JELINSKI-MORANDA MODEL SIMULATION     ")
    print("=========================================")
    
    # Parameters
    N = 20           # Total Initial Faults
    phi = 0.01       # Proportionality Constant
    
    print(f"Parameters: N={N}, phi={phi}")
    print("Simulating the debugging process...\n")
    
    print(f"{'Fault #':<10} | {'Remaining':<10} | {'Failure Rate (λ)':<20} | {'Expected MTBF (hrs)':<20} | {'Actual Sim Time'}")
    print("-" * 90)
    
    total_time = 0
    
    for i in range(1, N + 1):
        remaining = N - (i - 1)
        lambd = phi * remaining
        
        expected_mtbf = 1.0 / lambd
        
        # Simulate actual time to find this bug
        actual_time = simulate_failure_time(lambd)
        total_time += actual_time
        
        print(f"{i:<10} | {remaining:<10} | {lambd:<20.4f} | {expected_mtbf:<20.2f} | {actual_time:.2f}")
        time.sleep(0.1)
        
        if i >= 15:
            print("... (Stopping simulation early as MTBF gets huge) ...")
            break

    print("-" * 90)
    print("\nObservation:")
    print("As 'Remaining Faults' drops, the 'Failure Rate' drops linearly.")
    print("Consequently, the MTBF (Mean Time Between Failures) grows exponentially.")
    print("Finding the last few bugs takes a VERY long time!")

if __name__ == "__main__":
    run_simulation()
