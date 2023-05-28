"""
Module: decorator enforce_snake_case.py
This module provides decorator for enforce_snake_case.
"""
import re

def enforce_snake_case(func):
    """
    Decorator that enforces the snake_case naming convention for method names.

    Parameters:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function.

    Raises:
        ValueError: If the method name does not comply with the snake_case convention.

    Notes:
        The decorator checks if the method name matches the regular expression pattern
        '^[_a-z][_a-z0-9]*$', which represents the snake_case convention. If the method
        name does not comply, a ValueError is raised.
    """
    def wrapper(*args, **kwargs):
        """
        Wrapper function that enforces the snake_case naming convention
            and invokes the original function.

        Parameters:
            *args (tuple): Positional arguments passed to the function.
            **kwargs (dict): Keyword arguments passed to the function.

        Returns:
            object: The result of the original function call.

        Raises:
            ValueError: If the method name does not comply with the snake_case convention.
        """
        method_name = func.__name__
        if not re.match(r'^[a-z_][a-z0-9_]*$', method_name):
            raise ValueError(
                f"Method name '{method_name}' does not comply with snake_case convention.")
        return func(*args, **kwargs)
    return wrapper
