import pyautogui as pya


class Position:
    x: int
    y: int

    def __init__(self, x: int = None, y: int = None, pos=None):
        if (pos != None):
            self.x = pos.x
            self.y = pos.y
        else:
            self.x = x
            self.y = y


def MousePos():
    return pya.position()


def FindOnDisplay(path: str, region= None,confidence=0.95):
    try:
        if (region == None):
            return pya.locateCenterOnScreen(path,confidence=confidence)
        else:
            return pya.locateCenterOnScreen(path, region)
    except:
        print("Image not found")


def LocateOnDispalay(path: str,confidence=0.15):
    try:
        return pya.locateOnScreen(path,confidence=confidence)
    except:
        print("Image not found")




def Drag(to: Position, duration=0.5):
    pya.mouseDown(button="left")
    MoveMouse(to, duration=duration)
    pass


def MoveMouse(to: Position, duration=0.5):
    pya.moveTo(to.x, to.y, duration=duration)
    pass


def Click(to: Position, duration=0.5):
    pya.click(to.x, to.y, duration=duration)
    pass

def Aktivator():
    pya.password()