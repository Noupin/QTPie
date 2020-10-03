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
    def __init__(self):
        pass

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
    
    def playPause(self, mediaWidget, app):
        """
        Swaps the play pause state of the media

        Args:\n
            mediaWidget (QTPieWidget): The widget that holds all media player widgets.
            app (PyQt5.QtWidgets.QApplication): The application to change icons
        """

        if mediaWidget.media.playing:
            mediaWidget.media.pause()
            mediaWidget.playPause.setIcon(app.style().standardIcon(PyQt5.QtWidgets.QStyle.SP_MediaPlay))
        else:
            mediaWidget.media.play()
            mediaWidget.playPause.setIcon(app.style().standardIcon(PyQt5.QtWidgets.QStyle.SP_MediaPause))
    
    def changeVolume(self, media, controller, button, app, tunableDict):
        """
        Changes the volume given a 1-100 value from the controller

        Args:\n
            media (QTPieMeida): The media player that holds media
            controller (QTPieSlider or QTPieDial): Controls the volume from 0-100 values
            button (QTPieButton): The volume button
            app (PyQt5.QtWidgets.QApplication): The application to change icons
            tunableDict (JSON): The tunable variables for the application
        """

        #media.setMuted(False)
        media.setVolume(controller.value())
        utilities.changeJSON("volume", controller.value())

        if media.volume() == 0:
            media.setMuted(True)
            button.setIcon(app.style().standardIcon(PyQt5.QtWidgets.QStyle.SP_MediaVolumeMuted))
        else:
            media.setMuted(False)
            tunableDict["volume"] = controller.value()
            button.setIcon(app.style().standardIcon(PyQt5.QtWidgets.QStyle.SP_MediaVolume))
    
    def changeTimestamp(self, media, controller):
        """
        Changes the timestamp given a 1-100 value from the controller

        Args:\n
            media (QTPieMeida): The media player that holds media
            controller (QTPieSlider or QTPieDial): Controls the videos position from 0-duration values
        """

        media.setPosition(controller.value())
    
    def timestampChanged(self, media, controller):
        """
        Changes the controller when the timestamp changes

        Args:\n
            media (QTPieMeida): The media player that holds media
            controller (QTPieSlider or QTPieDial): Controls the videos position from 0-duration values
        """

        controller.setValue(media.position())

        #Enables autoplay of video
        if (media.position() >= controller.maximum()) and not media.paused:
            media.play()
    
    def durationChanged(self, media, controller):
        """
        Changes the controller when the timestamp changes

        Args:\n
            media (QTPieMeida): The media player that holds media
            controller (QTPieSlider or QTPieDial): Controls the videos position from 0-duration values
        """

        controller.setRange(0, media.duration())
    
    def showControls(self, controls):
        """
        Enables the playPause, volume, and progress widgets passed

        Args:\n
            controls (List of QTPieMedia Controls): A list of QTPieButtons, QTPieSliders or QTPieDial
        """

        for _ in controls:
            _.setHidden(False)
    
    def hideControls(self, controls):
        """
        Enables the playPause, volume, and progress widgets passed

        Args:\n
            controls (List of QTPieMedia Controls): A list of QTPieButtons, QTPieSliders or QTPieDial
        """

        for _ in controls:
            _.setHidden(True)
    
    def openFile(self, media):
        """
        Opens a new file and plays the media

        Args:\n
            media (QTPieMeida): The media player that holds media
        """

        filename, _ = QtWidgets.QFileDialog.getOpenFileName()

        if filename.lower().endswith(('.mp4', '.avi')):
            media.setMedia(PyQt5.QtMultimedia.QMediaContent(PyQt5.QtCore.QUrl.fromLocalFile(filename)))
            media.play()

    def muteUnmute(self, mediaWidget, volumeWidget, app, tunableDict):
        """
        Swaps the mute state of the media

        Args:\n
            mediaWidget (QTPieWidget): The widget that holds all media player widgets.
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

    def volumeHover(self, mediaWidget):
        """
        shows the volume slider bar when hovering over the volume button

        Args:\n
            mediaWidget (QTPieWidget): The widget that holds all media player widgets.
        """

        mediaWidget.volumeBar.show()
    
    def volumeUnhover(self, mediaWidget):
        """
        shows the volume slider bar when hovering over the volume button

        Args:\n
            mediaWidget (QTPieWidget): The widget that holds all media player widgets.
        """

        if not mediaWidget.volumeBar.mouseOn:
            mediaWidget.volumeBar.hide()
