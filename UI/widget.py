#pylint: disable=C0103, C0301, R0902
"""
Sets up and maintains the Widget part of the UI for QTPie
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui


class QTPieWidget(QtWidgets.QWidget):
    """
    A super function extending the QWidget class from PyQt5. This adds extra functionality to the widget to be used in QTPie

    Args:\n
        QtWidgets (PyQt5.QtWidgets.QWidget): Inherits from QWidget
    """

    resized = QtCore.pyqtSignal()
    clicked = QtCore.pyqtSignal()
    mouseEnter = QtCore.pyqtSignal()
    mouseLeave = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        """
        Initializes the super class

        Args:\n
            parent (PyQt5.QtWidgets.*): The object to put the widget on. Defaults to None.
        """

        super().__init__(parent)
    
    def resizeEvent(self, event):
        """
        Triggers when the window is resized

        Args:\n
            event (PyQt5.QtGui.QResizeEvent): The PyQt5 resize event
        """

        self.resized.emit()
        return super(QTPieWidget, self).resizeEvent(event)
    
    def mousePressEvent(self, event):
        """
        Triggers when the window is resized

        Args:\n
            event (PyQt5.QtGui.QMousePressEvent): The PyQt5 mouse press event
        """

        self.clicked.emit()
        return super(QTPieWidget, self).mousePressEvent(event)

    def enterEvent(self, event):
        """
        Triggers when the mouse enters the QTPieWidget

        Args:\n
            event (PyQt5.QtGui.QEnterEvent): The PyQt5 mouse enter event
        """

        self.mouseEnter.emit()
        return super(QTPieWidget, self).enterEvent(event)
    
    def leaveEvent(self, event):
        """
        Triggers when the mouse leaves the QTPieWidget

        Args:\n
            event (PyQt5.QtGui.QEnterEvent): The PyQt5 mouse leave event
        """

        self.mouseLeave.emit()
        return super().leaveEvent(event)
