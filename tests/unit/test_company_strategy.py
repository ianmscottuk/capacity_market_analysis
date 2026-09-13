import pytest

from src.company_strategy import get_remaining_units
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


@pytest.mark.parametrize(
    "price, expected_remaining, expected_leaving",
    [
        (60, {"CMU001", "CMU002", "CMU003"}, set()),
        (40, {"CMU003"}, {"CMU001", "CMU002"}),
        (20, set(), {"CMU001", "CMU002", "CMU003"}),
    ],
)
def test_get_remaining_units(
    units,
    price,
    expected_remaining,
    expected_leaving,
):
    remaining, leaving = get_remaining_units([], units, price)

    assert {u.cmu_id for u in remaining} == expected_remaining
    assert {u.cmu_id for u in leaving} == expected_leaving
