#pylint: disable=C0103, C0301, R0902
"""
Sets up and maintains the Dropdown part of the UI for QTPie
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui


class QTPieDropdown(QtWidgets.QComboBox):
    """
    A super function extending the QComboBox class from PyQt5. This adds extra functionality to the combo box to be used in QTPie

    Args:\n
        QtWidgets (PyQt5.QtWidgets.QComboBox): Inherits from QComboBox
    """

    def __init__(self, parent=None, dropArea=False):
        """
        Initializes the super class

        Args:
            parent (PyQt5.QtWidgets.*, optional): The object to put the widget on. Defaults to None.
            dropArea (bool, optional): Enables or disables dropping text. Defaults to False.
            dragArea (bool, optional): Enables or disables dragging text. Defaults to True.
        """

        super().__init__(parent)
        
        self.setAcceptDrops(dropArea)
    
    def dragEnterEvent(self, event):
        """
        Triggers when dragged over

        Args:\n
            event (PyQt5.QtGui.QDragEnterEvent): Data held with the object being dragged
        """

        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        """
        Triggers when dropped on

        Args:\n
            event (PyQt5.QtGui.QDragDropEvent): Data held with the object being dropped
        """

        self.setText(event.mimeData().text())
