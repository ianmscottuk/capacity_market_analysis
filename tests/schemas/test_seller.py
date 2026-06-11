import pytest
from src.schemas import CapacityMarketUnit


@pytest.fixture
def unit():
    return CapacityMarketUnit(
        cmu_id="CMU001",
        name="Test Plant",
        parent_company="Acme Energy",
        capacity_mw=100.0,
        min_acceptable_price=52.0,
        is_price_taker=False,
    )


class TestCanExitAtPrice:
    @pytest.mark.parametrize(
        "price,expected",
        [
            (51.0, True),
            (52.0, True),
            (60.0, False),
        ],
    )
    def test_exits_when_price_below_minimum(self, unit, price, expected):
        assert (
            unit.can_exit_at_price(
                current_auction_price=price, price_taker_threshold=100.0
            )
            is expected
        )
