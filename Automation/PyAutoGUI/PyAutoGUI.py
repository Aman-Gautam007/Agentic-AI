import pyautogui
"""
Module: PyAutoGUI Automation Examples

Description:
This module demonstrates basic PyAutoGUI functionality for GUI automation tasks.
PyAutoGUI is a cross-platform Python module for programmatically controlling the mouse
and keyboard. This script shows how to move the mouse, click, type text, and capture screenshots.

Functions/Operations Demonstrated:
- Mouse movement to specific coordinates with duration control
- Mouse clicking at the current position
- Keyboard text input with customizable intervals
- Screenshot capture for screen monitoring

Safety Features:
- FAILSAFE is enabled to prevent accidental automation issues by allowing quick cursor
    movement to screen corners to interrupt the script

Use Cases:
- Automating repetitive GUI tasks
- Testing GUI applications
- Creating bots for interactive applications
- Screen monitoring and documentation

Dependencies:
- pyautogui: For mouse and keyboard automation
- time: For timing control (imported but not used in examples)

Warning:
Use this module responsibly and only on systems where you have permission to automate tasks.
Automated mouse and keyboard control can be dangerous if misused.
"""
import time

# Set a safety margin to prevent accidental misclicks
pyautogui.FAILSAFE = True

# Example: Move mouse to position (100, 100)
pyautogui.moveTo(100, 100, duration=1)

# Example: Click at current position
pyautogui.click()

# Example: Type some text
pyautogui.typewrite(['h', 'e', 'l', 'l', 'o'], interval=0.1)

# Example: Take a screenshot
screenshot = pyautogui.screenshot()

print("PyAutoGUI example completed!")