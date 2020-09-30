#pylint: disable=C0103, C0301, R0902
"""
Sets up and maintains the Video part of the UI for QTPie
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import PyQt5
from PyQt5 import QtMultimedia


class QTPieMedia(QtMultimedia.QMediaPlayer):
    """
    A super function extending the QMediaPlayer class from PyQt5. This adds extra functionality to the media player to be used in QTPie

    Args:\n
        QtWidgets (PyQt5.QtWidgets.QMediaPlayer): Inherits from QMediaPlayer
    """

    def __init__(self, parent=None):
        """
        Initializes the super class

        Args:\n
            parent (PyQt5.QtWidgets.*): The object to put the widget on. Defaults to None.
        """

        super().__init__(parent)
        self.playing = False
        self.paused = False
    
    def play(self):
        """
        Plays the video

        Returns:
            NoneType: Continues the PyQt5 play function
        """
        
        self.playing = True
        self.paused = False

        return super().play()
    
    def pause(self):
        """
        Plays the pause

        Returns:
            NoneType: Continues the PyQt5 pause function
        """

        self.paused = True
        self.playing = False
        
        return super().pause()
