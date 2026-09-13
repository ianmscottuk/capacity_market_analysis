# tests/conftest.py

import pytest

from src.schemas import CapacityMarketUnit


@pytest.fixture
def units():
    return [
        CapacityMarketUnit(
            cmu_id="CMU001",
            name="Unit 1",
            capacity=1.0,
            min_acceptable_price=50.0,
        ),
        CapacityMarketUnit(
            cmu_id="CMU002",
            name="Unit 2",
            capacity=1.0,
            min_acceptable_price=40.0,
        ),
        CapacityMarketUnit(
            cmu_id="CMU003",
            name="Unit 3",
            capacity=1.0,
            min_acceptable_price=30.0,
        ),
    ]
