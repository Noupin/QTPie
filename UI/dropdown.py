#pylint: disable=C0103, C0301, R0902
"""
Sets up and maintains the Dropdown part of the UI for QTPie.
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import PyQt5


class QTPieDropdown(PyQt5.QtWidgets.QComboBox):
    """
    A super function extending the QComboBox class from PyQt5. This adds extra functionality to the combo box to be used in QTPie.

    Args:\n
        QtWidgets (PyQt5.QtWidgets.QComboBox): Inherits from QComboBox.
    """

    def __init__(self, parent=None, dropArea=False):
        """
        Initializes the super class.

        Args:
            parent (PyQt5.QtWidgets.*, optional): The object to put the widget on. Defaults to None.
            dropArea (bool, optional): Enables or disables dropping text. Defaults to False.
            dragArea (bool, optional): Enables or disables dragging text. Defaults to True.
        """

        super().__init__(parent)
        
        self.setAcceptDrops(dropArea)
    
    def dragEnterEvent(self, event):
        """
        Triggers when dragged over.

        Args:\n
            event (PyQt5.QtGui.QDragEnterEvent): Data held with the object being dragged.
        
        Returns:\n
            PyQt5.QtWidgets.QPushButton.dragEnterEvent: Runs the parents dragEnterEvent.
        """

        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()
        
        return super(QTPieDropdown, self).dragEnterEvent(event)

    def dropEvent(self, event):
        """
        Triggers when dropped on.

        Args:\n
            event (PyQt5.QtGui.QDragDropEvent): Data held with the object being dropped.
        
        Returns:\n
            PyQt5.QtWidgets.QPushButton.dropEvent: Runs the parents dropEvent.
        """

        self.setText(event.mimeData().text())

        return super(QTPieDropdown, self).dropEvent(event)
