"""
Architectural Patterns Simulation
=================================
This script demonstrates the difference in control flow between:
1. Monolithic (Synchronous/Layered) Architecture
2. Event-Driven (Asynchronous/Distributed) Architecture

Scenario: Placing an E-commerce Order.
"""

import time
import queue
import threading
import random

# ==============================================================================
# 1. MONOLITHIC ARCHITECTURE (Synchronous)
# ==============================================================================
def monolithic_order_flow(order_id):
    print(f"\n[MONOLITH] Starting Order {order_id}...")
    
    # Step 1: Validate (Blocking)
    print(f"   [Controller] -> Calling Service: Validate User...")
    time.sleep(0.5) # Simulating DB call
    
    # Step 2: Payment (Blocking)
    print(f"   [Service]    -> Calling Payment Gateway...")
    time.sleep(0.5) # Simulating API call
    
    # Step 3: Inventory (Blocking)
    print(f"   [Service]    -> Updating Inventory...")
    time.sleep(0.5) 
    
    # Step 4: Email (Blocking)
    print(f"   [Service]    -> Sending Email...")
    time.sleep(0.5)
    
    print(f"[MONOLITH] Order {order_id} Completed! Execution Time: ~2.0s")

# ==============================================================================
# 2. EVENT-DRIVEN ARCHITECTURE (Asynchronous)
# ==============================================================================
class EventBus:
    def __init__(self):
        self.queue = queue.Queue()
        
    def publish(self, event_type, data):
        print(f"   [EventBus]   <-- Event Published: '{event_type}'")
        self.queue.put((event_type, data))

    def consume(self):
        while not self.queue.empty():
            event_type, data = self.queue.get()
            self.dispatch(event_type, data)
            self.queue.task_done()
            
    def dispatch(self, event_type, data):
        # In a real system, these would be separate processes/microservices
        # running in parallel. We simulate this with threads.
        if event_type == "OrderPlaced":
            t1 = threading.Thread(target=self.payment_service, args=(data,))
            t2 = threading.Thread(target=self.inventory_service, args=(data,))
            t3 = threading.Thread(target=self.email_service, args=(data,))
            t1.start(); t2.start(); t3.start()
            t1.join(); t2.join(); t3.join()
            
    def payment_service(self, data):
        time.sleep(random.uniform(0.1, 0.5))
        print(f"   [PaymentSvc] Processed payment for Order {data}")

    def inventory_service(self, data):
        time.sleep(random.uniform(0.1, 0.5))
        print(f"   [StockSvc]   Reserved items for Order {data}")

    def email_service(self, data):
        time.sleep(random.uniform(0.1, 0.5))
        print(f"   [EmailSvc]   Sent confirmation for Order {data}")

def event_driven_order_flow(order_id):
    print(f"\n[EVENT-DRIVEN] Starting Order {order_id}...")
    bus = EventBus()
    
    # The 'Main' process just publishes an event and returns immediately
    # It doesn't wait for email, inventory, etc.
    bus.publish("OrderPlaced", order_id)
    print(f"[EVENT-DRIVEN] Order {order_id} Accepted immediately! (Services working in background...)")
    
    # Simulate background processing
    bus.consume()
    print(f"[EVENT-DRIVEN] All background tasks finished.")

def run_simulation():
    print("=========================================")
    print("   ARCHITECTURE PATTERN SIMULATION       ")
    print("=========================================")
    
    # Monolith
    monolithic_order_flow(101)
    
    print("-" * 40)
    
    # Event Driven
    event_driven_order_flow(202)

if __name__ == "__main__":
    run_simulation()
