#pylint: disable=C0103, C0301, R0902
"""
Sets up and maintains the Widget part of the UI for QTPie.
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import PyQt5


class QTPieWidget(PyQt5.QtWidgets.QWidget):
    """
    A super function extending the QWidget class from PyQt5. This adds extra functionality to the widget to be used in QTPie.

    Args:\n
        QtWidgets (PyQt5.QtWidgets.QWidget): Inherits from QWidget.
    """

    resized = PyQt5.QtCore.pyqtSignal()
    clicked = PyQt5.QtCore.pyqtSignal()
    mouseEnter = PyQt5.QtCore.pyqtSignal()
    mouseLeave = PyQt5.QtCore.pyqtSignal()

    def __init__(self, parent=None, doesSignal=False):
        """
        Initializes the super class.

        Args:\n
            parent (PyQt5.QtWidgets.*): The object to put the widget on. Defaults to None.
            doesSignal (bool, optional): Whether or not signals for leaving and entering are emitted. Defaults to False.
        """

        super().__init__(parent)

        self.doesSignal = doesSignal

        #Grid varibles for the widget
        self.grid = None
        self.gridCount = 0

        self.setAcceptDrops(self.doesSignal)
    
    def resizeEvent(self, event):
        """
        Triggers when the window is resized.

        Args:\n
            event (PyQt5.QtGui.QResizeEvent): The PyQt5 resize event.
        
        Returns:\n
            PyQt5.QtWidgets.QWidget.resizeEvent: Runs the parents resizeEvent.
        """

        self.resized.emit()

        return super(QTPieWidget, self).resizeEvent(event)
    
    def mousePressEvent(self, event):
        """
        Triggers when the window is resized.

        Args:\n
            event (PyQt5.QtGui.QMousePressEvent): The PyQt5 mouse press event.
        
        Returns:\n
            PyQt5.QtWidgets.QWidget.mousePressEvent: Runs the parents mousePressEvent.
        """

        if self.doesSignal:
            self.clicked.emit()

        return super(QTPieWidget, self).mousePressEvent(event)

    def enterEvent(self, event):
        """
        Triggers when the mouse enters the QTPieWidget.

        Args:\n
            event (PyQt5.QtGui.QEnterEvent): The PyQt5 mouse enter event.
        
        Returns:\n
            PyQt5.QtWidgets.QWidget.enterEvent: Runs the parents enterEvent.
        """

        if self.doesSignal:
            self.mouseEnter.emit()

        return super(QTPieWidget, self).enterEvent(event)
    
    def leaveEvent(self, event):
        """
        Triggers when the mouse leaves the QTPieWidget.

        Args:\n
            event (PyQt5.QtGui.QLeaveEvent): The PyQt5 mouse leave event.
        
        Returns:\n
            PyQt5.QtWidgets.QWidget.leaveEvent: Runs the parents leaveEvent.
        """

        if self.doesSignal:
            self.mouseLeave.emit()

        return super(QTPieWidget, self).leaveEvent(event)
