from typing import List

import keyboard
import pyautogui as gui

from Binds import *


class Gui:
    Binds: List[BindsStorage]
    def WriteBind(self):
        binds: list
        while (True):
            if (self.CheckInput('/') == True):
                break
            if (self.CheckInput('left')):
                binds += Bind(gui.position().x,gui.position().y)
            pass
        self.Binds.append(BindsStorage(binds))
        pass
    def CheckInput(self,button:str):
        return keyboard.is_pressed(button)
    def UseBind(self, index: int):
        if (index >= len(self.Binds)):
            return Exception
        self.Binds[index].Use()
        pass
