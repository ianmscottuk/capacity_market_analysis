import pytest

from src.company_strategy import get_remaining_units


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
