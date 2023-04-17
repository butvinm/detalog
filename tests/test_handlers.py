import logging
from os import getenv

import pytest

from detalog.handlers import PingBackHandler


@pytest.fixture
def handler():
    return PingBackHandler(
        app_url=getenv("APP_URL"),
        api_key=getenv("API_KEY"),
    )


@pytest.fixture
def logger(handler: PingBackHandler):
    logger = logging.getLogger("test_logger")
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger


def test_info(handler: PingBackHandler, logger: logging.Logger):
    logger.info("This is an info message")
    assert True


def test_warning(handler: PingBackHandler, logger: logging.Logger):
    logger.warning("This is a warning message")
    assert True


def test_error(handler: PingBackHandler, logger: logging.Logger):
    logger.error("This is an error message")
    assert True


def test_critical(handler: PingBackHandler, logger: logging.Logger):
    logger.critical("This is a critical message")
    assert True


def test_debug(handler: PingBackHandler, logger: logging.Logger):
    logger.debug("This is a debug message")
    assert True


def test_with_channel(handler: PingBackHandler, logger: logging.Logger):
    logger.info("This should be in test channel", extra={"channel": "test"})
    assert True
