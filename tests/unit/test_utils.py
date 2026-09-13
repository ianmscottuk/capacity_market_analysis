import pytest

from src.utils import capacity_met


@pytest.mark.parametrize(
    "demand, expected",
    [
        (2.0, True),
        (3.0, True),
        (3.1, False),
    ],
)
def test_capacity_met(units, demand, expected):
    assert capacity_met(demand, units) is expected
