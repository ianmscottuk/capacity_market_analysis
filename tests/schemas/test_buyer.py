import pytest

from src.schemas import CapacityBuyer

TARGET = 5.0
NETCONE = 50.0


@pytest.fixture
def buyer():
    return CapacityBuyer(target_capacity=TARGET, net_CONE=NETCONE)


def test_demand_capacity_above_price_cap(buyer):
    with pytest.raises(ValueError):
        buyer.demand_capacity(buyer.price_cap + 1)


def test_demand_capacity_negative(buyer):
    with pytest.raises(ValueError):
        buyer.demand_capacity(-1)


def test_demand_capacity_at_price_cap(buyer):
    assert buyer.demand_capacity(buyer.price_cap) == TARGET - 1.5


def test_demand_capacity_at_net_cone(buyer):
    assert buyer.demand_capacity(NETCONE) == TARGET


def test_demand_capacity_at_zero(buyer):
    assert buyer.demand_capacity(0) == TARGET + 1.5
