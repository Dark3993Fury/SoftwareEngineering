"""
Reliability Metrics Calculator
==============================
This script calculates MTBF, MTTF, MTTR, and Availability from raw system logs.

Scenario: A server that crashes and gets rebooted multiple times.
"""

def calculate_metrics(incidents):
    """
    Incidents is a list of tuples: (start_time, failure_time, repair_end_time)
    start_time     : When system started running (or restarted)
    failure_time   : When system crashed
    repair_end_time: When system was fixed and running again
    """
    total_uptime = 0
    total_downtime = 0
    failures = len(incidents)
    
    print(f"\n{'-'*60}")
    print(f"{'Incident':<10} | {'Uptime (hrs)':<15} | {'Downtime (hrs)':<15}")
    print(f"{'-'*60}")
    
    for i, (start, fail, end) in enumerate(incidents):
        uptime = fail - start
        downtime = end - fail
        
        total_uptime += uptime
        total_downtime += downtime
        
        print(f"{i+1:<10} | {uptime:<15.2f} | {downtime:<15.2f}")

    # Calculations
    mttf = total_uptime / failures
    mttr = total_downtime / failures
    mtbf = mttf + mttr
    availability = mttf / mtbf * 100

    return mttf, mttr, mtbf, availability

def run_simulation():
    print("=========================================")
    print("   RELIABILITY METRICS CALCULATOR        ")
    print("=========================================")
    
    # Simulated Logs (Time in hours)
    # (Start, Crash, Fixed)
    logs = [
        (0.0,  100.0, 102.0), # Ran for 100h, took 2h to fix
        (102.0, 250.0, 255.0), # Ran for 148h, took 5h to fix
        (255.0, 300.0, 301.0), # Ran for 45h,  took 1h to fix
        (301.0, 600.0, 604.0), # Ran for 299h, took 4h to fix
    ]
    
    mttf, mttr, mtbf, avail = calculate_metrics(logs)
    
    print(f"{'-'*60}")
    print("\n📊 RESULTS:")
    print(f"   Total Failures: {len(logs)}")
    print(f"   MTTF (Avg Uptime)   : {mttf:.2f} hours")
    print(f"   MTTR (Avg Fix Time) : {mttr:.2f} hours")
    print(f"   MTBF (Total Cycle)  : {mtbf:.2f} hours")
    print(f"   -------------------------------")
    print(f"   Availability        : {avail:.4f}%")

if __name__ == "__main__":
    run_simulation()
