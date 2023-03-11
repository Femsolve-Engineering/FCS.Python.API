
import logging
import os

class FCSLogger:
    """
    Class used for logging for all FCS operations.
    """
    def __init__(self, user_id: str, path_to_log_file: str):
        self.logger = logging.getLogger(f'fcs_{user_id}')
        self.logger.setLevel(logging.INFO)
        self.path_to_log_file = path_to_log_file
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setLevel(logging.INFO)
        self.stream_handler.setFormatter(formatter)
        self.logger.addHandler(self.stream_handler)

        self.file_handler = logging.FileHandler(self.path_to_log_file)
        self.file_handler.setLevel(logging.INFO)
        self.file_handler.setFormatter(formatter)
        self.logger.addHandler(self.file_handler)

    def set_logging_context(self, context_name: str) -> None:
        """The logging may refer to a custom addin. If so, we want to indicate that these logging messages
        come from inside plugin.

        Args:
            context_name (str): Name of the application.
        """

        formatter = logging.Formatter(f"{context_name} - %(asctime)s - %(levelname)s - %(message)s")
        self.stream_handler.setFormatter(formatter)
        self.file_handler.setFormatter(formatter)

    def get_log_file_path(self) -> str:
        """Returns path to log file.
        """
        return self.path_to_log_file

    def log(self, message):
        self.logger.info(message)

    def dbg(self, message):
        self.logger.debug(message)

    def wrn(self, message):
        self.logger.warn(message)

    def err(self, message):
        self.logger.error(message)

    def fatal(self, message):
        """These should be errors that indicate the binary backend 
        failed or created unexpected results.
        """
        self.logger.critical(message)