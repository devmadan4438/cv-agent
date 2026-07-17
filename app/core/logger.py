import logging
import sys

def setup_logger():
    logging.basicConfig(
        level=logging.CRITICAL,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
        ],
    )