import pytest
from src.schemas import CapacityBuyer


@pytest.fixture
def buyer():
    return CapacityBuyer(
        target_capacity_mw=1000.0,
        price_cap_per_kw_year=75.0,
    )


class TestSpareCapacity:
    @pytest.mark.parametrize("active_capacity_mw,expected", [
        (1200.0, 200.0),   # surplus
        (1000.0, 0.0),     # exactly at target
        (800.0, -200.0),   # shortfall
    ])
    def test_spare_capacity(self, buyer, active_capacity_mw, expected):
        assert buyer.spare_capacity(active_capacity_mw) == expected
