"""
Pham-Nordmann-Zhang (PNZ) Model Simulation
==========================================
This script simulates the Software Reliability Growth using the PNZ Model.
It calculates the cumulative number of failures detected over time, 
accounting for:
1. S-Shaped Learning Curve (Testers getting better).
2. Imperfect Debugging (New bugs introduced while fixing old ones).
"""

import math
import time

def pnz_mean_value_function(t, a, b, alpha, beta):
    """
    Calculates m(t): Expected number of faults detected by time t.
    
    Parameters:
    t     : Time (e.g., weeks or hours)
    a     : Initial number of faults
    b     : Fault detection rate
    alpha : Fault introduction rate (imperfect debugging)
    beta  : Inflection factor (S-shape parameter)
    """
    try:
        term1 = (1 - math.exp(-b * t)) * (1 - (alpha / beta))
        term2 = alpha * t
        numerator = a * (term1 + term2)
        denominator = 1 + beta * math.exp(-b * t)
        
        return numerator / denominator
    except ZeroDivisionError:
        return 0

def run_simulation():
    print("=========================================")
    print("   PNZ RELIABILITY MODEL SIMULATION      ")
    print("=========================================")
    print("Simulating a 20-week testing phase...\n")

    # Model Parameters (Example values based on typical research papers)
    # a: Total initial faults expected
    param_a = 100 
    # b: Rate at which faults are detected
    param_b = 0.15 
    # beta: Shape factor (Higher beta = more pronounced S-shape start)
    param_beta = 5.0 
    # alpha: Rate of NEW faults introduced (Imperfect debugging)
    # If alpha is 0, debugging is perfect. 
    # If alpha > 0, we create new bugs!
    param_alpha = 0.5 

    print(f"Parameters:")
    print(f"  Initial Faults (a) : {param_a}")
    print(f"  Detection Rate (b) : {param_b}")
    print(f"  S-Shape Factor (β) : {param_beta}")
    print(f"  Bug Intro Rate (α) : {param_alpha} (Imperfect Debugging!)")
    print("-" * 40)
    print(f"{'Week':<10} | {'Detected (Cumulative)':<25} | {'Reliability Growth'}")
    print("-" * 40)

    previous_m = 0
    
    for t in range(0, 21):
        # Calculate m(t) using PNZ formula
        m_t = pnz_mean_value_function(t, param_a, param_b, param_alpha, param_beta)
        
        # Determine growth (New faults found this week)
        growth = m_t - previous_m
        previous_m = m_t
        
        # Visual Bar
        bar = "█" * int(growth * 2) 
        
        print(f"{t:<10} | {m_t:<25.2f} | {bar}")
        time.sleep(0.2)

    print("-" * 40)
    print("\nAnalysis:")
    print("1. Early weeks showed slow growth (Learning Phase).")
    print("2. Middle weeks showed rapid detection (Inflection Point).")
    print("3. Late weeks continue to find bugs partly due to 'alpha' (New bugs introduced).")
    print("   Unlike other models that plateau completely, PNZ prediction keeps rising")
    print("   if alpha > 0, representing the challenging reality of maintenance.")

if __name__ == "__main__":
    run_simulation()
