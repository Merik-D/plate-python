"""
Module: decorator logged.py
This module provides decorator for logged.
"""
import logging


def logged(exception, mode):
    """
    Decorator for logging exceptions.

    Args:
        exception: The exception type to catch.
        mode: The logging mode ("console" or "file").

    Returns:
        The decorated function.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as ex:
                logger = logging.getLogger(__name__)
                logger.setLevel(logging.ERROR)

                if mode == "console":
                    console_handler = logging.StreamHandler()
                    logger.addHandler(console_handler)
                elif mode == "file":
                    file_handler = logging.FileHandler("log.txt")
                    logger.addHandler(file_handler)

                logger.exception(ex)

        return wrapper

    return decorator
