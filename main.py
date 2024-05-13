import pyautogui
from pyautogui import *

Paths = {

    'Box': r'Image\Box.png',
    '2Box': r'Image\2Box.png',
    'Cell': r'Image\Cell.png',
    'Field': r'Image\Field.png',
    'Confirm': r'Image\Confirm.png',

}
def InputInField(pos: int):
    click(pos)
    pyautogui.press('0')
    pass

if(confirm(text="Start?",buttons = ["Yes","No"])=="No"):
    quit()
PosBox = locateCenterOnScreen(Paths['Box'])
PosBox2 = locateCenterOnScreen(Paths['2Box'])
DifferentCells = (PosBox2.x - PosBox.x, PosBox.y)
click(PosBox)
FieldPos: (int, int)
Confirm: (int, int)
DifferentCells: (int, int)

print(DifferentCells)