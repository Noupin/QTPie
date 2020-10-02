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


class QTPieWidget(QtWidgets.QWidget):
    """
    A super function extending the QWidget class from PyQt5. This adds extra functionality to the widget to be used in QTPie

    Args:\n
        QtWidgets (PyQt5.QtWidgets.QWidget): Inherits from QWidget
    """

    resized = QtCore.pyqtSignal()
    clicked = QtCore.pyqtSignal()
    mouseEnter = QtCore.pyqtSignal()
    mouseLeave = QtCore.pyqtSignal()

    def __init__(self, parent=None, isVideo=False):
        """
        Initializes the super class

        Args:\n
            parent (PyQt5.QtWidgets.*): The object to put the widget on. Defaults to None.
        """

        super().__init__(parent)

        self.isVideo = isVideo
        self.grid = None
        self.gridCount = 0
        self.media = None
        self.video = None
        self.filename = ""
        self.controls = []

        self.setAcceptDrops(self.isVideo)
    
    def resizeEvent(self, event):
        """
        Triggers when the window is resized

        Args:\n
            event (PyQt5.QtGui.QResizeEvent): The PyQt5 resize event
        """

        self.resized.emit()

        return super(QTPieWidget, self).resizeEvent(event)
    
    def mousePressEvent(self, event):
        """
        Triggers when the window is resized

        Args:\n
            event (PyQt5.QtGui.QMousePressEvent): The PyQt5 mouse press event
        """

        if self.isVideo:
            self.clicked.emit()

        return super(QTPieWidget, self).mousePressEvent(event)

    def enterEvent(self, event):
        """
        Triggers when the mouse enters the QTPieWidget

        Args:\n
            event (PyQt5.QtGui.QEnterEvent): The PyQt5 mouse enter event
        """

        if self.isVideo:
            self.mouseEnter.emit()

        return super(QTPieWidget, self).enterEvent(event)
    
    def leaveEvent(self, event):
        """
        Triggers when the mouse leaves the QTPieWidget

        Args:\n
            event (PyQt5.QtGui.QEnterEvent): The PyQt5 mouse leave event
        """

        if self.isVideo:
            self.mouseLeave.emit()

        return super(QTPieWidget, self).leaveEvent(event)
    
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
        
        return super(QTPieWidget, self).dragEnterEvent(event)

    def dropEvent(self, event):
        """
        Triggers when dropped on

        Args:\n
            event (PyQt5.QtGui.QDragDropEvent): Data held with the object being dropped
        
        Returns:\n
            PyQt5.QtGui.QDragDropEvent: Continues the original PyQt5 dropEvent code.
        """

        if self.isVideo and event.mimeData().text()[8:].lower().endswith(('.mp4', '.avi')):
            self.filename = event.mimeData().text()[8:]
            self.media.setMedia(PyQt5.QtMultimedia.QMediaContent(PyQt5.QtCore.QUrl.fromLocalFile(self.filename)))
            self.media.play()
        
        return super(QTPieWidget, self).dropEvent(event)
