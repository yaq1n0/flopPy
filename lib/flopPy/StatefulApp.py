

from tkinter import Tk
import logging
import types
from lib.pySSS import State


class StatefulApp:
    """ class wrapper for tkinter root """
    def __init__(self, title="title", width=1280, height=720, resizable=True, strict=True):
        # create Tk() root
        self.root = Tk()

        # save StatefulApp parameters as object fields
        self.rootTitle = title
        self.rootWidth = width
        self.rootHeight = height
        self.rootResizeable = resizable
        self.rootStrict = strict

        # create state
        self.appState = State()

        # call initialization subroutines
        self.setTitle()
        self.setGeometry()
        self.bindAll()

    def setTitle(self):
        self.root.title(self.rootTitle)
        return

    def setGeometry(self):
        # set geometry to center the Tk window
        offset_x = int(self.root.winfo_screenwidth() / 2 - self.rootWidth / 2)
        offset_y = int(self.root.winfo_screenheight() / 2 - self.rootHeight / 2)
        geometry = "{}x{}+{}+{}".format(self.rootWidth, self.rootHeight, offset_x, offset_y)
        logging.debug("[StatefulApp] setting root geometry {}".format(geometry))
        self.root.geometry(geometry)

        # handle resizable
        if self.rootResizeable:
            self.root.resizable(True, True)
        else:
            self.root.resizable(False, False)

        return

    def addBind(self, bind, event):
        return


    def bindAll(self):
        # bind keys to functions here
        self.root.bind('<Escape>')
        return

    def run(self):
        self.root.mainloop()




if __name__ == "__main__":
    app = StatefulApp()
    # app.addBind()

    app.run()

