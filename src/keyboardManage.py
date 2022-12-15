import keyboard
#print(keyboard.key_to_scan_codes("+"))

def hacerZoom():
    keyboard.press("ctrl")  
    keyboard.press_and_release(78)
    keyboard.release("ctrl")
    return;

def hacerMim():
    keyboard.press_and_release("ctrl+-")  
    return;


