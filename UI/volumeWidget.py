#pylint: disable=C0103, C0301, R0902
"""
Sets up and maintains the Widget part of the UI for QTPie.
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import PyQt5

#First Party Imports
from UI.widget import QTPieWidget


class QTPieVolumeWidget(QTPieWidget):
    """
    A super function extending the QTPieWidget class from QTPie. Specialized for volume control attributes.

    Args:\n
        QTPieWidget (UI.widget.QTPieWidget): Inherits from QTPieWidget.
    """

    def __init__(self, parent=None, doesSignal=False):
        """
        Initializes the super class.

        Args:\n
            parent (PyQt5.QtWidgets.*): The object to put the widget on. Defaults to None.
            doesSignal (bool, optional): Whether or not signals for leaving and entering are emitted. Defaults to False.
        """

        super().__init__(parent, doesSignal)

        #Grid varibles for the widget
        self.grid = None
        self.gridCount = 0

        #Volume widget variables
        self.volumeBtn = None
        self.volumeBar = None
