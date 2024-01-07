import logging


def logger_setup(name: str):
    """
    Set up and return a configured logger.

    Args:
    name (str): The name of the logger, typically __name__ when used in a module.

    Returns:
    logging.Logger: A configured logger instance.
    """

    # Create a logger with the specified name
    logger = logging.getLogger(name)

    # Set the level of logging. INFO will capture everything from info level and above
    logger.setLevel(logging.INFO)

    # Create a formatter that specifies the format of the log messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create a console handler to output logs to the console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Add the console handler to the logger
    logger.addHandler(console_handler)

    return logger
