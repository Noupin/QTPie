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
    
    def makeLoadPage(self):
        """
        Lays out the UI for the Load screen.
        """

        for _ in range(12):
            self.ui.addGridRow(self.ui.grid, self.ui.gridCount, 12)
            self.ui.gridCount += 1
        
        self.ui.createMenu()

        self.maleBtn = self.ui.makeButton(self.ui.actions.load, name="maleBtn", txt="Male", gridData=[6, 11, 6, 1])
        self.femaleBtn = self.ui.makeButton(self.ui.actions.fileDialog, name="femaleBtn", txt="Female", gridData=[0, 11, 6, 1])
        self.label = self.ui.makeLabel(txt="QTPie", enableDrop=True, gridData=[5, 0, 2, 1])
        self.progressBar = self.ui.makeProgressBar(gridData=[0, 10, 12, 1])
        self.slider = self.ui.makeSlider(lambda: self.ui.actions.slideAndProgress(self.slider, self.progressBar), gridData=[0, 2, 12, 1])
        self.radio = self.ui.makeRadioButton(txt="r1", gridData=[0, 12, 3, 1])
        self.radio1 = self.ui.makeRadioButton(txt="r2", gridData=[3, 12, 3, 1])
        self.check = self.ui.makeCheckbox(txt="c1", gridData=[6, 12, 3, 1])
        self.dial = self.ui.makeDial(lambda: self.ui.actions.dialAndProgress(self.dial, self.progressBar), gridData=[9, 12, 3, 1])
        self.text = self.ui.makeTextbox(align="center", enableDrop=True, gridData=[0, 3, 6, 1])
        self.autoBox = self.ui.makeDropdown(align="center", values=["hi", "hello", "test"], textEdit=True, gridData=[6, 3, 6, 1])
        self.image = self.ui.makeImage(keepAR=True, enableDrop=True, gridData=[3, 4, 6, 3])
        self.video = self.ui.makeVideo(gridData=[3, 7, 6, 3])

        self.ui.mainWindow.show()
        sys.exit(self.ui.app.exec_())
