#pylint: disable=C0103, C0301, R0902
"""
Sets up and maintains the Label part of the UI for QTPie
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import PyQt5
from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui

#First Party Imports
from UI.label import QTPieLabel


class QTPieImage(QTPieLabel):
    """
    A super function extending the QLabel class from PyQt5. This adds extra functionality to the label to be used in QTPie

    Args:\n
        QtWidgets (PyQt5.QtWidgets.QLabel): Inherits from QLabel
    """

    def __init__(self, parent=None, dropArea=False, filename=""):
        """
        Initializes the super class

        Args:\n
            parent (PyQt5.QtWidgets.*): The object to put the widget on. Defaults to None.
            dropArea (bool, optional): Enables or disables drag and drop. Defaults to False.
            filename (str, optional): The given path for the image to be displayed. Defaults to "".
        """

        super().__init__(parent)

        self.filename = filename
        self.pixelMap = None

        self.setAcceptDrops(dropArea)

    def dropEvent(self, event):
        """
        Triggers when dropped on

        Args:\n
            event (PyQt5.QtGui.QDragDropEvent): Data held with the object being dropped
        
        Returns:\n
            PyQt5.QtGui.QDragDropEvent: Continues the original PyQt5 dropEvent code.
        """

        if event.mimeData().text()[8:].lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
            self.filename = event.mimeData().text()[8:]
            self.pixelMap = self.pixelMap.fromImage(PyQt5.QtGui.QImage(self.filename))
            self.pixelMap = self.pixelMap.scaled(self.size(), PyQt5.QtCore.Qt.KeepAspectRatio)
            self.setPixmap(self.pixelMap)
        
        return super(QTPieLabel, self).dropEvent(event)
    
    def resizeEvent(self, event):
        """
        Resizes the image inside the label to ensure the aspect ratio is kept and the image looks nice

        Args:
            event (PyQt5.QtGui.QResizeEvent): Data held with the label being resized

        Returns:
            PyQt5.QtGui.QResizeEvent: Continues the original PyQt5 resizeEvent code.
        """

        self.pixelMap = self.pixelMap.fromImage(PyQt5.QtGui.QImage(self.filename))
        self.pixelMap = self.pixelMap.scaled(self.size(), PyQt5.QtCore.Qt.KeepAspectRatio)
        self.setPixmap(self.pixelMap)

        return super().resizeEvent(event)
