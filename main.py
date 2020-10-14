#pylint: disable=C0103, C0301, R0902
"""
The master file for the QTPie Example application.
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys

#Allow for Python. relative imports
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

#First Party Imports
from ui import UI
from QTPie import QTPie
from tunable import Tunable


class Main:
    """
    Master class for the QTPie Example application.
    """

    def __init__(self):
        """
        Initializes the application.
        """

        self.QTPie = QTPie(tunableDict=Tunable.tunableDict, title="QTPie")
        self.ui = UI(self.QTPie)
        self.ui.makePage()
    
if __name__ == "__main__":
    CAS = Main()
