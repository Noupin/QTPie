#pylint: disable=C0103, C0301, R0902
"""
Sets up and maintains the Image part of the UI for QTPie.
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui

#First Party Imports
from UI.label import QTPieLabel


class QTPieImage(QTPieLabel):
    """
    A super function extending the QTPieLabel class from QTPie. This adds extra
    functionality to the QTPieLabel to be used as an image holder in QTPie.

    Args:\n
        QTPieLabel (UI.label.QTPieLabel): Inherits from QTPieLabel.
    """

    def __init__(self, parent=None, dropArea=False, filename=""):
        """
        Initializes the super class

        Args:\n
            parent (PyQt5.QtWidgets.*): The object to put the widget on. Defaults to None.
            dropArea (bool, optional): Enables or disables drag and drop. Defaults to False.
            filename (str, optional): The given path for the image to be displayed. Defaults to "".
        """

        super().__init__(parent, dropArea)

        self.filename = filename
        self.pixelMap = None

    def dropEvent(self, event):
        """
        Triggers when dropped on.

        Args:\n
            event (PyQt5.QtGui.QDragDropEvent): Data held with the object being dropped.
        
        Returns:\n
            PyQt5.QtWidgets.QLabel.dropEvent: Runs the parents dropEvent.
        """

        if event.mimeData().text()[8:].lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
            self.filename = event.mimeData().text()[8:]
            self.pixelMap = self.pixelMap.fromImage(PyQt5.QtGui.QImage(self.filename))
            self.pixelMap = self.pixelMap.scaled(self.size(), PyQt5.QtCore.Qt.KeepAspectRatio)
            self.setPixmap(self.pixelMap)
        
        return super(QTPieLabel, self).dropEvent(event)
    
    def resizeEvent(self, event):
        """
        Resizes the image inside the label to ensure the aspect ratio is kept and the image looks original.

        Args:\n
            event (PyQt5.QtGui.QResizeEvent): Data held with the label being resized.

        Returns:\n
            PyQt5.QtWidgets.QLabel.resizeEvent: Runs the parents resizeEvent.
        """

        self.pixelMap = self.pixelMap.fromImage(PyQt5.QtGui.QImage(self.filename))
        self.pixelMap = self.pixelMap.scaled(self.size(), PyQt5.QtCore.Qt.KeepAspectRatio)
        self.setPixmap(self.pixelMap)

        return super(QTPieLabel, self).resizeEvent(event)
