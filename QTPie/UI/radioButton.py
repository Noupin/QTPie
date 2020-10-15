#pylint: disable=C0103, C0301, R0902
"""
Sets up and maintains the Radio Button part of the UI for QTPie.
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import PyQt5


class QTPieRadioButton(PyQt5.QtWidgets.QRadioButton):
    """
    A super function extending the QRadioButton class from PyQt5. This adds extra functionality to the radio button to be used in QTPie.

    Args:\n
        QtWidgets (PyQt5.QtWidgets.QRadioButton): Inherits from QRadioButton.
    """

    def __init__(self, parent=None):
        """
        Initializes the super class.

        Args:\n
            parent (PyQt5.QtWidgets.*): The object to put the widget on. Defaults to None.
        """

        super().__init__(parent)
