import pytest
from detalog.handlers import PingBackHandler


@pytest.fixture
def handler():
    return PingBackHandler()
