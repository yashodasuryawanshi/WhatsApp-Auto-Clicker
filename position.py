# import pyautogui
# import time

# print("5 second hai.... whatsapp ke message par mouse le jao")
# time.sleep(5)
# x,y=pyautogui.position()
# print("coordinate:",x,y)



import pyautogui
import pyperclip
import time

pyautogui.FALSE

x = 1218  
y = 350   

print("3 second hai... WhatsApp open rakho")
time.sleep(3)

pyautogui.click(x, y, clicks=3, interval=0.1)
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

text = pyperclip.paste()
print("copied Text:", text)
