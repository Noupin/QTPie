#pylint: disable=C0103, C0301, R0902
"""
Sets up and maintains the Pixmap part of the UI for QTPie
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui


class QTPiePixmap(QtGui.QPixmap):
    """
    A super function extending the QLabel class from PyQt5. This adds extra functionality to the pixmap to be used in QTPie

    Args:\n
        QtGui (PyQt5.QtGui.QPixmap): Inherits from QPixmap
    """

    def __init__(self, parent=None):
        """
        Initializes the super class

        Args:\n
            parent (PyQt5.QtWidgets.*): The object to put the widget on. Defaults to None.
        """

        super().__init__(parent)
