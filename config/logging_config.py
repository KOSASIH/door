# config/logging_config.py

import logging
import sys

def setup_logging(level=logging.INFO):
    """Set up logging configuration."""
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),  # Log to standard output
            logging.FileHandler("door_for_pi.log")  # Log to a file
        ]
    )
