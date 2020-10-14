#pylint: disable=C0103, C0301, R0902
"""
The UI handling for the QTPie Example application.
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys

#Allow for Python. relative imports
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

#First Party Imports
from QTPie import QTPie
from tunable import Tunable as tunable


class UI:
    """
    Master class for the application.
    """

    def __init__(self, ui):
        """
        Manages the different pages for the UI.

        Args:
            ui (QTPie.QTPie): Extension of PyQt5.
        """

        self.ui = ui
    
    def makePage(self):
        """
        Lays out the UI for the Load screen.
        """

        for _ in range(12):
            self.ui.addGridRow(self.ui.grid, self.ui.gridCount, 12)
            self.ui.gridCount += 1
        
        self.ui.createMenu()

        self.maleBtn = self.ui.addButton([6, 11, 6, 1], self.ui.actions.load, name="maleBtn", txt="Male")
        self.femaleBtn = self.ui.addButton([0, 11, 6, 1], self.ui.actions.fileDialog, name="femaleBtn", txt="Female")
        self.label = self.ui.addLabel([5, 0, 2, 1], txt="QTPie\nExample", enableDrop=True)
        self.progressBar = self.ui.addProgressBar([0, 10, 12, 1])
        self.slider = self.ui.addSlider([0, 2, 12, 1], lambda: self.ui.actions.slideAndProgress(self.slider, self.progressBar))
        self.radio = self.ui.addRadioButton([0, 12, 3, 1], txt="r1")
        self.radio1 = self.ui.addRadioButton([3, 12, 3, 1], txt="r2")
        self.check = self.ui.addCheckbox([6, 12, 3, 1], txt="c1")
        self.dial = self.ui.addDial([9, 12, 3, 1], lambda: self.ui.actions.dialAndProgress(self.dial, self.progressBar))
        self.text = self.ui.addTextbox([0, 3, 6, 1], align="center", enableDrop=True)
        self.autoBox = self.ui.addDropdown([6, 3, 6, 1], align="center", values=["hi", "hello", "test"], textEdit=True)
        self.image = self.ui.addImage([3, 4, 6, 3], keepAR=True, enableDrop=True)
        self.video = self.ui.addVideo([3, 7, 6, 3])

        self.ui.mainWindow.show()
        sys.exit(self.ui.app.exec_())
