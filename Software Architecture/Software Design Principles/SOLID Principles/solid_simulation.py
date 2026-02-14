"""
SOLID Principles Simulation
===========================
This script demonstrates the difference between:
1. VIOLATING SOLID (The 'Bad' way)
2. FOLLOWING SOLID (The 'Good' way)

Focus: Open/Closed Principle (OCP) and Single Responsibility (SRP).
Scenario: A Notification System.
"""

# ==============================================================================
# ❌ BAD DESIGN (Violates OCP & SRP)
# ==============================================================================
class NotificationManagerBad:
    """
    This class does too much (Violates SRP).
    And if we want to add 'SMS', we must modify the code (Violates OCP).
    """
    def send_notification(self, type, message):
        if type == "email":
            print(f"   [BAD] Sending EMAIL: {message}")
            # Logic for email...
        elif type == "push":
            print(f"   [BAD] Sending PUSH: {message}")
            # Logic for push...
        else:
            print("   [BAD] Unknown type.")

# ==============================================================================
# ✅ GOOD DESIGN (Follows SOLID)
# ==============================================================================
from abc import ABC, abstractmethod

# 1. Interface (DIP / ISP)
class NotificationSender(ABC):
    @abstractmethod
    def send(self, message):
        pass

# 2. Concrete Implementations (SRP)
class EmailSender(NotificationSender):
    def send(self, message):
        print(f"   [GOOD] 📧 EmailSender: {message}")

class PushSender(NotificationSender):
    def send(self, message):
        print(f"   [GOOD] 🔔 PushSender: {message}")

class SMSSender(NotificationSender):
    def send(self, message):
        print(f"   [GOOD] 📱 SMSSender: {message}")

# 3. Manager (OCP - Works with ANY sender)
class NotificationService:
    def __init__(self, sender: NotificationSender):
        # Dependence Inversion: Depends on Abstraction, not concrete class
        self.sender = sender
        
    def notify(self, msg):
        self.sender.send(msg)

# ==============================================================================
# SIMULATION
# ==============================================================================
def run_simulation():
    print("=========================================")
    print("   SOLID PRINCIPLES SIMULATION           ")
    print("=========================================")
    
    print("\n1. ❌ BAD DESIGN (Rigid)")
    bad_manager = NotificationManagerBad()
    bad_manager.send_notification("email", "Hello World")
    bad_manager.send_notification("push", "Update Available")
    
    print("-" * 40)
    
    print("\n2. ✅ GOOD DESIGN (Flexible)")
    # We can easily swap implementations without changing the Service logic!
    
    email_service = NotificationService(EmailSender())
    email_service.notify("Hello SOLID World")
    
    push_service = NotificationService(PushSender())
    push_service.notify("SOLID is great")
    
    # Adding SMS didn't require changing NotificationService! (OCP)
    sms_service = NotificationService(SMSSender())
    sms_service.notify("New Feature Added easily!")

if __name__ == "__main__":
    run_simulation()
