import keyboard 
#print(keyboard.key_to_scan_codes("+"))

def hacerZoom():
    a = 0
    while a < 20:
        a = a+1
        print("a")
        keyboard.press("ctrl")  
        keyboard.press_and_release(78)
        keyboard.release("ctrl")
    


hacerZoom()
