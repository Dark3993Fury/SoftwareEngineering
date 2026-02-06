"""
User Interface Design Simulation
================================
An interactive simulation demonstrating UI design concepts including:
- The four phases of UI design
- Theo Mandel's Golden Rules
- UI component interactions
- Feedback mechanisms

Author: Software Engineering Tutorial Series
"""

import time
import random
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Callable
from enum import Enum, auto
from abc import ABC, abstractmethod


# =============================================================================
# ENUMS AND CONSTANTS
# =============================================================================

class UIPhase(Enum):
    """The four phases of User Interface Design Process."""
    ANALYSIS = auto()
    DESIGN = auto()
    IMPLEMENTATION = auto()
    VALIDATION = auto()
    
    def __str__(self):
        descriptions = {
            UIPhase.ANALYSIS: "User, Task & Environmental Analysis",
            UIPhase.DESIGN: "Interface Design",
            UIPhase.IMPLEMENTATION: "Interface Construction & Implementation",
            UIPhase.VALIDATION: "Interface Validation"
        }
        return descriptions[self]


class UserType(Enum):
    """User skill level categories."""
    NOVICE = auto()
    INTERMEDIATE = auto()
    EXPERT = auto()
    
    def __str__(self):
        return self.name.capitalize()


class InteractionMode(Enum):
    """Types of user interaction mechanisms."""
    KEYBOARD = "⌨️ Keyboard"
    MOUSE = "🖱️ Mouse"
    TOUCH = "👆 Touch"
    VOICE = "🎤 Voice"


# =============================================================================
# UI COMPONENTS
# =============================================================================

@dataclass
class UIComponent(ABC):
    """Abstract base class for UI components."""
    id: str
    label: str
    visible: bool = True
    enabled: bool = True
    
    @abstractmethod
    def render(self) -> str:
        """Render the component as text representation."""
        pass
    
    @abstractmethod
    def interact(self) -> str:
        """Handle user interaction with the component."""
        pass


@dataclass
class Button(UIComponent):
    """A clickable button component."""
    action: Optional[Callable] = None
    style: str = "primary"
    
    def render(self) -> str:
        if not self.visible:
            return ""
        state = "🔘" if self.enabled else "⚫"
        return f"{state} [{self.label}]"
    
    def interact(self) -> str:
        if not self.enabled:
            return f"❌ Button '{self.label}' is disabled"
        if self.action:
            self.action()
        return f"✅ Clicked: {self.label}"


@dataclass
class TextInput(UIComponent):
    """A text input field component."""
    value: str = ""
    placeholder: str = "Enter text..."
    max_length: int = 100
    
    def render(self) -> str:
        if not self.visible:
            return ""
        display = self.value if self.value else self.placeholder
        return f"📝 {self.label}: [{display}]"
    
    def interact(self) -> str:
        if not self.enabled:
            return f"❌ Input '{self.label}' is disabled"
        return f"✏️ Ready to type in: {self.label}"
    
    def set_value(self, value: str) -> str:
        """Set the input value with validation."""
        if len(value) > self.max_length:
            return f"⚠️ Text exceeds maximum length of {self.max_length}"
        self.value = value
        return f"✅ Value set: {value}"


@dataclass
class Menu(UIComponent):
    """A menu component with selectable options."""
    options: List[str] = field(default_factory=list)
    selected_index: int = -1
    
    def render(self) -> str:
        if not self.visible:
            return ""
        lines = [f"📋 {self.label}:"]
        for i, option in enumerate(self.options):
            marker = "▶" if i == self.selected_index else "○"
            lines.append(f"  {marker} {option}")
        return "\n".join(lines)
    
    def interact(self) -> str:
        if not self.enabled:
            return f"❌ Menu '{self.label}' is disabled"
        return f"📋 Menu displayed with {len(self.options)} options"
    
    def select(self, index: int) -> str:
        """Select a menu option by index."""
        if 0 <= index < len(self.options):
            self.selected_index = index
            return f"✅ Selected: {self.options[index]}"
        return f"❌ Invalid option index: {index}"


@dataclass
class ProgressBar(UIComponent):
    """A progress indicator component."""
    progress: float = 0.0  # 0.0 to 1.0
    
    def render(self) -> str:
        if not self.visible:
            return ""
        filled = int(self.progress * 20)
        empty = 20 - filled
        bar = "█" * filled + "░" * empty
        return f"📊 {self.label}: [{bar}] {int(self.progress * 100)}%"
    
    def interact(self) -> str:
        return f"Progress: {int(self.progress * 100)}%"
    
    def update(self, value: float) -> None:
        """Update progress value (0.0 to 1.0)."""
        self.progress = max(0.0, min(1.0, value))


# =============================================================================
# GOLDEN RULES IMPLEMENTATION
# =============================================================================

class GoldenRulesDemo:
    """Demonstrates Theo Mandel's Three Golden Rules of UI Design."""
    
    def __init__(self):
        self.action_history: List[str] = []
        self.user_preferences: Dict[str, any] = {}
        self.current_context: str = "Main Menu"
    
    # -------------------------------------------------------------------------
    # Rule 1: Place the User in Control
    # -------------------------------------------------------------------------
    
    def demonstrate_user_control(self):
        """Demonstrate principles of user control."""
        print("\n" + "=" * 60)
        print("🎮 RULE 1: Place the User in Control")
        print("=" * 60)
        
        # Flexible interaction modes
        print("\n📌 Flexible Interaction Modes:")
        for mode in InteractionMode:
            print(f"   {mode.value} - Supported")
        
        # Interruptible and undoable
        print("\n📌 Interruptible & Undoable Actions:")
        self._simulate_undoable_action()
        
        # Customization
        print("\n📌 Customizable Interface:")
        self._simulate_customization()
    
    def _simulate_undoable_action(self):
        """Simulate an undoable action sequence."""
        actions = ["Create Document", "Add Text", "Format Text", "Save Document"]
        print("   Performing actions:")
        for action in actions:
            self.action_history.append(action)
            print(f"      ▶ {action}")
            time.sleep(0.2)
        
        print("\n   User presses Ctrl+Z (Undo):")
        if self.action_history:
            undone = self.action_history.pop()
            print(f"      ↩️ Undone: {undone}")
    
    def _simulate_customization(self):
        """Simulate interface customization."""
        preferences = {
            "theme": ["Light", "Dark", "System"],
            "font_size": ["Small", "Medium", "Large"],
            "layout": ["Compact", "Comfortable", "Expanded"]
        }
        
        for pref, options in preferences.items():
            selected = random.choice(options)
            self.user_preferences[pref] = selected
            print(f"   🔧 {pref.replace('_', ' ').title()}: {selected}")
    
    # -------------------------------------------------------------------------
    # Rule 2: Reduce the User's Memory Load
    # -------------------------------------------------------------------------
    
    def demonstrate_memory_load_reduction(self):
        """Demonstrate principles of reducing memory load."""
        print("\n" + "=" * 60)
        print("🧠 RULE 2: Reduce the User's Memory Load")
        print("=" * 60)
        
        # Meaningful defaults
        print("\n📌 Meaningful Defaults:")
        defaults = {
            "Document Name": "Untitled Document",
            "Font": "Arial, 12pt",
            "Paper Size": "A4 (210 x 297 mm)",
            "Margins": "Normal (2.54 cm)"
        }
        for setting, default in defaults.items():
            print(f"   ⚙️ {setting}: {default}")
        
        # Intuitive shortcuts
        print("\n📌 Intuitive Keyboard Shortcuts:")
        shortcuts = {
            "Ctrl+S": "Save",
            "Ctrl+C": "Copy",
            "Ctrl+V": "Paste",
            "Ctrl+Z": "Undo",
            "Ctrl+P": "Print"
        }
        for key, action in shortcuts.items():
            print(f"   ⌨️ {key} → {action}")
        
        # Real-world metaphors
        print("\n📌 Real-World Metaphors:")
        metaphors = {
            "📁 Folders": "Organize files like physical folders",
            "🗑️ Recycle Bin": "Deleted items go to trash",
            "✂️ Cut & 📋 Paste": "Like scissors and clipboard",
            "🖼️ Desktop": "Main work surface"
        }
        for metaphor, meaning in metaphors.items():
            print(f"   {metaphor}: {meaning}")
    
    # -------------------------------------------------------------------------
    # Rule 3: Make the Interface Consistent
    # -------------------------------------------------------------------------
    
    def demonstrate_consistency(self):
        """Demonstrate principles of interface consistency."""
        print("\n" + "=" * 60)
        print("🔄 RULE 3: Make the Interface Consistent")
        print("=" * 60)
        
        # Navigation context
        print("\n📌 Consistent Navigation Context:")
        breadcrumb = ["Home", "Documents", "Projects", "Current File"]
        print("   Breadcrumb: " + " > ".join(breadcrumb))
        
        # Consistent styling
        print("\n📌 Consistent Button Styling:")
        buttons = [
            ("Save", "primary", "Blue, prominent"),
            ("Cancel", "secondary", "Gray, subtle"),
            ("Delete", "danger", "Red, warning")
        ]
        for label, style, description in buttons:
            print(f"   [{label}] ({style}) - {description}")
        
        # Consistent feedback
        print("\n📌 Consistent Feedback Patterns:")
        feedback_types = [
            ("✅ Success", "Green toast notification"),
            ("⚠️ Warning", "Yellow alert banner"),
            ("❌ Error", "Red error message"),
            ("ℹ️ Info", "Blue information tooltip")
        ]
        for feedback, pattern in feedback_types:
            print(f"   {feedback}: {pattern}")


# =============================================================================
# UI DESIGN PHASES SIMULATION
# =============================================================================

class UIDesignSimulation:
    """Simulates the complete UI Design process through all four phases."""
    
    def __init__(self, project_name: str = "Sample Application"):
        self.project_name = project_name
        self.current_phase = UIPhase.ANALYSIS
        self.phase_progress: Dict[UIPhase, float] = {phase: 0.0 for phase in UIPhase}
        self.user_requirements: List[str] = []
        self.design_artifacts: List[str] = []
        self.prototype_components: List[UIComponent] = []
        self.validation_results: Dict[str, bool] = {}
    
    def run_simulation(self):
        """Run the complete UI design simulation."""
        print("\n" + "🎨" * 30)
        print(f"   USER INTERFACE DESIGN SIMULATION")
        print(f"   Project: {self.project_name}")
        print("🎨" * 30)
        
        self._phase_analysis()
        self._phase_design()
        self._phase_implementation()
        self._phase_validation()
        
        self._show_summary()
    
    def _phase_analysis(self):
        """Execute Phase 1: User, Task & Environmental Analysis."""
        self.current_phase = UIPhase.ANALYSIS
        print(f"\n{'='*60}")
        print(f"📊 PHASE 1: {self.current_phase}")
        print(f"{'='*60}")
        
        # User profiling
        print("\n👥 User Profile Analysis:")
        user_types = [
            (UserType.NOVICE, "40%", "Basic features, guided navigation"),
            (UserType.INTERMEDIATE, "45%", "Standard features, shortcuts"),
            (UserType.EXPERT, "15%", "Advanced features, customization")
        ]
        for user_type, percentage, needs in user_types:
            print(f"   {user_type}: {percentage} - {needs}")
            self._update_progress(0.1)
        
        # Task analysis
        print("\n📋 Task Analysis:")
        tasks = [
            "Create new document",
            "Edit existing content",
            "Save and export",
            "Share with team"
        ]
        for task in tasks:
            self.user_requirements.append(task)
            print(f"   ✓ {task}")
            self._update_progress(0.05)
        
        # Environmental analysis
        print("\n🌍 Environmental Analysis:")
        env_factors = {
            "Location": "Office/Remote (Desktop/Laptop)",
            "Lighting": "Variable, require good contrast",
            "Noise": "Standard office, audio feedback optional",
            "Constraints": "Screen sizes 13\" to 27\""
        }
        for factor, value in env_factors.items():
            print(f"   • {factor}: {value}")
            self._update_progress(0.05)
        
        self.phase_progress[UIPhase.ANALYSIS] = 1.0
        print(f"\n✅ Phase 1 Complete! Progress: 100%")
    
    def _phase_design(self):
        """Execute Phase 2: Interface Design."""
        self.current_phase = UIPhase.DESIGN
        print(f"\n{'='*60}")
        print(f"✏️ PHASE 2: {self.current_phase}")
        print(f"{'='*60}")
        
        # Define UI objects
        print("\n🎯 Defining Interface Objects:")
        objects = ["Navigation Bar", "Content Area", "Sidebar", "Footer", "Modal Dialogs"]
        for obj in objects:
            self.design_artifacts.append(obj)
            print(f"   📦 {obj}")
            self._update_progress(0.1)
        
        # Define actions
        print("\n⚡ Defining User Actions:")
        actions = ["Click", "Double-click", "Drag & Drop", "Keyboard input", "Scroll"]
        for action in actions:
            print(f"   ▶ {action}")
            self._update_progress(0.05)
        
        # User scenarios
        print("\n📖 User Scenarios:")
        scenarios = [
            "New user creates first document",
            "User edits and formats content",
            "User exports document to PDF",
            "User collaborates with team member"
        ]
        for i, scenario in enumerate(scenarios, 1):
            print(f"   Scenario {i}: {scenario}")
            self._update_progress(0.05)
        
        self.phase_progress[UIPhase.DESIGN] = 1.0
        print(f"\n✅ Phase 2 Complete! Progress: 100%")
    
    def _phase_implementation(self):
        """Execute Phase 3: Interface Construction & Implementation."""
        self.current_phase = UIPhase.IMPLEMENTATION
        print(f"\n{'='*60}")
        print(f"🛠️ PHASE 3: {self.current_phase}")
        print(f"{'='*60}")
        
        # Create prototype components
        print("\n🔧 Building Prototype Components:")
        
        # Navigation
        nav_menu = Menu(
            id="main_nav",
            label="Main Navigation",
            options=["Home", "Documents", "Settings", "Help"]
        )
        self.prototype_components.append(nav_menu)
        print(f"\n{nav_menu.render()}")
        self._update_progress(0.15)
        
        # Form elements
        title_input = TextInput(
            id="doc_title",
            label="Document Title",
            placeholder="Enter document title..."
        )
        self.prototype_components.append(title_input)
        print(f"\n{title_input.render()}")
        self._update_progress(0.1)
        
        # Buttons
        save_btn = Button(id="save_btn", label="Save Document", style="primary")
        cancel_btn = Button(id="cancel_btn", label="Cancel", style="secondary")
        self.prototype_components.extend([save_btn, cancel_btn])
        print(f"\n{save_btn.render()}  {cancel_btn.render()}")
        self._update_progress(0.1)
        
        # Progress indicator
        upload_progress = ProgressBar(id="upload", label="Upload Progress", progress=0.0)
        self.prototype_components.append(upload_progress)
        
        print("\n📊 Simulating Upload Progress:")
        for i in range(0, 101, 20):
            upload_progress.update(i / 100)
            print(f"   {upload_progress.render()}")
            time.sleep(0.2)
            self._update_progress(0.05)
        
        self.phase_progress[UIPhase.IMPLEMENTATION] = 1.0
        print(f"\n✅ Phase 3 Complete! Progress: 100%")
    
    def _phase_validation(self):
        """Execute Phase 4: Interface Validation."""
        self.current_phase = UIPhase.VALIDATION
        print(f"\n{'='*60}")
        print(f"✅ PHASE 4: {self.current_phase}")
        print(f"{'='*60}")
        
        # Validation criteria
        print("\n🔍 Running Validation Tests:")
        tests = [
            ("Functionality Test", "All actions work correctly", True),
            ("Usability Test", "Interface easy to use", True),
            ("Accessibility Test", "Meets WCAG 2.1 AA", True),
            ("Performance Test", "Response time < 200ms", True),
            ("Consistency Test", "Design patterns uniform", True),
            ("User Acceptance", "Users find it useful", True)
        ]
        
        for test_name, description, passed in tests:
            self.validation_results[test_name] = passed
            status = "✅ PASSED" if passed else "❌ FAILED"
            print(f"   {status} - {test_name}: {description}")
            self._update_progress(0.15)
            time.sleep(0.2)
        
        # Summary
        passed_count = sum(self.validation_results.values())
        total_count = len(self.validation_results)
        
        print(f"\n📈 Validation Summary: {passed_count}/{total_count} tests passed")
        
        self.phase_progress[UIPhase.VALIDATION] = 1.0
        print(f"\n✅ Phase 4 Complete! Progress: 100%")
    
    def _update_progress(self, increment: float):
        """Update the current phase progress."""
        current = self.phase_progress[self.current_phase]
        self.phase_progress[self.current_phase] = min(1.0, current + increment)
    
    def _show_summary(self):
        """Display the final simulation summary."""
        print("\n" + "=" * 60)
        print("📊 SIMULATION SUMMARY")
        print("=" * 60)
        
        print(f"\n🏷️ Project: {self.project_name}")
        print(f"📋 Requirements Gathered: {len(self.user_requirements)}")
        print(f"🎨 Design Artifacts: {len(self.design_artifacts)}")
        print(f"🧩 Prototype Components: {len(self.prototype_components)}")
        
        print("\n📈 Phase Completion:")
        for phase, progress in self.phase_progress.items():
            bar_filled = int(progress * 20)
            bar = "█" * bar_filled + "░" * (20 - bar_filled)
            print(f"   {str(phase)[:35]:35} [{bar}] {int(progress * 100)}%")
        
        print("\n" + "🎉" * 30)
        print("   UI DESIGN SIMULATION COMPLETE!")
        print("🎉" * 30)


# =============================================================================
# INTERACTIVE DEMO
# =============================================================================

def interactive_demo():
    """Run an interactive demonstration of UI concepts."""
    print("\n" + "=" * 60)
    print("🎨 USER INTERFACE DESIGN - INTERACTIVE DEMO")
    print("=" * 60)
    
    while True:
        print("\n📋 Main Menu:")
        print("   1. Run Full UI Design Simulation")
        print("   2. Explore Golden Rules Demo")
        print("   3. Interact with UI Components")
        print("   4. View UI Types Comparison")
        print("   5. Exit")
        
        try:
            choice = input("\n👉 Enter your choice (1-5): ").strip()
        except EOFError:
            # Non-interactive mode - run demo automatically
            choice = "0"
        
        if choice == "1":
            sim = UIDesignSimulation("Interactive Demo App")
            sim.run_simulation()
            
        elif choice == "2":
            demo = GoldenRulesDemo()
            demo.demonstrate_user_control()
            demo.demonstrate_memory_load_reduction()
            demo.demonstrate_consistency()
            
        elif choice == "3":
            _component_demo()
            
        elif choice == "4":
            _ui_types_comparison()
            
        elif choice == "5":
            print("\n👋 Thank you for exploring UI Design concepts!")
            break
            
        elif choice == "0":
            # Auto-run all demos for non-interactive mode
            print("\n🤖 Running in non-interactive mode...")
            
            # Run simulation
            sim = UIDesignSimulation("Auto Demo Application")
            sim.run_simulation()
            
            # Run golden rules demo
            demo = GoldenRulesDemo()
            demo.demonstrate_user_control()
            demo.demonstrate_memory_load_reduction()
            demo.demonstrate_consistency()
            
            # Show UI types
            _ui_types_comparison()
            
            print("\n👋 Non-interactive demo complete!")
            break
            
        else:
            print("❌ Invalid choice. Please enter 1-5.")


def _component_demo():
    """Interactive demo of UI components."""
    print("\n" + "-" * 40)
    print("🧩 UI COMPONENTS DEMO")
    print("-" * 40)
    
    # Create components
    btn = Button(id="demo_btn", label="Click Me!")
    text = TextInput(id="demo_input", label="Name", placeholder="Enter your name")
    menu = Menu(id="demo_menu", label="Options", options=["Option A", "Option B", "Option C"])
    progress = ProgressBar(id="demo_progress", label="Loading", progress=0.0)
    
    print("\n📦 Available Components:\n")
    print(btn.render())
    print(text.render())
    print(menu.render())
    print(progress.render())
    
    print("\n⚡ Simulating Interactions:\n")
    print(btn.interact())
    
    text.set_value("John Doe")
    print(text.render())
    
    menu.select(1)
    print(menu.render())
    
    for i in range(0, 101, 25):
        progress.update(i / 100)
        print(progress.render())
        time.sleep(0.3)


def _ui_types_comparison():
    """Display comparison of UI types."""
    print("\n" + "-" * 40)
    print("📊 UI TYPES COMPARISON")
    print("-" * 40)
    
    print("""
┌────────────────────┬──────────────────────────────┬──────────────────────────────┐
│ Aspect             │ CLI (Command Line)           │ GUI (Graphical)              │
├────────────────────┼──────────────────────────────┼──────────────────────────────┤
│ Learning Curve     │ Steep - requires commands    │ Gentle - visual cues help    │
│ Speed (Expert)     │ Very Fast                    │ Moderate                     │
│ Speed (Novice)     │ Slow                         │ Moderate to Fast             │
│ Memory Required    │ Low                          │ High                         │
│ Visual Feedback    │ Text-based                   │ Rich visuals                 │
│ Error Handling     │ Technical messages           │ User-friendly dialogs        │
│ Automation         │ Excellent (scripting)        │ Limited                      │
│ Accessibility      │ Screen reader friendly       │ Varies by implementation     │
│ Examples           │ Terminal, PowerShell         │ Windows, macOS, Web Browsers │
└────────────────────┴──────────────────────────────┴──────────────────────────────┘
""")


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

def main():
    """Main entry point for the simulation."""
    print("\n" + "🎨" * 30)
    print("   USER INTERFACE DESIGN")
    print("   Software Engineering Tutorial")
    print("🎨" * 30)
    
    interactive_demo()


if __name__ == "__main__":
    main()
