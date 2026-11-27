import logging

from mail_analyzer.logging_config import (
    setup_logging,
)


def test_logging_setup():

    setup_logging()

    logger = logging.getLogger(
        "test"
    )

    logger.info(
        "logging works"
    )

    assert logger is not None