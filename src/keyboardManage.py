import keyboard
#print(keyboard.key_to_scan_codes("+"))

def hacerZoom(k):
    for i in range(k):
        keyboard.press("ctrl")  
        keyboard.press_and_release(78)
        keyboard.release("ctrl")
    return;

def hacerMim(k):
    for i in range(k):
        keyboard.press_and_release("ctrl+-")  
    return;

def bajarPagina(k):  
    for i in range(k):
        keyboard.press_and_release("down")
    return;


def subirPagina(k):  
    for i in range(k):
        keyboard.press_and_release("up")
    return;


def paginaSiguiente(k):  
    for i in range(k):
        keyboard.press_and_release("right")
    return;

def paginaAnterior(k):  
    for i in range(k):
        keyboard.press_and_release("left")
    return;
