from pycaw.pycaw import AudioUtilities as AU, IAudioMeterInformation
from time import sleep
import keyboard
import pyautogui
aplikacje = AU.GetAllSessions()
def zarzut():
    sleep(0.1)
    pyautogui.mouseDown()
    sleep(0.4)
    pyautogui.mouseUp()
    print("Zarzut")
    sleep(0.5)
def zlow():
    pyautogui.mouseDown()
    sleep(0.05)
    pyautogui.mouseUp()
    print("Złowiona")

for apl in aplikacje:
    print(apl)
    if apl.Process!=None:
        if apl.Process.name()=="crueltysquad.exe": #Tutaj jaka aplikacja jest monitorowana
            szuk=apl
            break
else:
    print("Nie znaleziono procesu L")
    exit(0)

miernik = szuk._ctl.QueryInterface(IAudioMeterInformation)
print("Aby zaczac wcisnij q (by skonczyc tez btw)")
while True:          
    sleep(0.1)
    if keyboard.is_pressed('q'):
        print("Start Rybienia za 2 sekundy (puść guzik)")
        sleep(2)
        break
zarzut()
while True:
    glos = miernik.GetPeakValue()
    print(f"Poziom glosnosci: {glos}")
    sleep(0.03)
    if keyboard.is_pressed('q'):
        print("Koniec Rybienia")
        break
    if glos>0.007 and glos<0.009:
        print("Branie...")
        zlow()
        sleep(1)
        zarzut()
