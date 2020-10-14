#pylint: disable=C0103, C0301, R0902
"""
Sets up and maintains the Label part of the UI for QTPie.
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import PyQt5
from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui


class QTPieLabel(QtWidgets.QLabel):
    """
    A super function extending the QLabel class from PyQt5. This adds extra functionality to the label to be used in QTPie.

    Args:\n
        QtWidgets (PyQt5.QtWidgets.QLabel): Inherits from QLabel.
    """

    def __init__(self, parent=None, dropArea=False):
        """
        Initializes the super class.

        Args:\n
            parent (PyQt5.QtWidgets.*): The object to put the widget on. Defaults to None.
            dropArea (bool, optional): Enables or disables drag and drop. Defaults to False.
        """

        super().__init__(parent)

        self.setAcceptDrops(dropArea)
    
    def dragEnterEvent(self, event):
        """
        Triggers when dragged over.

        Args:\n
            event (PyQt5.QtGui.QDragEnterEvent): Data held with the object being dragged.
        
        Returns:\n
            PyQt5.QtWidgets.QLabel.leaveEvent: Runs the parents dragEnterEvent.
        """

        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()
        
        return super(QTPieLabel, self).dragEnterEvent(event)

    def dropEvent(self, event):
        """
        Triggers when dropped on.

        Args:\n
            event (PyQt5.QtGui.QDragDropEvent): Data held with the object being dropped.
        
        Returns:\n
            PyQt5.QtWidgets.QLabel.leaveEvent: Runs the parents dropEvent.
        """

        self.setText(event.mimeData().text())
        
        return super(QTPieLabel, self).dropEvent(event)

