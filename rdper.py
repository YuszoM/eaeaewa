import os
from time import sleep
import pyautogui
pyautogui.FAILSAFE = False

def connect_to_remote_computer():
    with open('pass.txt',encoding='utf8') as f:
        lines = f.readlines()
        number_of_lines = len(lines)
        print(number_of_lines)

    for i in range(number_of_lines):
        host = lines[i].strip()
        os.system(f"cmdkey /generic:{host} /user:Administrator /pass:9fLdLy3rYM9LF5eNAa")
        os.system(f'start mstsc /v:{host} /w:1000 /h:800')
        sleep(5)
        print("[+] Connected to remote computer"
        )
        pyautogui.press('left')
        pyautogui.press('enter')
        sleep(30)
        
if __name__ == "__main__":
    connect_to_remote_computer()
