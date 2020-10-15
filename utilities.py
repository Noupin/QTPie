#pylint: disable=C0103, C0301, R0903, E1101
"""
No-self-use functions for QTPie.
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import json


def changeJSON(key, value):
    """
    Takes a key and a value to change the tunable JSON file.
    """

    with open(resource_path(r"tunable.json")) as jsonFile:
        tunableDict = json.load(jsonFile)

    tunableDict[key] = value

    with open(resource_path(r"tunable.json"), 'w') as jsonFile:
        json.dump(tunableDict, jsonFile)

def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller.
    """

    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
