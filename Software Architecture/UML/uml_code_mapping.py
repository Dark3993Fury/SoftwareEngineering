"""
UML Model to Code Mapping Simulation
====================================
This script demonstrates how UML concepts translate directly into Python Code.

UML Diagram:
1. Class `ATM` aggregates `BankSystem`.
2. Sequence: `User` -> `ATM` -> `BankSystem`.
"""

import time

# ==============================================================================
# 1. CLASS DIAGRAM IMPLEMENTATION
# ==============================================================================

class BankSystem:
    """
    Represents the Backend Bank System (Component in Diagram)
    """
    def __init__(self):
        self._accounts = {"1234": {"pin": "0000", "balance": 1000}}

    def verify_card(self, card_num):
        print(f"   [BankSystem] Verifying Card {card_num}...")
        time.sleep(0.5)
        return card_num in self._accounts

    def validate_pin(self, card_num, pin):
        print(f"   [BankSystem] Validating PIN...")
        time.sleep(0.5)
        return self._accounts[card_num]["pin"] == pin

    def check_balance(self, card_num):
        return self._accounts[card_num]["balance"]

    def withdraw(self, card_num, amount):
        if self._accounts[card_num]["balance"] >= amount:
            self._accounts[card_num]["balance"] -= amount
            print(f"   [BankSystem] Withdrawal Approved. New Balance: ${self._accounts[card_num]['balance']}")
            return True
        print(f"   [BankSystem] Insufficient Funds!")
        return False

class ATM:
    """
    Represents the ATM Machine (Class in Diagram)
    Depending on BankSystem (Association relationship)
    """
    def __init__(self, bank_system: BankSystem):
        self.bank = bank_system
        self.current_card = None

    def insert_card(self, card_num):
        print(f"\n[ATM] Card Inserted: {card_num}")
        if self.bank.verify_card(card_num):
            self.current_card = card_num
            print("[ATM] Card Accepted. Please enter PIN.")
            return True
        else:
            print("[ATM] Card Rejected.")
            return False

    def enter_pin(self, pin):
        if not self.current_card:
            print("[ATM] No card inserted!")
            return False
            
        print(f"[ATM] User entering PIN: ****")
        if self.bank.validate_pin(self.current_card, pin):
            print("[ATM] PIN Correct. Access Granted.")
            return True
        else:
            print("[ATM] Incorrect PIN.")
            return False

    def withdraw_cash(self, amount):
        print(f"[ATM] Requesting Withdrawal: ${amount}...")
        if self.bank.withdraw(self.current_card, amount):
            print("[ATM] Dispensing Cash... 💵")
        else:
            print("[ATM] Transaction Failed.")


# ==============================================================================
# 2. SEQUENCE DIAGRAM SIMULATION (Runtime Behavior)
# ==============================================================================
def run_simulation():
    print("=========================================")
    print("   UML MODEL -> CODE MAPPING             ")
    print("=========================================")
    print("Demonstrating the 'ATM Withdrawal' Sequence Diagram\n")

    # Setup (structural wiring)
    backend = BankSystem()
    atm_machine = ATM(backend)

    # Execution (behavioral sequence)
    # 1. User -> ATM: Insert Card
    if atm_machine.insert_card("1234"):
        
        # 2. User -> ATM: Enter PIN
        if atm_machine.enter_pin("0000"):
            
            # 3. User -> ATM: Withdraw
            atm_machine.withdraw_cash(100)
            
            # 4. Another withdrawal (Exceed balance check)
            atm_machine.withdraw_cash(5000)

if __name__ == "__main__":
    run_simulation()
