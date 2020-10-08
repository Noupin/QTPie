#pylint: disable=C0103, C0301, R0902
"""
Holds all the actions to be used on UI element interaction
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui

#Allow for Python. relative imports
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

#First Party Imports
import utilities
from tunable import Tunable


class Actions:
    """
    Holds the actions functions for the QTPie GUI
    """

    def fileDialog(self):
        """
        Opens file dialog window
        """

        filename, _ = QtWidgets.QFileDialog.getOpenFileName()
    
    def load(self):
        """
        Action once the load button is clicked
        """

        print("Clicked!")
    
    def slideAndProgress(self, slider, progress):
        """
        Action when the slide is moved

        Args:\n
            slider (QTPieSlider): The initialized QTPie slider widget
            progress (QTPieProgressBar): The progress bar to be changed
        """

        progress.setValue(slider.value())

    def dialAndProgress(self, dial, progress):
        """
        Action when the slide is moved

        Args:\n
            slider (QTPieSlider): The initialized QTPie slider widget
            progress (QTPieProgressBar): The progress bar to be changed
        """

        progress.setValue(dial.value())
    
    def onWindowClose(self, window):
        """
        Actions to happen before the application window closes and the program finishes executing

        Args:\n
            window (QTPieWidget, QTPieWindow): The object waiting for a close signal
        """

        x, y = window.pos().x(), window.pos().y()
        width, height = window.size().width(), window.size().height()
        utilities.changeJSON("windowX", x)
        utilities.changeJSON("windowY", y)
        utilities.changeJSON("windowWidth", width)
        utilities.changeJSON("windowHeight", height)
    
    def playPause(self, mediaWidget, controlWidget, app):
        """
        Swaps the play pause state of the media

        Args:\n
            mediaWidget (QTPieWidget): The widget that holds all media player widgets.
            controlWidget (QTPieWidget): The widget that holds all media player control widgets.
            app (PyQt5.QtWidgets.QApplication): The application to change icons
        """

        if mediaWidget.media.playing:
            mediaWidget.media.pause()
            controlWidget.playPause.setIcon(app.style().standardIcon(PyQt5.QtWidgets.QStyle.SP_MediaPlay))
        else:
            mediaWidget.media.play()
            controlWidget.playPause.setIcon(app.style().standardIcon(PyQt5.QtWidgets.QStyle.SP_MediaPause))
    
    def changeVolume(self, mediaWidget, volumeWidget, app, tunableDict):
        """
        Changes the volume given a 1-100 value from the controller

        Args:\n
            mediaWidget (QTPieWidget): The widget that holds all media player widgets.
            volumeWidget (QTPieWidget): The widget that holds all media player volume widgets.
            app (PyQt5.QtWidgets.QApplication): The application to change icons
            tunableDict (JSON): The tunable variables for the application
        """

        mediaWidget.media.setVolume(volumeWidget.volumeBar.value())
        utilities.changeJSON("volume", volumeWidget.volumeBar.value())

        if mediaWidget.media.volume() == 0:
            mediaWidget.media.setMuted(True)
            volumeWidget.volumeBtn.setIcon(app.style().standardIcon(PyQt5.QtWidgets.QStyle.SP_MediaVolumeMuted))
        else:
            mediaWidget.media.setMuted(False)
            tunableDict["volume"] = volumeWidget.volumeBar.value()
            volumeWidget.volumeBtn.setIcon(app.style().standardIcon(PyQt5.QtWidgets.QStyle.SP_MediaVolume))
    
    def changeTimestamp(self, mediaWidget, controller):
        """
        Changes the timestamp given a 1-100 value from the controller

        Args:\n
            mediaWidget (QTPieWidget): The widget that holds all media player widgets.
            controller (QTPieSlider or QTPieDial): Controls the videos position from 0-duration values
        """

        mediaWidget.media.setPosition(controller.value())
    
    def timestampChanged(self, mediaWidget, controller):
        """
        Changes the controller when the timestamp changes

        Args:\n
            mediaWidget (QTPieWidget): The widget that holds all media player widgets.
            controller (QTPieSlider or QTPieDial): Controls the videos position from 0-duration values
        """

        controller.setValue(mediaWidget.media.position())

        #Enables autoplay of video
        if (mediaWidget.media.position() >= controller.maximum()) and not mediaWidget.media.paused:
            mediaWidget.media.play()
    
    def durationChanged(self, mediaWidget, controller):
        """
        Changes the controller when the timestamp changes

        Args:\n
            mediaWidget (QTPieWidget): The widget that holds all media player widgets.
            controller (QTPieSlider or QTPieDial): Controls the videos position from 0-duration values
        """

        controller.setRange(0, mediaWidget.media.duration())
    
    def showControls(self, controlWidget):
        """
        Enables the playPause, volume, and progress widgets passed

        Args:\n
            controlWidget (QTPieWidget): The widget that holds all media player control widgets.
        """

        controlWidget.setHidden(False)
    
    def hideControls(self, mediaWidget, controlWidget):
        """
        Enables the playPause, volume, and progress widgets passed

        Args:\n
            mediaWidget (QTPieWidget): The widget that holds all media player widgets.
            controlWidget (QTPieWidget): The widget that holds all media player control widgets.
        """

        if mediaWidget.media.paused:
            return

        controlWidget.setHidden(True)
    
    def openFile(self, mediaWidget):
        """
        Opens a new file and plays the media

        Args:\n
            mediaWidget (QTPieWidget): The widget that holds all media player widgets.
        """

        filename, _ = QtWidgets.QFileDialog.getOpenFileName()

        if filename.lower().endswith(('.mp4', '.avi', '.m4v')):
            mediaWidget.media.setMedia(PyQt5.QtMultimedia.QMediaContent(PyQt5.QtCore.QUrl.fromLocalFile(filename)))
            mediaWidget.media.play()

    def muteUnmute(self, mediaWidget, volumeWidget, app, tunableDict):
        """
        Swaps the mute state of the media

        Args:\n
            mediaWidget (QTPieWidget): The widget that holds all media player widgets.
            volumeWidget (QTPieWidget): The widget that holds all media player volume widgets.
            app (PyQt5.QtWidgets.QApplication): The application to change icons
            tunableDict (JSON): The tunable variables for the application
        """

        if not mediaWidget.media.isMuted():
            mediaWidget.media.setMuted(True)
            volumeWidget.volumeBar.setValue(0)
            volumeWidget.volumeBtn.setIcon(app.style().standardIcon(PyQt5.QtWidgets.QStyle.SP_MediaVolumeMuted))
        else:
            mediaWidget.media.setMuted(False)
            volumeWidget.volumeBar.setValue(tunableDict["volume"])
            volumeWidget.volumeBtn.setIcon(app.style().standardIcon(PyQt5.QtWidgets.QStyle.SP_MediaVolume))

    def volumeHover(self, volumeWidget):
        """
        shows the volume slider bar when hovering over the volume button

        Args:\n
            volumeWidget (QTPieWidget): The widget that holds all media player volume widgets.
        """

        volumeWidget.volumeBar.show()
    
    def volumeUnhover(self, volumeWidget):
        """
        shows the volume slider bar when hovering over the volume button

        Args:\n
            volumeWidget (QTPieWidget): The widget that holds all media player volume widgets.
        """

        if not volumeWidget.volumeBar.mouseOn:
            volumeWidget.volumeBar.hide()
