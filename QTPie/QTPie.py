#pylint: disable=C0103, C0301, R0902
"""
Sets up and maintains the UI for QTPie Example.
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
from tunable import Tunable
from QTPie.actions import Actions
from QTPie.UI.dial import QTPieDial
from QTPie.UI.image import QTPieImage
from QTPie.UI.label import QTPieLabel
from QTPie.UI.media import QTPieMedia
from QTPie.UI.video import QTPieVideo
from QTPie.UI.button import QTPieButton
from QTPie.UI.pixmap import QTPiePixmap
from QTPie.UI.slider import QTPieSlider
from QTPie.UI.widget import QTPieWidget
from QTPie.UI.window import QTPieWindow
from QTPie.UI.textbox import QTPieTextbox
from QTPie.UI.checkbox import QTPieCheckbox
from QTPie.UI.dropdown import QTPieDropdown
from QTPie.UI.scrollArea import QTPieScroll
from QTPie.UI.mediaWidget import QTPieMediaWidget
from QTPie.UI.progressBar import QTPieProgressBar
from QTPie.UI.radioButton import QTPieRadioButton
from QTPie.UI.volumeWidget import QTPieVolumeWidget
from QTPie.UI.controlWidget import QTPieControlWidget


class QTPie:
    """
    Manages the UI based on the users monitor and position in the application.
    """

    def __init__(self, icon=None, tunableDict=json.loads(json.dumps({"windowX": 20, "windowY": 50, "windowWidth": 500, "windowHeight": 500, "volume": 50})), title="Window"):
        """
        Initializing the UI for Forge.

        Args:\n
            icon (string, optional): File path to the icon(.ico file) for the top left of the window. Defaults to None.
            tunableDict (JSON, optional): The tunable variables class for saving the windows position on close.
                                          Defaults to {"windowX": 10, "windowY": 10, "windowWidth": 500, "windowHeight": 500}.
            title (str, optional): The name of the window. Defaults to "Window".
        """

        stylesheet = open(utilities.resource_path("QTPie\\QTPie Style\\style.css"), "r")
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
        self.space = self.makeLabel(txt="", name="Spacer", addToGrid=False)

        self.window = QTPieWidget()
        self.window.setLayout(self.grid)

        self.mainWindow = QTPieWindow()
        self.mainWindow.setGeometry(self.tunableDict["windowX"],
                                    self.tunableDict["windowY"],
                                    self.tunableDict["windowWidth"],
                                    self.tunableDict["windowHeight"])
        self.mainWindow.setWindowTitle(title)
        self.mainWindow.setCentralWidget(self.window)

    def percentToPosition(self, xPos, yPos, width, height):
        """
        Converts percent values to pixel values and returns pixel values for QTPie to use.

        Args:\n
            xPos (int, str, float): The x coordinate of the window on the users screen.
            yPos (int, str, float):  The y coordinate of the window on the users screen.
            width (int, str, float: The width of the window.
            height (int, str, float): The height of the window.

        Returns:\n
            tuple of int: The arg converted to an int pixel value.
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
        Given an alignment direction the widget is aligned to that direction.

        Args:\n
            widget (PyQt5.QtWidgets.QWidget): A PyQt5 widget to be aligned.
            alignment (str): A left, right or center string.
        """

        alignments = {"left": QtCore.Qt.AlignLeft, "center": QtCore.Qt.AlignCenter, "right": QtCore.Qt.AlignRight}
        widget.setAlignment(alignments[alignment.lower()])

    def addGridRow(self, grid, count, columns):
        """
        Adds a row to the given grid on the count.

        Args:\n
            grid (PyQt5.QtWidgets.QGridLayout): A grid with count amount of rows.
            count (int): The current amount of rows the grid being passed in has.
            columns (int): The amount of columns to be added to each row.
        """

        for _ in range(columns):
            grid.addWidget(self.space, count, _)
            grid.setColumnStretch(_, 1)
        grid.setRowStretch(count, 1)

    def makeLabel(self, name="", txt="Button", enableDrop=False, align="center", addToGrid=True, gridData=[0, 0, 0, 0]):
        """
        Combines the basic Label code into one function with added functionality and support for css syntax.

        Args:\n
            name (str, optional): The name for the QTPie stylesheet to specify style. Defaults to "".
            txt (str, optional): The text to be displayed. Defaults to "Button".
            enableDrop (bool, optional): Determines whether drag and drop is enabled. Defaults to False.
            align (str, optional): left, right, center alignment of the content of the label. Defaults to "center".
            addToGrid (bool, optional): Determines whether to add to the main grid or not. Defaults to True.
            gridData (list of int, optional): List of column, row, columnspan, rowspan values. Defaults to [0, 0, 0, 0].

        Returns:\n
            QTPieLabel: A QTPie label.
        """

        label = QTPieLabel(dropArea=enableDrop)
        label.setObjectName(name)
        label.setText(txt)
        label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.alignWidget(label, align)

        if addToGrid:
            self.grid.addWidget(label, gridData[1], gridData[0], gridData[3], gridData[2])

        return label
    
    def makeImage(self, name="", filename=r"smile.jpg", keepAR=True, enableDrop=False, align="center", addToGrid=True, gridData=[0, 0, 0, 0]):
        """
        Combines the basic Image code into one function with added functionality and support for CSS syntax

        Args:\n
            name (str, optional): The name for the QTPie stylesheet to specify style. Defaults to "".
            filename (str, optional): The filepath for the pixmap image. Defaults to "icon.png".
            keepAR (bool, optional): Whether to keep the original pictures aspect ratio or fit to given width and height. Defaults to True.
            enableDrop (bool, optional): Determines whether drag and drop is enabled. Defaults to False.
            align (str, optional): left, right, center alignment of the content of the label. Defaults to "center".
            addToGrid (bool, optional): Determines whether to add to the main grid or not. Defaults to True.
            gridData (list of int, optional): List of column, row, columnspan, rowspan values. Defaults to [0, 0, 0, 0].

        Returns:\n
            QTPieImage: A QTPie image with a pixmamp in it and extending the QTPieLabel
        """

        name += "Image"

        image = QTPieImage(dropArea=enableDrop, filename=filename)
        image.pixelMap = QTPiePixmap()
        image.pixelMap = image.pixelMap.fromImage(PyQt5.QtGui.QImage(filename))

        image.setObjectName(name)
        image.setPixmap(image.pixelMap)
        image.setSizePolicy(PyQt5.QtWidgets.QSizePolicy.Ignored, PyQt5.QtWidgets.QSizePolicy.Ignored)
        self.alignWidget(image, align)

        if addToGrid:
            self.grid.addWidget(image, gridData[1], gridData[0], gridData[3], gridData[2])

        return image

    def makeButton(self, clickAction, mouseEnterAction=None, mouseLeaveAction=None, name="", txt="Button", icon="", enableDrop=False, enableHover=False, addToGrid=True, gridData=[0, 0, 0, 0]):
        """
        Combines the basic Button code into one function with added functionality and support for css syntax. Optional to apply to grid.

        Args:\n
            clickAction (def): The function to be called on click.
            mouseEnterAction (def, optional): The function to be called on the mouse entering the button. Defaults to None.
            mouseLeaveAction (def, optional): The function to be called on the mouse leaving the button. Defaults to None.
            name (str, optional): The name for the QTPie stylesheet to specify style. Defaults to "".
            txt (str, optional): The text the be displayed. Defaults to "Button".
            icon (str, optional): The string corresponding to an icon. Defaults to "".
            enableDrop (bool, optional): Determines whether drag and drop is enabled. Defaults to False.
            enableHover (bool, optional): Determines whether hovering signals are enabled. Defaults to False.
            addToGrid (bool, optional): Determines whether to add to the main grid or not. Defaults to True.
            gridData (list of int, optional): List of column, row, columnspan, rowspan values. Defaults to [0, 0, 0, 0].

        Returns:\n
            QTPieButton: A PyQt5 push button.
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

        if addToGrid:
            self.grid.addWidget(btn, gridData[1], gridData[0], gridData[3], gridData[2])

        return btn 

    def makeVolume(self, mediaWidget, volumeWidget):
        """
        Create a volume slider for a given media. Does not apply to grid.

        Args:\n
            mediaWidget (QTPieMediaWidget): The widget that holds all media player widgets.
            volumeWidget (QTPieVolumeWidget): The widget that holds all volume widgets.
            parent (QTPieScrollArea or QTPieWidget): The widget for the button to be placed on.

        Returns:\n
            QTPieSlider: A QTPie slider.
        """

        volume = QTPieSlider()
        volume.setObjectName("VideoVolume")
        volume.setOrientation(QtCore.Qt.Horizontal)
        volume.setMinimum(0)
        volume.setMaximum(100)
        volume.setValue(mediaWidget.media.volume())
        volume.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        volume.valueChanged.connect(lambda: self.actions.changeVolume(mediaWidget, volumeWidget, self.app, self.tunableDict))

        return volume
    
    def makeVideoProgressBar(self, mediaWidget):
        """
        Create a volume slider for a given media. Does not apply to grid.

        Args:\n
            mediaWidget (QTPieMediaWidget): The widget that holds all media player widgets.

        Returns:\n
            QTPieSlider: A QTPie slider.
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

    def setupWidget(self, widget, name="", makeGrid=True, columns=1, rows=1):
        """
        Boilerplate for the QTPie widgets.

        Args:\n
            widget (QTPieWidget or super(QTPieWidget)): The widget to be setup.
            name (str, optional): The name for the style sheet. Defaults to "".
            makeGrid (bool, optional): Whether the grid is setup immediatley or not. Defautls to True.
            columns (int, optional): The number of columns per row of the grid. Defaults to 1.
            rows (int, optional): The number of rows in the grid. Defaults to 1.
        """

        widget.setObjectName(name)
        widget.setMouseTracking(True)
        widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        if makeGrid:
            self.setupGrid(widget, name, columns, rows)
        
    def setupGrid(self, widget, name="", columns=1, rows=1):
        """
        Boilerplate for the PyQt5 QGridLayout's.

        Args:\n
            widget (QTPieWidget or super(QTPieWidget)): The widget to be setup.
            name (str, optional): The name for the style sheet. Defaults to "".
            columns (int, optional): The number of columns per row of the grid. Defaults to 1.
            rows (int, optional): The number of rows in the grid. Defaults to 1.
        """

        widget.grid = QtWidgets.QGridLayout()
        widget.grid.setObjectName(name)
        widget.grid.setSpacing(0)
        widget.grid.setContentsMargins(0, 0, 0, 0)

        for i in range(rows):
            self.addGridRow(widget.grid, widget.gridCount, columns)
            widget.gridCount += 1

    def makeVideo(self, name="", filename=r"ChrisH.mp4", enableDrop=False, addToGrid=True, gridData=[0, 0, 0, 0]):
        """
        Combines the basic Video code into one function with added functionality and support for CSS syntax.

        Args:\n
            name (str, optional): The name for the QTPie stylesheet to specify style. Defaults to "".
            filename (str, optional): The filepath for the media player video.
            addToGrid (bool, optional): Determines whether to add to the main grid or not. Defaults to True.
            gridData (list of int, optional): List of column, row, columnspan, rowspan values. Defaults to [0, 0, 0, 0].
        
        Returns:\n
            QTPieVideo: A PyQt5 media player
        """

        name = "mediaPlayer" + name

        '''Making the widget for the media'''
        mediaWidget = QTPieMediaWidget(doesSignal=True, dropArea=True)
        self.setupWidget(mediaWidget, name=name)

        #Assigning video to mediaWidget
        mediaWidget.video = QTPieVideo()
        mediaWidget.video.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        #Assigning media to mediaWidget
        mediaWidget.media = QTPieMedia()
        mediaWidget.media.setMedia(PyQt5.QtMultimedia.QMediaContent(PyQt5.QtCore.QUrl.fromLocalFile(filename)))
        mediaWidget.media.setVideoOutput(mediaWidget.video)
        mediaWidget.media.setVolume(self.tunableDict["volume"])
        mediaWidget.media.setObjectName(name)


        '''Making the widget for the media controls'''
        controlWidget = QTPieControlWidget(doesSignal=True)
        self.setupWidget(controlWidget, name=name+"Controls", columns=12)

        #Assigning widgets for the controlWidget
        controlWidget.playPause = self.makeButton(lambda: self.actions.playPause(mediaWidget, controlWidget, self.app), name="VideoPlayPause", icon="pause", addToGrid=False)
        controlWidget.openFile = self.makeButton(lambda: self.actions.openFile(mediaWidget), name="VideoOpenFile", icon="file", addToGrid=False)
        controlWidget.videoProgress = self.makeVideoProgressBar(mediaWidget)


        '''Making the widget for the volume controls'''
        volumeWidget = QTPieVolumeWidget(doesSignal=True)
        self.setupWidget(volumeWidget, name=name+"Volume", columns=6)

        #Assigning widgets for the volumeWidget
        volumeWidget.volumeBar = self.makeVolume(mediaWidget, volumeWidget)
        volumeWidget.volumeBtn = self.makeButton(lambda: self.actions.muteUnmute(mediaWidget, volumeWidget, self.app, self.tunableDict),
                                                 mouseEnterAction=lambda: self.actions.volumeHover(volumeWidget),
                                                 name="VideoVolumeBtn", icon="volume", enableHover=True, addToGrid=False)

        volumeWidget.mouseLeave.connect(lambda: self.actions.volumeUnhover(volumeWidget))

        #Adding widgets to volumeWidget grid layout
        volumeWidget.grid.addWidget(volumeWidget.volumeBtn, 0, 0, 1, 1)
        volumeWidget.grid.addWidget(volumeWidget.volumeBar, 0, 1, 1, 2)

        #Setting layout of volumeWidget to grid
        volumeWidget.setLayout(volumeWidget.grid)
        volumeWidget.volumeBar.hide()

        #Assigning volume widget to controlWidget
        controlWidget.volumeWidget = volumeWidget
        controlWidget.updateControls()

        #Adding widgets to controlWidget grid layout
        controlWidget.grid.addWidget(controlWidget.playPause, 1, 0, 1, 1)
        controlWidget.grid.addWidget(controlWidget.volumeWidget, 1, 1, 1, 6)
        controlWidget.grid.addWidget(controlWidget.openFile, 1, 11, 1, 1)
        controlWidget.grid.addWidget(controlWidget.videoProgress, 0, 0, 1, 12)

        #Finalizing the controlWidget and connecting actions
        controlWidget.setLayout(controlWidget.grid)

        #Connecting actions to the mediaWidget
        mediaWidget.clicked.connect(lambda: self.actions.playPause(mediaWidget, controlWidget, self.app))
        mediaWidget.mouseEnter.connect(lambda: self.actions.showControls(controlWidget))
        mediaWidget.mouseLeave.connect(lambda: self.actions.hideControls(mediaWidget, controlWidget))

        #Adding widgets to mediaWidget grid layout
        mediaWidget.grid.addWidget(mediaWidget.video, 0, 0, 20, 11)
        mediaWidget.grid.addWidget(controlWidget, 18, 0, 2, 11)
        mediaWidget.setLayout(mediaWidget.grid)
        
        self.actions.hideControls(mediaWidget, controlWidget)
        self.actions.playPause(mediaWidget, controlWidget, self.app)

        if addToGrid:
            self.grid.addWidget(mediaWidget, gridData[1], gridData[0], gridData[3], gridData[2])

        return mediaWidget
    
    def makeProgressBar(self, name="", addToGrid=True, gridData=[0, 0, 0, 0]):
        """
        Combines the basic Progress Bar code into one function with added functionality and support for CSS syntax.

        Args:\n
            name (str, optional): The name for the QTPie stylesheet to specify style. Defaults to "".
            addToGrid (bool, optional): Determines whether to add to the main grid or not. Defaults to True.
            gridData (list of int, optional): List of column, row, columnspan, rowspan values. Defaults to [0, 0, 0, 0].

        Returns:\n
            QTPieProgressBar: A QTPie progress bar.
        """

        progressBar = QTPieProgressBar()
        progressBar.setObjectName(name)
        progressBar.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        if addToGrid:
            self.grid.addWidget(progressBar, gridData[1], gridData[0], gridData[3], gridData[2])
        
        return progressBar
    
    def makeSlider(self, action, name="", orientation="horizontal", minVal=0, maxVal=100, addToGrid=True, gridData=[0, 0, 0, 0]):
        """
        Combines the basic Slider code into one function with added functionality and support for CSS syntax.

        Args:\n
            action (def): The function to be called when the slider is moved.
            name (str, optional): The name for the QTPie stylesheet to specify style. Defaults to "".
            orientation (str, optional): Whether the slider is vertical or horizontal. Defaults to "horizontal".
            minVal (int, optional): Minimum slider value. Defaults to 0.
            maxVal (int, optional): Maximum slider value. Defaults to 100.
            addToGrid (bool, optional): Determines whether to add to the main grid or not. Defaults to True.
            gridData (list of int, optional): List of column, row, columnspan, rowspan values. Defaults to [0, 0, 0, 0].

        Returns:\n
            QTPieSlider: A QTPie slider.
        """

        orientationDict = {"horizontal": QtCore.Qt.Horizontal, "vertical": QtCore.Qt.Vertical}

        slider = QTPieSlider()
        slider.setObjectName(name)
        slider.setOrientation(orientationDict[orientation])
        slider.setMinimum(minVal)
        slider.setMaximum(maxVal)
        slider.valueChanged.connect(action)
        slider.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        if addToGrid:
            self.grid.addWidget(slider, gridData[1], gridData[0], gridData[3], gridData[2])

        return slider
    
    def makeRadioButton(self, name="", txt="RadioButton", addToGrid=True, gridData=[0, 0, 0, 0]):
        """
        Combines the basic Radio Button code into one function with added functionality and support for CSS syntax.

        Args:\n
            name (str, optional): The name for the QTPie stylesheet to specify style. Defaults to "".
            txt (str, optional): The text the be displayed. Defaults to "RadioButton".
            addToGrid (bool, optional): Determines whether to add to the main grid or not. Defaults to True.
            gridData (list of int, optional): List of column, row, columnspan, rowspan values. Defaults to [0, 0, 0, 0].

        Returns:\n
            QTPieRadioButton: A QTPie radio button with a text tag.
        """

        radioButton = QTPieRadioButton()
        radioButton.setObjectName(name)
        radioButton.setText(txt)
        radioButton.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        if addToGrid:
            self.grid.addWidget(radioButton, gridData[1], gridData[0], gridData[3], gridData[2])

        return radioButton
    
    def makeCheckbox(self, name="", txt="Checkbox", addToGrid=True, gridData=[0, 0, 0, 0]):
        """
        Combines the basic Checkbox code into one function with added functionality and support for CSS syntax.

        Args:\n
            name (str, optional): The name for the QTPie stylesheet to specify style. Defaults to "".
            txt (str, optional): The text the be displayed. Defaults to "Checkbox".
            addToGrid (bool, optional): Determines whether to add to the main grid or not. Defaults to True.
            gridData (list of int, optional): List of column, row, columnspan, rowspan values. Defaults to [0, 0, 0, 0].

        Returns:\n
            QTPieCheckbox: A QTPie checkbox with a text tag.
        """

        checkbox = QTPieCheckbox()
        checkbox.setObjectName(name)
        checkbox.setText(txt)
        checkbox.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        if addToGrid:
            self.grid.addWidget(checkbox, gridData[1], gridData[0], gridData[3], gridData[2])

        return checkbox

    def makeTextbox(self, name="", align="left", enableDrop=False, addToGrid=True, gridData=[0, 0, 0, 0]):
        """
        Combines the basic Textbox code into one function with added functionality and support for CSS syntax.

        Args:\n
            name (str, optional): The name for the QTPie stylesheet to specify style. Defaults to "".
            aling (str, optional): left, right, center alignment of the content of the label. Defaults to "left".
            enableDrop (bool, optional): Enables or disables text droppping into the text box. Defaults to False.
            addToGrid (bool, optional): Determines whether to add to the main grid or not. Defaults to True.
            gridData (list of int, optional): List of column, row, columnspan, rowspan values. Defaults to [0, 0, 0, 0].

        Returns:\n
            QTPieTextbox: A QTPie textbox with drag and drop optional
        """

        textbox = QTPieTextbox(dropArea=enableDrop)
        textbox.setObjectName(name)
        textbox.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.alignWidget(textbox, align)

        if addToGrid:
            self.grid.addWidget(textbox, gridData[1], gridData[0], gridData[3], gridData[2])

        return textbox

    def makeDial(self, action, name="", minVal=0, maxVal=100, wrapping=True, addToGrid=True, gridData=[0, 0, 0, 0]):
        """
        Combines the basic Dial code into one function with added functionality and support for CSS syntax.

        Args:\n
            action (def): The function to be called when the dial is rotated.
            name (str, optional): The name for the QTPie stylesheet to specify style. Defaults to "".
            minVal (int, optional): Minimum slider value. Defaults to 0.
            maxVal (int, optional): Maximum slider value. Defaults to 100.
            wrapping (bool, optional): Whether the dial can completely circle around. Defaults to True.
            addToGrid (bool, optional): Determines whether to add to the main grid or not. Defaults to True.
            gridData (list of int, optional): List of column, row, columnspan, rowspan values. Defaults to [0, 0, 0, 0].

        Returns:\n
            QTPieDial: A QTPie dial.
        """

        dial = QTPieDial(wrapping=wrapping)
        dial.setObjectName(name)
        dial.setMinimum(minVal)
        dial.setMaximum(maxVal)
        dial.valueChanged.connect(action)
        dial.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        if addToGrid:
            self.grid.addWidget(dial, gridData[1], gridData[0], gridData[3], gridData[2])

        return dial

    def makeDropdown(self, name="", align="left", textEdit=False, autocomp=False, values=[], addToGrid=True, gridData=[0, 0, 0, 0]):
        """
        Combines the basic AutofillBox code into one function with added functionality and support for CSS syntax.

        Args:\n
            name (str, optional): The name for the QTPie stylesheet to specify style. Defaults to "".
            align (str, optional): The alignment for the text. Defaults to "left".
            textEdit (bool, optional): Determines whether the user can type or not. Defaults to False.
            autocomp (bool, optional): Determines whether the dropdown autocompletes the text. Defaults to False.
            values (list of str, optional): The autocomplete values. Defaults to [].
            addToGrid (bool, optional): Determines whether to add to the main grid or not. Defaults to True.
            gridData (list of int, optional): List of column, row, columnspan, rowspan values. Defaults to [0, 0, 0, 0].

        Returns:\n
            QTPieTextbox: A QTPie dropdown with a set of autofill values
        """

        dropdown = QTPieDropdown()
        dropdown.setObjectName(name)
        dropdown.setEditable(textEdit)
        dropdown.setAutoFillBackground(autocomp)
        for _ in values:
            dropdown.addItem(_)
        dropdown.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        if addToGrid:
            self.grid.addWidget(dropdown, gridData[1], gridData[0], gridData[3], gridData[2])

        return dropdown

    def createMenu(self):
        """
        Makes the menu bar like most applications have at the top of the screen.
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
        fileMenu.addAction(exitAction)
