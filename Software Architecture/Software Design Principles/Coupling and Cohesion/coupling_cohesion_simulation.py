"""
Coupling and Cohesion Simulation
================================
This script demonstrates the practical difference between:
1. High Coupling / Low Cohesion (The "Anti-Pattern")
2. Low Coupling / High Cohesion (The "Best Practice")

It simulates a simple E-commerce Order Processing flow.
"""

import time
import random

# ==============================================================================
# SCENARIO 1: BAD DESIGN (High Coupling, Low Cohesion)
# ==============================================================================
print("\n" + "❌" * 30)
print(" SCENARIO 1: The 'Spaghetti' System")
print(" (High Coupling, Low Cohesion)")
print("❌" * 30)

# PROBLEM 1: Common Coupling (Shared Global Data)
# Any module can change this, making bugs hard to track.
GLOBAL_CART = []
GLOBAL_USER_BALANCE = 1000
GLOBAL_INVENTORY = {"Laptop": 5, "Phone": 10}

class GodObjectManager:
    """
    PROBLEM 2: Coincidental/Logical Cohesion
    This class does EVERYTHING. It mixes User logic, Inventory logic,
    Billing logic, and Email logic.
    """
    
    def do_everything(self, action, item_name=None, price=0):
        # PROBLEM 3: Control Coupling
        # The 'action' string controls internal flow. 
        # Adding a new action means modifying this huge method (Violates Open/Closed).
        
        global GLOBAL_USER_BALANCE
        
        if action == "add_to_cart":
            print(f"   [GodObject] Adding {item_name} to global cart...")
            # Direct access to global data
            GLOBAL_CART.append({"name": item_name, "price": price})
            
        elif action == "checkout":
            print("   [GodObject] Starting checkout process...")
            total = sum(item['price'] for item in GLOBAL_CART)
            
            # Content Coupling-ish: Changing global state directly everywhere
            if GLOBAL_USER_BALANCE >= total:
                GLOBAL_USER_BALANCE -= total
                print(f"   [GodObject] Charged ${total}. New Balance: ${GLOBAL_USER_BALANCE}")
                
                # Logical Cohesion: Why is the 'Manager' directly printing receipts?
                print("   [GodObject] Printing Receipt: " + ", ".join([i['name'] for i in GLOBAL_CART]))
                
                # Temporal Cohesion: Doing inventory update right here because "it happens at the same time"
                for item in GLOBAL_CART:
                    name = item['name']
                    if name in GLOBAL_INVENTORY:
                        GLOBAL_INVENTORY[name] -= 1
                        print(f"   [GodObject] Inventory updated for {name}")
                
                GLOBAL_CART.clear()
            else:
                print("   [GodObject] Insufficient funds!")

        elif action == "send_email":
            # Why is email logic in the same class as inventory management?
            print("   [GodObject] Sending generic email to user...")

# Run Bad Scenario
bad_system = GodObjectManager()
bad_system.do_everything("add_to_cart", "Laptop", 800)
bad_system.do_everything("add_to_cart", "Phone", 100)
bad_system.do_everything("checkout")


# ==============================================================================
# SCENARIO 2: GOOD DESIGN (Low Coupling, High Cohesion)
# ==============================================================================
print("\n" + "✅" * 30)
print(" SCENARIO 2: The 'Modular' System")
print(" (Low Coupling, High Cohesion)")
print("✅" * 30)

# SOLUTION 1: Data Encapsulation (No Globals)

class InventoryService:
    """High Cohesion: Responsible ONLY for Inventory."""
    def __init__(self):
        self._stock = {"Laptop": 5, "Phone": 10}
        
    def check_stock(self, item_name):
        return self._stock.get(item_name, 0) > 0
        
    def reduce_stock(self, item_name):
        if self.check_stock(item_name):
            self._stock[item_name] -= 1
            print(f"   [Inventory] Reduced stock for {item_name}. Remaining: {self._stock[item_name]}")
            return True
        return False

class BillingService:
    """High Cohesion: Responsible ONLY for Money."""
    def __init__(self, balance):
        self._balance = balance
        
    def process_payment(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"   [Billing] Payment of ${amount} successful. Balance: ${self._balance}")
            return True
        print(f"   [Billing] Payment Failed. Insufficient funds.")
        return False

class NotificationService:
    """High Cohesion: Responsible ONLY for Communication."""
    def send_confirmation(self, items):
        item_list = ", ".join(items)
        print(f"   [Email] Sent order confirmation for: {item_list}")

class OrderController:
    """
    Low Coupling: Orchestrates the work.
    Depends on abstractions/services, not globals.
    """
    def __init__(self, inventory: InventoryService, billing: BillingService, notifier: NotificationService):
        # Component Coupling: References injected services (Good practice usually)
        self.inventory = inventory
        self.billing = billing
        self.notifier = notifier
        self.cart = []
        
    def add_item(self, name, price):
        if self.inventory.check_stock(name):
            self.cart.append({"name": name, "price": price})
            print(f"   [Order] Added {name} to cart.")
        else:
            print(f"   [Order] Could not add {name} - Out of Stock!")
            
    def checkout(self):
        if not self.cart:
            return
            
        total = sum(item['price'] for item in self.cart)
        
        # Data Coupling: Passing only necessary data (amount) to billing
        if self.billing.process_payment(total):
            # Sequential Cohesion in the flow: Pay -> Update Stock -> Notify
            item_names = [i['name'] for i in self.cart]
            
            for name in item_names:
                self.inventory.reduce_stock(name)
                
            self.notifier.send_confirmation(item_names)
            self.cart.clear()

# Run Good Scenario
# Setup independent modules
inventory_svc = InventoryService()
billing_svc = BillingService(1000)
email_svc = NotificationService()

# Inject dependencies (Low Coupling pattern)
order_system = OrderController(inventory_svc, billing_svc, email_svc)

order_system.add_item("Laptop", 800)
order_system.add_item("Phone", 100)
order_system.checkout()

print("\n" + "="*60)
print(" ANALYSIS")
print("="*60)
print("""
1. Maintainability:
   - Bad: Changing 'Inventory' logic might break 'Billing' in GodObject.
   - Good: You can rewrite 'InventoryService' completely without touching 'BillingService'.

2. Testing:
   - Bad: To test 'checkout', you must set up correct global state.
   - Good: You can mock 'BillingService' to test 'OrderController' in isolation.

3. Reusability:
   - Bad: You can't use 'GodObject' in another project that doesn't need 'Billing'.
   - Good: 'NotificationService' can be dropped into any other project easily.
""")
