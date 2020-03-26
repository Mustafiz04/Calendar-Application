import calendar
import keyboard
from datetime import datetime

year = datetime.now().year
month = datetime.now().month
was_click = False
while True:
    if(keyboard.is_pressed('a' or 'A')):
        if not was_click:
            print(calendar.calendar(year,2,1,6))
            was_click = True
    elif keyboard.is_pressed('F1') :
        if not was_click:
            print(calendar.month(year,1))
            was_click = True
    elif keyboard.is_pressed('F2') :
        if not was_click:
            print(calendar.month(year,2))
            was_click = True
    elif keyboard.is_pressed('F3') :
        if not was_click:
            print(calendar.month(year,3))
            was_click = True
    elif keyboard.is_pressed('F4') :
        if not was_click:
            print(calendar.month(year,4))
            was_click = True
    elif keyboard.is_pressed('F5') :
        if not was_click:
            print(calendar.month(year,5))
            was_click = True
    elif keyboard.is_pressed('F6') :
        if not was_click:
            print(calendar.month(year,6))
            was_click = True
    elif keyboard.is_pressed('F7') :
        if not was_click:
            print(calendar.month(year,7))
            was_click = True
    elif keyboard.is_pressed('F8') :
        if not was_click:
            print(calendar.month(year,8))
            was_click = True
    elif keyboard.is_pressed('F9') :
        if not was_click:
            print(calendar.month(year,9))
            was_click = True
    elif keyboard.is_pressed('F10') :
        if not was_click:
            print(calendar.month(year,10))
            was_click = True
    elif keyboard.is_pressed('F11') :
        if not was_click:
            print(calendar.month(year,11))
            was_click = True
    elif keyboard.is_pressed('F12') :
        if not was_click:
            print(calendar.month(year,12))
            was_click = True
    elif keyboard.is_pressed("up arrow") :
        if not was_click:
            print(calendar.month(year-1,month))
            was_click = True
    elif keyboard.is_pressed("down arrow") :
        if not was_click:
            print(calendar.month(year+1,month))
            was_click = True
    elif keyboard.is_pressed("left arrow") :
        if not was_click:
            print(calendar.month(year,month-1))
            was_click = True
    elif keyboard.is_pressed("right arrow") :
        if not was_click:
            print(calendar.month(year,month+1))
            was_click = True
    elif keyboard.is_pressed('esc') :
        break
    else:
        was_click = False
    

