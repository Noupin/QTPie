#pylint: disable=C0103, C0301, R0902
"""
Sets up and maintains the UI for QTPie Example
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import json
import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui

#Allow for Python. relative imports
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

#First Party Imports
import utilities
from actions import Actions
from tunable import Tunable
from UI.dial import QTPieDial
from UI.label import QTPieLabel
from UI.media import QTPieMedia
from UI.video import QTPieVideo
from UI.window import QTPieWindow
from UI.widget import QTPieWidget
from UI.button import QTPieButton
from UI.pixmap import QTPiePixmap
from UI.slider import QTPieSlider
from UI.textbox import QTPieTextbox
from UI.checkbox import QTPieCheckbox
from UI.dropdown import QTPieDropdown
from UI.scrollArea import QTPieScroll
from UI.progressBar import QTPieProgressBar
from UI.radioButton import QTPieRadioButton
from UI.mediaWidget import QTPieMediaWidget
from UI.volumeWidget import QTPieVolumeWidget
from UI.controlWidget import QTPieControlWidget


class QTPie:
    """
    Manages the UI based on the users monitor and position in the application
    """

    def __init__(self, icon=None, tunableDict=json.loads(json.dumps({"windowX": 20, "windowY": 50, "windowWidth": 500, "windowHeight": 500, "volume": 50})), title="Window"):
        """
        Initializing the UI for Forge

        Args:\n
            icon (string, optional): File path to the icon(.ico file) for the top left of the window. Defaults to None.
            tunableDict (JSON, optional): The tunable variables class for saving the windows position on close.
                                          Defaults to {"windowX": 10, "windowY": 10, "windowWidth": 500, "windowHeight": 500}.
            title (str, optional): The name of the window. Defaults to "Window".
        """

        stylesheet = open(utilities.resource_path("QTPie Style\\style.css"), "r")
        self.styling = stylesheet.read()
        stylesheet.close()

        self.actions = Actions()

        self.tunableDict = tunableDict

        self.app = QtWidgets.QApplication(sys.argv)
        self.app.setStyleSheet(self.styling)
        self.app.aboutToQuit.connect(lambda: self.actions.onWindowClose(self.mainWindow))

        if icon:
            appIcon = PyQt5.QtGui.QIcon()
            appIcon.addFile(utilities.resource_path("icon.png"))
            self.app.setWindowIcon(appIcon)

        self.grid = QtWidgets.QGridLayout()
        self.gridCount = 0
        self.grid.setSpacing(0)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.space = self.addLabel([1, 1, 1, 1], txt="", name="Spacer")

        self.window = QTPieWidget()
        self.window.setLayout(self.grid)

        self.mainWindow = QTPieWindow()
        #self.mainWindow.setWindowOpacity(.5)
        self.mainWindow.setGeometry(self.tunableDict["windowX"],
                                    self.tunableDict["windowY"],
                                    self.tunableDict["windowWidth"],
                                    self.tunableDict["windowHeight"])
        self.mainWindow.setWindowTitle(title)
        self.mainWindow.setCentralWidget(self.window)

    def percentToPosition(self, xPos, yPos, width, height):
        """
        Converts percent values to pixel values and returns pixel values for QTPie to use

        Args:\n
            xPos (int, str, float): The x coordinate of the window on the users screen
            yPos (int, str, float):  The y coordinate of the window on the users screen
            width (int, str, float: The width of the window
            height (int, str, float): The height of the window

        Returns:\n
            tuple of int: The arg converted to an int pixel value
        """

        if type(xPos) == str:
            if xPos.find("%") != -1:
                xPos = self.window.size().width()*(int(xPos.replace("%", ""))/100)
        if type(yPos) == str:
            if yPos.find("%") != -1:
                yPos = self.window.size().height()*(int(yPos.replace("%", ""))/100)
        if type(width) == str:
            if width.find("%") != -1:
                width = self.window.size().width()*(int(width.replace("%", ""))/100)
        if type(height) == str:
            if height.find("%") != -1:
                height = self.window.size().height()*(int(height.replace("%", ""))/100)
        
        return int(xPos), int(yPos), int(width), int(height)

    def alignWidget(self, widget, alignment):
        """
        Given an alignment direction the widget is aligned to that direction

        Args:\n
            widget (PyQt5.QtWidgets.QWidget): A PyQt5 widget to be aligned
            alignment (str): A left, right or center string
        """

        alignments = {"left": QtCore.Qt.AlignLeft, "center": QtCore.Qt.AlignCenter, "right": QtCore.Qt.AlignRight}
        widget.setAlignment(alignments[alignment])

    def addGridRow(self, grid, count, columns):
        """
        Adds a row to the given grid on the count

        Args:\n
            grid (PyQt5.QtWidgets.QGridLayout): A grid with count amount of rows
            count (int): The current amount of rows the grid being passed in has
        """

        for _ in range(columns):
            grid.addWidget(self.space, count, _)
            grid.setColumnStretch(_, 1)
        grid.setRowStretch(count, 1)
        #count += 1

    def addLabel(self, gridData, name="", txt="Button", enableDrop=False, align="center"):
        """
        Combines the basic Label code into one function with added functionality and support for css syntax

        Args:\n
            gridData (list of int): List of column, row, columnspan, rowspan values
            name (str, optional): The name for the QTPie stylesheet to specify style. Defaults to "".
            txt (str, optional): The text to be displayed. Defaults to "Button".
            enableDrop (bool, optional): Determines whether drag and drop is enabled. Defaults to False.

        Returns:\n
            QTPieLabel: A PyQt5 label
        """

        label = QTPieLabel(dropArea=enableDrop)
        label.setObjectName(name)
        label.setText(txt)
        label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.alignWidget(label, align)
        self.grid.addWidget(label, gridData[1], gridData[0], gridData[3], gridData[2])

        return label
    
    def addButton(self, gridData, action, name="", txt="Button", enableDrop=False):
        """
        Combines the basic Button code into one function with added functionality and support for css syntax

        Args:\n
            gridData (list of int): List of column, row, columnspan, rowspan values
            action (def): The function to be called on click
            name (str, optional): The name for the QTPie stylesheet to specify style. Defaults to "".
            txt (str, optional): The text the be displayed. Defaults to "Button".
            enableDrop (bool, optional): Determines whether drag and drop is enabled. Defaults to False.

        Returns:\n
            QTPieButton: A PyQt5 push button
        """

        btn = QTPieButton(dropArea=enableDrop)
        btn.setObjectName(name)
        btn.setText(txt)
        btn.clicked.connect(action)
        btn.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.grid.addWidget(btn, gridData[1], gridData[0], gridData[3], gridData[2])

        return btn
    
    def addImage(self, gridData, name="", filename="smile.jpg", keepAR=True, enableDrop=False, align="center"):
        """
        Combines the basic Image code into one function with added functionality and support for CSS syntax

        Args:\n
            gridData (list of int): List of column, row, columnspan, rowspan values
            name (str, optional): The name for the QTPie stylesheet to specify style. Defaults to "".
            filename (str, optional): The filepath for the pixmap image. Defaults to "icon.png".
            keepAR (bool, optional): Whether to keep the original pictures aspect ratio or fit to given width and height. Defaults to True.
            enableDrop (bool, optional): Determines whether drag and drop is enabled. Defaults to False.

        Returns:\n
            QTPieLabel: A PyQt scroll area with a PyQt5 label with a PyQt5 pixmap inside
        """

        name += "Image"

        image = QTPieLabel(dropArea=enableDrop, isImage=True, filename=filename)
        image.pixelMap = QTPiePixmap()
        image.pixelMap = image.pixelMap.fromImage(PyQt5.QtGui.QImage(filename))

        image.setObjectName(name)
        image.setPixmap(image.pixelMap)
        image.setSizePolicy(PyQt5.QtWidgets.QSizePolicy.Ignored, PyQt5.QtWidgets.QSizePolicy.Ignored)
        self.alignWidget(image, align)

        self.grid.addWidget(image, gridData[1], gridData[0], gridData[3], gridData[2])

        return image

    def makeButton(self, clickAction, mouseEnterAction=None, mouseLeaveAction=None, name="", txt="Button", icon="", enableDrop=False, enableHover=False):
        """
        Combines the basic Button code into one function with added functionality and support for css syntax

        Args:\n
            clickAction (def): The function to be called on click.
            mouseEnterAction (def, optional): The function to be called on the mouse entering the button. Defaults to None.
            mouseLeaveAction (def): The function to be called on the mouse leaving the button. Defaults to None.
            name (str, optional): The name for the QTPie stylesheet to specify style. Defaults to "".
            txt (str, optional): The text the be displayed. Defaults to "Button".
            icon (str, optional): The string corresponding to an icon. Defaults to "".
            enableDrop (bool, optional): Determines whether drag and drop is enabled. Defaults to False.
            enableHover (bool, optional): Determines whether hovering signals are enabled. Defaults to False.

        Returns:\n
            QTPieButton: A PyQt5 push button
        """

        icons = {"play": PyQt5.QtWidgets.QStyle.SP_MediaPlay,
                 "pause": PyQt5.QtWidgets.QStyle.SP_MediaPause,
                 "file": PyQt5.QtWidgets.QStyle.SP_FileLinkIcon,
                 "volume": PyQt5.QtWidgets.QStyle.SP_MediaVolume,
                 "muted": PyQt5.QtWidgets.QStyle.SP_MediaVolumeMuted}

        btn = QTPieButton(dropArea=enableDrop, hover=enableHover)
        btn.setObjectName(name)
        if icon in icons:
            btn.setIcon(self.app.style().standardIcon(icons[icon]))
        else:
            btn.setText(txt)
        btn.clicked.connect(clickAction)
        if mouseEnterAction:
            btn.hover = enableHover
            btn.mouseEnter.connect(mouseEnterAction)
        if mouseLeaveAction:
            btn.hover = enableHover
            btn.mouseLeave.connect(mouseLeaveAction)
        btn.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        return btn 

    def makeVolume(self, mediaWidget, volumeWidget):
        """
        Create a volume slider for a given media to be put on a given parent

        Args:\n
            mediaWidget (QTPieMediaWidget): The widget that holds all media player widgets.
            volumeWidget (QTPieVolumeWidget): The holder of a type of media
            parent (QTPieScrollArea or QTPieWidget): The widget for the button to be placed on

        Returns:\n
            QTPieSlider: An extension of the PyQt5 QSlider
        """

        volume = QTPieSlider()
        volume.setObjectName("VideoVolume")
        volume.setOrientation(QtCore.Qt.Horizontal)
        volume.setMinimum(0)
        volume.setMaximum(100)
        #volume.valueChanged.connect(lambda: self.actions.changeVolume(mediaWidget.media, volumeWidget.volumeBar, volumeWidget.volumeBtn, self.app, self.tunableDict))
        volume.setValue(mediaWidget.media.volume())
        volume.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        return volume
    
    def makeVideoProgressBar(self, mediaWidget):
        """
        Create a volume slider for a given media to be put on a given parent

        Args:\n
            mediaWidget (QTPieMediaWidget): The widget that holds all media player widgets.
            parent (QTPieScrollArea or QTPieWidget): The widget for the button to be placed on

        Returns:\n
            QTPieSlider: An extension of the PyQt5 QSlider
        """

        videoProgress = QTPieSlider()
        videoProgress.setObjectName("VideoProgressBar")
        videoProgress.setOrientation(QtCore.Qt.Horizontal)
        videoProgress.setMinimum(0)
        videoProgress.setMaximum(100)
        videoProgress.sliderMoved.connect(lambda: self.actions.changeTimestamp(mediaWidget, videoProgress))
        mediaWidget.media.positionChanged.connect(lambda: self.actions.timestampChanged(mediaWidget, videoProgress))
        mediaWidget.media.durationChanged.connect(lambda: self.actions.durationChanged(mediaWidget, videoProgress))
        videoProgress.setValue(mediaWidget.media.position())
        videoProgress.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        return videoProgress

    def addVideo(self, gridData, name="", filename=r"ChrisH.mp4", enableDrop=False):
        """
        Combines the basic Video code into one function with added functionality and support for CSS syntax

        Args:\n
            gridData (list of int): List of column, row, columnspan, rowspan values
            name (str, optional): The name for the QTPie stylesheet to specify style. Defaults to "".
            filename (str, optional): The filepath for the media player video.
        
        Returns:\n
            QTPieVideo: A PyQt5 media player
        """

        name = "mediaPlayer" + name

        '''Making the widget for the media'''
        mediaWidget = QTPieMediaWidget(doesSignal=True)
        mediaWidget.setObjectName(name)
        mediaWidget.setMouseTracking(True)
        mediaWidget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        #Making video output
        mediaWidget.video = QTPieVideo()
        mediaWidget.video.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        #Making media controller
        mediaWidget.media = QTPieMedia()
        mediaWidget.media.setMedia(PyQt5.QtMultimedia.QMediaContent(PyQt5.QtCore.QUrl.fromLocalFile(filename)))
        mediaWidget.media.setVideoOutput(mediaWidget.video)
        mediaWidget.media.setVolume(self.tunableDict["volume"])
        mediaWidget.media.setObjectName(name)

        mediaWidget.grid = QtWidgets.QGridLayout()
        mediaWidget.grid.setObjectName(name)
        mediaWidget.grid.setSpacing(0)
        mediaWidget.grid.setContentsMargins(0, 0, 0, 0)
        self.addGridRow(mediaWidget.grid, mediaWidget.gridCount, 1)


        '''Making the widget for the media controls'''
        controlWidget = QTPieControlWidget(doesSignal=True)
        controlWidget.setObjectName(name+"Controls")
        controlWidget.setMouseTracking(True)
        controlWidget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        #Making controls for the controlWidget
        controlWidget.playPause = self.makeButton(lambda: self.actions.playPause(mediaWidget, controlWidget, self.app), name="VideoPlayPause", icon="pause")
        controlWidget.openFile = self.makeButton(lambda: self.actions.openFile(mediaWidget), name="VideoOpenFile", icon="file")
        controlWidget.videoProgress = self.makeVideoProgressBar(mediaWidget)


        '''Making the widget for the volume'''
        volumeWidget = QTPieVolumeWidget(doesSignal=True)
        volumeWidget.setObjectName(name+"Volume")
        volumeWidget.setMouseTracking(True)
        volumeWidget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        volumeWidget.grid = QtWidgets.QGridLayout()
        volumeWidget.grid.setObjectName(name+"Volume")
        volumeWidget.grid.setSpacing(0)
        volumeWidget.grid.setContentsMargins(0, 0, 0, 0)
        self.addGridRow(volumeWidget.grid, volumeWidget.gridCount, 6)

        volumeWidget.volumeBar = self.makeVolume(mediaWidget, volumeWidget)
        volumeWidget.volumeBar.valueChanged.connect(lambda: self.actions.changeVolume(mediaWidget, volumeWidget, self.app, self.tunableDict))
        volumeWidget.volumeBtn = self.makeButton(lambda: self.actions.muteUnmute(mediaWidget, volumeWidget, self.app, self.tunableDict),
                                                 mouseEnterAction=lambda: self.actions.volumeHover(volumeWidget),
                                                 name="VideoVolumeBtn", icon="volume", enableHover=True)

        volumeWidget.mouseLeave.connect(lambda: self.actions.volumeUnhover(volumeWidget))

        volumeWidget.grid.addWidget(volumeWidget.volumeBtn, 0, 0, 1, 1)
        volumeWidget.grid.addWidget(volumeWidget.volumeBar, 0, 1, 1, 5)

        volumeWidget.setLayout(volumeWidget.grid)
        volumeWidget.volumeBar.hide()

        controlWidget.volumeWidget = volumeWidget
        controlWidget.updateControls()

        #Setting up resizable grid for the controlWidget
        controlWidget.grid = QtWidgets.QGridLayout()
        controlWidget.grid.setObjectName(name+"Controls")
        controlWidget.grid.setSpacing(0)
        controlWidget.grid.setContentsMargins(0, 0, 0, 0)
        self.addGridRow(controlWidget.grid, controlWidget.gridCount, 12)

        controlWidget.grid.addWidget(controlWidget.playPause, 1, 0, 1, 1)
        controlWidget.grid.addWidget(controlWidget.volumeWidget, 1, 1, 1, 6)
        controlWidget.grid.addWidget(controlWidget.openFile, 1, 11, 1, 1)
        controlWidget.grid.addWidget(controlWidget.videoProgress, 0, 0, 1, 12)

        #Finalizing the controlWidget and connecting actions
        controlWidget.setLayout(controlWidget.grid)
        mediaWidget.clicked.connect(lambda: self.actions.playPause(mediaWidget, controlWidget, self.app))
        mediaWidget.mouseEnter.connect(lambda: self.actions.showControls(controlWidget))
        mediaWidget.mouseLeave.connect(lambda: self.actions.hideControls(mediaWidget, controlWidget))

        mediaWidget.grid.addWidget(mediaWidget.video, 0, 0, 2, 11)
        mediaWidget.grid.addWidget(controlWidget, 1, 0, 1, 11)
        mediaWidget.setLayout(mediaWidget.grid)
        self.grid.addWidget(mediaWidget, gridData[1], gridData[0], gridData[3], gridData[2])
        
        self.actions.hideControls(mediaWidget, controlWidget)
        self.actions.playPause(mediaWidget, controlWidget, self.app)

        return mediaWidget
    
    def addProgressBar(self, gridData, name=""):
        """
        Combines the basic Progress Bar code into one function with added functionality and support for CSS syntax

        Args:\n
            gridData (list of int): List of column, row, columnspan, rowspan values
            name (str, optional): The name for the QTPie stylesheet to specify style. Defaults to "".

        Returns:\n
            QTPieProgressBar: A PyQt5 progress bar
        """

        progressBar = QTPieProgressBar()
        progressBar.setObjectName(name)
        progressBar.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.grid.addWidget(progressBar, gridData[1], gridData[0], gridData[3], gridData[2])

        
        return progressBar
    
    def addSlider(self, gridData, action, name="", orientation="horizontal", minVal=0, maxVal=100):
        """
        Combines the basic Slider code into one function with added functionality and support for CSS syntax

        Args:\n
            gridData (list of int): List of column, row, columnspan, rowspan values
            action (def): The function to be called when the slider is moved
            name (str, optional): The name for the QTPie stylesheet to specify style. Defaults to "".
            orientation (str, optional): Whether the slider is vertical or horizontal. Defaults to "horizontal".
            minVal (int, optional): Minimum slider value. Defaults to 0.
            maxVal (int, optional): Maximum slider value. Defaults to 100.

        Returns:\n
            QTPieSlider: A PyQt5 slider
        """

        orientationDict = {"horizontal": QtCore.Qt.Horizontal, "vertical": QtCore.Qt.Vertical}

        slider = QTPieSlider()
        slider.setObjectName(name)
        slider.setOrientation(orientationDict[orientation])
        slider.setMinimum(minVal)
        slider.setMaximum(maxVal)
        slider.valueChanged.connect(action)
        slider.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.grid.addWidget(slider, gridData[1], gridData[0], gridData[3], gridData[2])

        return slider
    
    def addRadioButton(self, gridData, name="", txt="RadioButton"):
        """
        Combines the basic Radio Button code into one function with added functionality and support for CSS syntax

        Args:\n
            gridData (list of int): List of column, row, columnspan, rowspan values
            name (str, optional): The name for the QTPie stylesheet to specify style. Defaults to "".
            txt (str, optional): The text the be displayed. Defaults to "RadioButton".

        Returns:\n
            QTPieRadioButton: A PyQt5 radio button with a text tag
        """

        radioButton = QTPieRadioButton()
        radioButton.setObjectName(name)
        radioButton.setText(txt)
        radioButton.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.grid.addWidget(radioButton, gridData[1], gridData[0], gridData[3], gridData[2])

        return radioButton
    
    def addCheckbox(self, gridData, name="", txt="Checkbox"):
        """
        Combines the basic Checkbox code into one function with added functionality and support for CSS syntax

        Args:\n
            gridData (list of int): List of column, row, columnspan, rowspan values
            name (str, optional): The name for the QTPie stylesheet to specify style. Defaults to "".
            txt (str, optional): The text the be displayed. Defaults to "Checkbox".

        Returns:\n
            QTPieCheckbox: A PyQt5 checkbox with a text tag
        """

        checkbox = QTPieCheckbox()
        checkbox.setObjectName(name)
        checkbox.setText(txt)
        checkbox.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.grid.addWidget(checkbox, gridData[1], gridData[0], gridData[3], gridData[2])

        return checkbox

    def addTextbox(self, gridData, name="", align="left"):
        """
        Combines the basic Textbox code into one function with added functionality and support for CSS syntax

        Args:\n
            gridData (list of int): List of column, row, columnspan, rowspan values
            name (str, optional): The name for the QTPie stylesheet to specify style. Defaults to "".

        Returns:\n
            QTPieTextbox: A PyQt5 textbox with drag and drop optional
        """

        textbox = QTPieTextbox()
        textbox.setObjectName(name)
        textbox.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.alignWidget(textbox, align)
        self.grid.addWidget(textbox, gridData[1], gridData[0], gridData[3], gridData[2])

        return textbox

    def addDial(self, gridData, action, name="", minVal=0, maxVal=100, wrapping=True):
        """
        Combines the basic Dial code into one function with added functionality and support for CSS syntax

        Args:\n
            gridData (list of int): List of column, row, columnspan, rowspan values
            action (def): The function to be called when the dial is rotated
            name (str, optional): The name for the QTPie stylesheet to specify style. Defaults to "".
            minVal (int, optional): Minimum slider value. Defaults to 0.
            maxVal (int, optional): Maximum slider value. Defaults to 100.
            wrapping (bool, optional): Whether the dial can completely circle around. Defaults to True.

        Returns:\n
            QTPieDial: A PyQt5 dial
        """

        dial = QTPieDial(wrapping=wrapping)
        dial.setObjectName(name)
        dial.setMinimum(minVal)
        dial.setMaximum(maxVal)
        dial.valueChanged.connect(action)
        dial.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.grid.addWidget(dial, gridData[1], gridData[0], gridData[3], gridData[2])

        return dial

    def addDropdown(self, gridData, name="", align="left", textEdit=False, autocomp=False, values=[]):
        """
        Combines the basic AutofillBox code into one function with added functionality and support for CSS syntax

        Args:\n
            gridData (list of int): List of column, row, columnspan, rowspan values
            name (str, optional): The name for the QTPie stylesheet to specify style. Defaults to "".
            align (str, optional): The alignment for the text. Defaults to "left".
            textEdit (bool, optional): Determines whether the user can type or not. Defaults to False.
            autocomp (bool, optional): Determines whether the dropdown autocompletes the text. Defaults to False.
            values (list of str, optional): The autocomplete values. Defaults to [].

        Returns:\n
            QTPieTextbox: A PyQt5 combobox with a set of autofill values
        """

        dropdown = QTPieDropdown()
        dropdown.setObjectName(name)
        dropdown.setEditable(textEdit)
        dropdown.setAutoFillBackground(autocomp)
        for _ in values:
            dropdown.addItem(_)
        dropdown.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.grid.addWidget(dropdown, gridData[1], gridData[0], gridData[3], gridData[2])

        return dropdown

    def createMenu(self):
        """
        Makes the menu bar like most applications have at the top of the screen
        """

        mainMenu = self.mainWindow.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        helpMenu = mainMenu.addMenu('Help')

        copyAction = QtWidgets.QAction('Copy', self.window)
        copyAction.setShortcut("Ctrl+C")
        fileMenu.addAction(copyAction)

        saveAction = QtWidgets.QAction('Save', self.window)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)

        pasteAction = QtWidgets.QAction('Paste', self.window)
        pasteAction.setShortcut("Ctrl+P")
        fileMenu.addAction(pasteAction)

        exitAction = QtWidgets.QAction(QtGui.QIcon("exit.png"), 'Exit', self.window)
        exitAction.setShortcut("Ctrl+E")
        #exitAction.triggered.connect(self.exitWindow)
        fileMenu.addAction(exitAction)
