import pyautogui

# To take screenshots and save it to desktop.
# pyautogui.screenshot('/Users/dmanral/Desktop/screenshot_example.png')

# Has to be pixel perfect and is slow.
# Image recognition (gives you location of whats in the image).
print(pyautogui.locateOnScreen('/where/your/file_Is/calc7key.png'))

# Center of the cropped out part of the bigger image.
width, hegiht = pyautogui.locateCenterOnScreen('/where/your/file_Is/calc7key.png')

# Moves to the coordinates.
pyautogui.moveTo((width, height) duration=1)

# Click the center.
pyautogui.click(width, height)
