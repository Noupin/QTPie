#pylint: disable=C0103, C0301, R0902
"""
Sets up and maintains the Video part of the UI for QTPie.
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import PyQt5
from PyQt5 import QtMultimediaWidgets


class QTPieVideo(PyQt5.QtMultimediaWidgets.QVideoWidget):
    """
    A super function extending the QVideoWidget class from PyQt5. This adds extra functionality to the video to be used in QTPie.

    Args:\n
        QtWidgets (PyQt5.QtMultimediaWidgets.QVideoWidget): Inherits from QVideoWidget.
    """

    def __init__(self, parent=None, dropArea=False):
        """
        Initializes the super class.

        Args:\n
            parent (PyQt5.QtWidgets.*): The object to put the widget on. Defaults to None.
            dropArea (bool, optional): Enables or disables drag and drop. Defaults to False.
        """

        super().__init__(parent)

        if dropArea:
            self.setAcceptDrops(True)
