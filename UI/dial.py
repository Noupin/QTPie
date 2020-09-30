#pylint: disable=C0103, C0301, R0902
"""
Sets up and maintains the Dial part of the UI for QTPie
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui


class QTPieDial(QtWidgets.QDial):
    """
    A super function extending the QDial class from PyQt5. This adds extra functionality to the dial to be used in QTPie

    Args:\n
        QtWidgets (PyQt5.QtWidgets.QDial): Inherits from QDial
    """

    def __init__(self, parent=None, wrapping=True):
        """
        Initializes the super class

        Args:\n
            parent (PyQt5.QtWidgets.*): The object to put the widget on. Defaults to None.
        """

        super().__init__(parent)
        self.setWrapping(wrapping)
