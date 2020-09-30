#pylint: disable=C0103, C0301, R0903
"""
Holds a data class with tunable variables
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import json

#Allow for Python. relative imports
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

#First Party Imports
import utilities


class Tunable:
    """
    Tunable variables for Shift
    """

    jsonFile = None
    tunableDict = None

    with open(utilities.resource_path("tunable.json")) as jsonFile:
        tunableDict = json.load(jsonFile)
