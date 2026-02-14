"""
Design Patterns Simulation (Smart Home)
=======================================
This script demonstrates multiple patterns working together:
1. Singleton: HomeAssistant (Central Hub)
2. Factory: DeviceFactory (Creates devices)
3. Adapter: Retrofiting an old 'LegacyFan' to work with smart home.
4. Observer: Security System listening to Sensors.
5. Strategy: Thermostat cooling strategies.
"""

from abc import ABC, abstractmethod

# ==============================================================================
# 1. SINGLETON (The Central Hub)
# ==============================================================================
class HomeAssistant:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print("[Singleton] Creating HomeAssistant Hub...")
            cls._instance = super(HomeAssistant, cls).__new__(cls)
            cls._instance.devices = []
        return cls._instance

    def add_device(self, device):
        self.devices.append(device)
        print(f"[Hub] Added device: {device.name}")

# ==============================================================================
# 2. FACTORY (Device Creation)
# ==============================================================================
class SmartDevice(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def turn_on(self): pass

class Light(SmartDevice):
    def turn_on(self): print(f"   💡 {self.name}: Lighting up room!")

class Lock(SmartDevice):
    def turn_on(self): print(f"   🔒 {self.name}: Locked secure.")

class DeviceFactory:
    @staticmethod
    def create_device(type, name):
        if type == "light": return Light(name)
        elif type == "lock": return Lock(name)
        else: raise ValueError("Unknown device type")

# ==============================================================================
# 3. ADAPTER (Legacy Device)
# ==============================================================================
class OldAnalogueFan:
    """A legacy device that doesn't share the 'SmartDevice' interface"""
    def pull_string(self):
        print("   🕸️ Old Fan: Whirrrr... (Pulled string)")

class FanAdapter(SmartDevice):
    def __init__(self, old_fan: OldAnalogueFan):
        super().__init__("Smart Fan (Adapted)")
        self.old_fan = old_fan
        
    def turn_on(self):
        print("[Adapter] Converting signal to mechanical pull...")
        self.old_fan.pull_string()

# ==============================================================================
# 4. OBSERVER (Security System)
# ==============================================================================
class MotionSensor:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detect_movement(self):
        print("\n[Sensor] 🏃 MOVEMENT DETECTED!")
        for observer in self._observers:
            observer.update()

class SecuritySystem:
    def update(self):
        print("   🚨 SecuritySystem: ALARM TRIGGERED! Calling Police!")

class SmartLightObserver:
    def update(self):
        print("   💡 SmartLight: Turning on fully bright to scare intruder!")

# ==============================================================================
# 5. STRATEGY (Thermostat)
# ==============================================================================
class CoolingStrategy(ABC):
    @abstractmethod
    def cool(self): pass

class EcoCooling(CoolingStrategy):
    def cool(self): print("   🌱 Thermostat: Using Fan only (Eco Mode)")

class TurboCooling(CoolingStrategy):
    def cool(self): print("   ❄️ Thermostat: AC Compressor MAX (Turbo Mode)")

class Thermostat:
    def __init__(self, strategy: CoolingStrategy):
        self.strategy = strategy
        
    def execute_cooling(self):
        self.strategy.cool()

# ==============================================================================
# MAIN SIMULATION
# ==============================================================================
def run_simulation():
    print("=========================================")
    print("   GENIUS SMART HOME (Design Patterns)   ")
    print("=========================================")
    
    # 1. Singleton
    hub = HomeAssistant()
    
    # 2. Factory
    light = DeviceFactory.create_device("light", "Living Room Light")
    hub.add_device(light)
    
    # 3. Adapter
    old_fan = OldAnalogueFan()
    smart_fan = FanAdapter(old_fan)
    hub.add_device(smart_fan)
    
    print("\n--- Testing Devices ---")
    light.turn_on()
    smart_fan.turn_on()
    
    print("\n--- Strategy Pattern (Thermostat) ---")
    thermostat = Thermostat(EcoCooling())
    thermostat.execute_cooling()
    
    # Switch Strategy dynamically
    print("   (It's getting hot!)")
    thermostat.strategy = TurboCooling()
    thermostat.execute_cooling()
    
    print("\n--- Observer Pattern (Intruder) ---")
    sensor = MotionSensor()
    security = SecuritySystem()
    hallway_light = SmartLightObserver()
    
    sensor.attach(security)
    sensor.attach(hallway_light)
    
    sensor.detect_movement()

if __name__ == "__main__":
    run_simulation()
