#pylint: disable=C0103, C0301, R0902
"""
Sets up and maintains the Window part of the UI for QTPie.
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import PyQt5


class QTPieWindow(PyQt5.QtWidgets.QMainWindow):
    """
    A super function extending the QMainWindow class from PyQt5. This adds extra functionality to the window to be used in QTPie.

    Args:\n
        QtWidgets (PyQt5.QtWidgets.QMainWindow): Inherits from QMainWindow.
    """

    resized = PyQt5.QtCore.pyqtSignal()

    def __init__(self, parent=None):
        """
        Initializes the super class.

        Args:\n
            parent (PyQt5.QtWidgets.*): The app to put the window on. Defaults to None.
        """

        super().__init__(parent)
    
    def resizeEvent(self, event):
        """
        Triggers when the window is resized.

        Args:\n
            event (PyQt5.QtGui.QResizeEvent): The PyQt5 resize event.
        
        Returns:\n
            PyQt5.QtWidgets.QWidget.resizeEvent: Runs the parents resizeEvent.
        """

        self.resized.emit()

        return super(QTPieWindow, self).resizeEvent(event)

