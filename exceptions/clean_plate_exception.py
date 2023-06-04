class CleanPlateException(Exception):
    def __init__(self, log_message="The plate is already clean."):
        self.log_message = log_message
