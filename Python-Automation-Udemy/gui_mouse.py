# pyautogui has a fail safe so you dont lose control of your computer when
# running a auto run program. If you slide your mouse to (0,0) or top left
# that will indicate pyautogui to stop the program.
import pyautogui

# Size of screen
# width, height = pyautogui.size()

# Position of the mouse
print(pyautogui.position())

# Controlling the mouse
# pyautogui.moveTo(1325,419)

# Controlling the mouse slowly (1.5 seconds)
# pyautogui.moveTo(1325,419, duration=1.5)

# Controlling/moving mouse to a relative position
# pyautogui.moveRel(200, 0)       # 200 pixels to the right.

# Controlling/moving mouse to a relative position with time
# pyautogui.moveRel(200, 0, 2)       # 200 pixels to the right in 2 seconds.
# pyautogui.moveRel(0, -100, 2)       # 100 pixels up in 2 seconds.

# Clicking the mouse
# width, height = pyautogui.position()    # Find position of where you want to click.
# pyautogui.click(width, height)
# pyautogui.doubleClick(width, height)    # Double click something. You can also rightClick and middleClick.

# deagTo() and dragRel() will click the mouse while moving it.

# Displays the mouse position.
pyautogui.displayMousePosition()        # Real time postion and rgb value of what the mouse is touching.
