"""
Module: clean_plate_exception.py
This module defines the CleanPlateException class.
"""
class CleanPlateException(Exception):
    """
    A class to represent a CleanPlateException.
    """
    def __init__(self, log_message="The plate is already clean."):
        self.log_message = log_message
