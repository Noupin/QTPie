#pylint: disable=C0103, C0301, R0902
"""
Sets up and maintains the Widget part of the UI for QTPie
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui

#First Party Imports
from UI.widget import QTPieWidget


class QTPieMediaWidget(QTPieWidget):
    """
    A super function extending the QTPieWidget class from QTPie. Specialized for media attributes.

    Args:\n
        QtWidgets (PyQt5.QtWidgets.QWidget): Inherits from QWidget
    """

    def __init__(self, parent=None, doesSignal=False, dropArea=False):
        """
        Initializes the super class

        Args:\n
            parent (PyQt5.QtWidgets.*): The object to put the widget on. Defaults to None.
            isVideo (bool, optional): Determines whether the video attributes will be used. Defaults to False.
        """

        super().__init__(parent, doesSignal)

        self.doesSignal = doesSignal

        #Grid varibles for the widget
        self.grid = None
        self.gridCount = 0

        #Media variables for the widget
        self.media = None
        self.video = None
        self.filename = ""

        self.setAcceptDrops(self.doesSignal)
    
    def dragEnterEvent(self, event):
        """
        Triggers when dragged over

        Args:\n
            event (PyQt5.QtGui.QDragEnterEvent): Data held with the object being dragged
        
        Returns:\n
            PyQt5.QtGui.QDragEnterEvent: Continues the original PyQt5 dragEnterEvent code.
        """

        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()
        
        return super(QTPieMediaWidget, self).dragEnterEvent(event)

    def dropEvent(self, event):
        """
        Triggers when dropped on

        Args:\n
            event (PyQt5.QtGui.QDragDropEvent): Data held with the object being dropped
        
        Returns:\n
            PyQt5.QtGui.QDragDropEvent: Continues the original PyQt5 dropEvent code.
        """

        if self.dropEvent and event.mimeData().text()[8:].lower().endswith(('.mp4', '.avi', '.m4v')):
            self.filename = event.mimeData().text()[8:]
            self.media.setMedia(PyQt5.QtMultimedia.QMediaContent(PyQt5.QtCore.QUrl.fromLocalFile(self.filename)))
            self.media.play()
        
        return super(QTPieMediaWidget, self).dropEvent(event)
    
    def updateControls(self):
        """
        Updates the items in the controls list
        """

        self.controls = [self.playPause, self.volumeWidget, self.openFile, self.vProgress]
