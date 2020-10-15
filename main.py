#pylint: disable=C0103, C0301, R0902
"""
The master file for the QTPie Example application.
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys

#First Party Imports
from QTPie.ui import UI
from QTPie.QTPie import QTPie
from tunable import Tunable


class Main:
    """
    Master class for the QTPie Example application.
    """

    def __init__(self):
        """
        Initializes the application.
        """

        self.QTPie = QTPie(icon=r"icon.png", tunableDict=Tunable.tunableDict, title="QTPie")
        self.ui = UI(self.QTPie)
        self.ui.makeLoadPage()
    
if __name__ == "__main__":
    CAS = Main()
