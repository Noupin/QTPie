#pylint: disable=C0103, C0301, R0902
"""
Sets up and maintains the Progress Bar part of the UI for QTPie.
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import PyQt5


class QTPieProgressBar(PyQt5.QtWidgets.QProgressBar):
    """
    A super function extending the QProgressBar class from PyQt5. This adds extra functionality to the progress bar to be used in QTPie.

    Args:\n
        QtWidgets (PyQt5.QtWidgets.QProgressBar): Inherits from QProgressBar.
    """

    def __init__(self, parent=None):
        """
        Initializes the super class.

        Args:\n
            parent (PyQt5.QtWidgets.*): The object to put the widget on. Defaults to None.
        """
        
        super().__init__(parent)
