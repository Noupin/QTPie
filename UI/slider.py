#pylint: disable=C0103, C0301, R0902
"""
Sets up and maintains the Slider part of the UI for QTPie.
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import PyQt5


class QTPieSlider(PyQt5.QtWidgets.QSlider):
    """
    A super function extending the QSlider class from PyQt5. This adds extra functionality to the slider to be used in QTPie.

    Args:\n
        QtWidgets (PyQt5.QtWidgets.QSlider): Inherits from QSlider.
    """

    def __init__(self, parent=None):
        """
        Initializes the super class.

        Args:\n
            parent (PyQt5.QtWidgets.*): The object to put the widget on. Defaults to None.
        """

        super().__init__(parent)

        self.mouseOn = False
    
    def enterEvent(self, event):
        """
        Triggers when the mouse enters the QTPieSlider.

        Args:\n
            event (PyQt5.QtGui.QEnterEvent): The PyQt5 mouse enter event.
        
        Returns:\n
            PyQt5.QtWidgets.QSlider.enterEvent: Runs the parents enterEvent.
        """

        self.mouseOn = True

        return super(QTPieSlider, self).enterEvent(event)
    
    def leaveEvent(self, event):
        """
        Triggers when the mouse leaves the QTPieSlider.

        Args:\n
            event (PyQt5.QtGui.QLeaveEvent): The PyQt5 mouse leave event.
        
        Returns:\n
            PyQt5.QtWidgets.QSlider.leaveEvent: Runs the parents leaveEvent.
        """

        self.mouseOn = False

        return super(QTPieSlider, self).leaveEvent(event)
