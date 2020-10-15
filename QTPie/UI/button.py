#pylint: disable=C0103, C0301, R0902
"""
Sets up and maintains the Button part of the UI for QTPie.
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import PyQt5


class QTPieButton(PyQt5.QtWidgets.QPushButton):
    """
    A super function extending the QPushButton class from PyQt5. This adds extra functionality to the button to be used in QTPie.

    Args:\n
        QtWidgets (PyQt5.QtWidgets.QPushButton): Inherits from QPushButton.
    """

    mouseEnter = PyQt5.QtCore.pyqtSignal()
    mouseLeave = PyQt5.QtCore.pyqtSignal()

    def __init__(self, parent=None, dropArea=False, hover=False):
        """
        Initializes the super class.

        Args:\n
            parent (PyQt5.QtWidgets.*): The object to put the widget on. Defaults to None.
            dropArea (bool, optional): Enables or disables drag and drop. Defaults to False.
            hover (bool, optional): Enables or disables hovering signals. Defaults to False.
        """

        super().__init__(parent)

        self.hover = hover
        self.dropArea = dropArea
        self.mouseOn = False

        if self.dropArea:
            self.setAcceptDrops(True)
    
    def dragEnterEvent(self, event):
        """
        Triggers when dragged over.

        Args:\n
            event (PyQt5.QtGui.QDragEnterEvent): Data held with the object being dragged.
        
        Returns:\n
            PyQt5.QtWidgets.QPushButton.dragEnterEvent: Runs the parents dragEnterEvent.
        """

        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()

        return super(QTPieButton, self).dragEnterEvent(event)

    def dropEvent(self, event):
        """
        Triggers when dropped on.

        Args:\n
            event (PyQt5.QtGui.QDragDropEvent): Data held with the object being dropped.
        
        Returns:\n
            PyQt5.QtWidgets.QPushButton.dropEvent: Runs the parents dropEvent.
        """

        self.setText(event.mimeData().text())

        return super(QTPieButton, self).dropEvent(event)
    
    def enterEvent(self, event):
        """
        Triggers when the mouse enters the QTPieWidget.

        Args:\n
            event (PyQt5.QtGui.QEnterEvent): The PyQt5 mouse enter event.
        
        Returns:\n
            PyQt5.QtWidgets.QPushButton.enterEvent: Runs the parents enterEvent.
        """

        if self.hover:
            self.mouseEnter.emit()

        return super(QTPieButton, self).enterEvent(event)
    
    def leaveEvent(self, event):
        """
        Triggers when the mouse leaves the QTPieWidget.

        Args:\n
            event (PyQt5.QtGui.QLeaveEvent): The PyQt5 mouse leave event.
        
        Returns:\n
            PyQt5.QtWidgets.QPushButton.leaveEvent: Runs the parents leaveEvent.
        """

        if self.hover:
            self.mouseLeave.emit()

        return super(QTPieButton, self).leaveEvent(event)
