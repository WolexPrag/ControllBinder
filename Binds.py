import pyautogui as gui
class BindsStorage:
    __storage: list

    def WriteBind(self, binds: list):
        storage = binds

    def Use(self):
        for bind in self.__storage:
            gui.sleep(0.1)
            bind.Use()

    pass


class Bind:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def Use(self):
        gui.leftClick(self.x, self.y)

    pass
