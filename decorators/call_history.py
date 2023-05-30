"""
Module: decorator call_history.py
This module provides decorator for call_history.
"""
import datetime
def call_history(file_name):
    def wrapper(func):
        """
        Decorator that logs the method call history to a file.

        Parameters
        ----------
        func : function
            The function to be decorated.

        Returns
        -------
        function
            The decorated function.

        Notes
        -----
        The decorator appends the method name
            and the current timestamp to a CSV file called "call_history.csv".
        The file is created if it doesn't exist and subsequent calls are appended to the existing file.
        The format of each entry in the file is "Method: <method_name>, Time: <timestamp>".
        """
        def decorated_func(*args, **kwargs):
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(f"{file_name}.csv", "a", encoding="utf-8") as file:
                file.write(f"Method: {func.__name__}, Time: {current_time}\n")
            return func(*args, **kwargs)
        return decorated_func
    return wrapper
