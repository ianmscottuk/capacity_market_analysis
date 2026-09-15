import pytest

from src.auction import run_round, select_units_to_keep
from src.schemas import CapacityMarketUnit
from src.utils import get_capacity


def test_run_round_no_units_leave(buyer, units):
    remaining_units, auction_round, clearing_price = run_round(
        round_number=1,
        price=buyer.price_cap,
        buyer=buyer,
        companies=[],
        active_units=units,
    )

    assert remaining_units == units
    assert auction_round.round_number == 1
    assert auction_round.price == buyer.price_cap
    assert clearing_price == None


def test_run_round_retains_units_when_all_try_to_leave(buyer, units):
    remaining_units, auction_round, clearing_price = run_round(
        round_number=5,
        price=10,
        buyer=buyer,
        companies=[],
        active_units=units,
    )

    assert len(remaining_units) == 3
    assert auction_round.round_number == 5
    assert auction_round.price == 10
    assert clearing_price == 10


@pytest.mark.parametrize(
    "min_prices, remaining_capacity, required_capacity, expected_kept_count",
    [
        ([50.0], 5, 6, 1),  # 1 leaving
        ([50.0, 50.0], 5, 6, 1),  # 2 leaving, same min
        ([50.0, 40.0], 5, 6, 1),  # 2 leaving, different mins
    ],
    ids=[
        "1 leaving, need him",
        "2 leaving, same min, need one",
        "2 leaving, different mins, need one",
    ],
)
def test_select_units_to_keep(
    min_prices,
    remaining_capacity,
    required_capacity,
    expected_kept_count,
):
    leaving_units = [
        CapacityMarketUnit(
            cmu_id=f"CMU{i}",
            name=f"Unit {i}",
            capacity=1.0,
            min_acceptable_price=min_price,
        )
        for i, min_price in enumerate(min_prices, start=1)
    ]

    kept = select_units_to_keep(
        leaving_units=leaving_units,
        remaining_capacity=remaining_capacity,
        required_capacity=required_capacity,
    )

    assert len(kept) == expected_kept_count
    assert remaining_capacity + get_capacity(kept) >= required_capacity
    assert kept[0].min_acceptable_price == min(min_prices)
