#pylint: disable=C0103, C0301, R0902
"""
Sets up and maintains the Scroll Area part of the UI for QTPie
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui


class QTPieScroll(QtWidgets.QScrollArea):
    """
    A super function extending the QScrollArea class from PyQt5. This adds extra functionality to the scroll area to be used in QTPie

    Args:\n
        QtWidgets (PyQt5.QtWidgets.QScrollArea): Inherits from QScrollArea
    """

    clicked = QtCore.pyqtSignal()
    mouseEnter = QtCore.pyqtSignal()
    mouseLeave = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        """
        Initializes the super class

        Args:\n
            parent (PyQt5.QtWidgets.*): The app to put the window on. Defaults to None.
        """

        super().__init__(parent)
    
    def mousePressEvent(self, event):
        """
        Triggers when the window is resized

        Args:\n
            event (PyQt5.QtGui.QResizeEvent): The PyQt5 resize event
        """

        self.clicked.emit()
        return super(QTPieScroll, self).mousePressEvent(event)

    def enterEvent(self, event):
        """
        Triggers when the mouse enters the QTPieScroll

        Args:\n
            event (PyQt5.QtGui.QEnterEvent): The PyQt5 mouse enter event
        """

        self.mouseEnter.emit()
        return super(QTPieScroll, self).enterEvent(event)
    
    def leaveEvent(self, event):
        """
        Triggers when the mouse leaves the QTPieScroll

        Args:\n
            event (PyQt5.QtGui.QEnterEvent): The PyQt5 mouse leave event
        """

        self.mouseLeave.emit()
        return super(QTPieScroll, self).leaveEvent(event)
