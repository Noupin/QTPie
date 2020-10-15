#pylint: disable=C0103, C0301, R0902
"""
Sets up and maintains the Media part of the UI for QTPie.
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import PyQt5
from PyQt5 import QtMultimedia


class QTPieMedia(PyQt5.QtMultimedia.QMediaPlayer):
    """
    A super function extending the QMediaPlayer class from PyQt5. This adds extra functionality to the media player to be used in QTPie.

    Args:\n
        QtWidgets (PyQt5.QtWidgets.QMediaPlayer): Inherits from QMediaPlayer.
    """

    def __init__(self, parent=None):
        """
        Initializes the super class.

        Args:\n
            parent (PyQt5.QtWidgets.*): The object to put the widget on. Defaults to None.
        """

        super().__init__(parent)
    
        self.playing = False
        self.paused = False
    
    def play(self):
        """
        Plays the media.

        Returns:\n
            PyQt5.QtMultimedia.QMediaPlayer.play: Runs the parents play.
        """
        
        self.playing = True
        self.paused = False

        return super(QTPieMedia, self).play()
    
    def pause(self):
        """
        Pauses the media.

        Returns:\n
            PyQt5.QtMultimedia.QMediaPlayer.pause: Runs the parents pause.
        """

        self.paused = True
        self.playing = False
        
        return super(QTPieMedia, self).pause()
