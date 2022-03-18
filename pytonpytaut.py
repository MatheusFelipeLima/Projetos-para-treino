import pyautogui as py
import pyperclip as pyperc
import time
py.PAUSE = 1
py.press('win')
time.sleep(2)
py.write('Microsoft Edge')
py.press('enter')
py.hotkey('ctrl','t')
pyperc.copy('https://www.youtube.com/watch?v=HHWQF50cIsw')
py.hotkey('ctrl','v')
py.press('enter')

