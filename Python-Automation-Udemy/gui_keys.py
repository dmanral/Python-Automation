import pyautogui

# Find a place to write.    Then write instantly.
# pyautogui.click(100,100); pyautogui.typewrite('Hello, world!')

# Find a place to write.    Then write slowly.
# pyautogui.click(100,100); pyautogui.typewrite('Hello, world!', interval=0.2)

# Typing, moving, then typing again.
# Find a place to write.    Then write a,b, then move to the left twice and type X,Y.
# pyautogui.click(100,100); pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval=1)

# List of keyboard keys.
# print(pyautogui.KEYBOARD_KEYS)

# Pressing F1
# pyautogui.press('f1')

# Pressing keys in combination.
pyautogui.hotkey('command', 'm')  # This will minimize terminal window in MAC.
