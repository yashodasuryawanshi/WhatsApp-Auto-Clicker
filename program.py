
import pyautogui
import pyperclip
import random
import time

pyautogui.FAILSAFE = False

# 1. YE TUMHARA REPLY LIKHO
replies = [
    "I am also good mom ❤️"
        "did you eat mom:"
        "take care mom:"
        "i love you mom:"
        ]  

print("10 second hai... WhatsApp Web ke chat box me click kar do ")
time.sleep(10)

reply=random.choice(replies)

# 2. REPLY TYPE KARNA
pyautogui.write(reply)
random.sleep(0.5)

# 3. SEND KARNA
pyautogui.press('enter')

print("Reply bhej diya!:",reply)