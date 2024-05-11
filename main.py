import Gui

gui1 = Gui.Gui()

while (True):

    if (gui1.CheckInput('-')):
        print("Start Write Bind")
        gui1.WriteBind()
        print("End Write Bind")
    if (gui1.CheckInput(1)):
        print("Start Use Bind")
        gui1.UseBind(1)
        print("End- Use Bind")
    pass
