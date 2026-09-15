import logging

from src.auction import run_auction
from src.company_strategy import get_active_units
from src.utils import get_capacity
from tests.integration.baseline_scenario import (
    baseline_scenario_all,
    baseline_scenario_kept,
    baseline_scenario_some_leave,
)


def test_baseline_scenario_runs_all_in(caplog):
    caplog.set_level(logging.INFO)

    buyer, companies = baseline_scenario_all()

    clearing_price, rounds = run_auction(buyer, companies)

    active_units = get_active_units(companies)

    assert "Auction Started" in caplog.text
    assert "Auction Ended" in caplog.text
    assert len(active_units) == 5
    assert get_capacity(active_units) >= buyer.demand_capacity(clearing_price)


def test_baseline_scenario_some_exit(caplog):
    caplog.set_level(logging.INFO)

    buyer, companies = baseline_scenario_some_leave()

    clearing_price, rounds = run_auction(buyer, companies)

    active_units = get_active_units(companies)

    assert len(active_units) == 5
    assert get_capacity(active_units) >= buyer.demand_capacity(clearing_price)
    assert clearing_price == 50
    assert companies[0].units[0].exit_price == 65
    assert companies[0].units[2].exit_price == 62
    assert companies[0].units[0] not in active_units
    assert companies[0].units[2] not in active_units


def test_baseline_scenario_kept(caplog):
    caplog.set_level(logging.INFO)

    buyer, companies = baseline_scenario_kept()

    clearing_price, rounds = run_auction(buyer, companies)

    active_units = get_active_units(companies)

    assert len(active_units) == 5
    assert get_capacity(active_units) >= buyer.demand_capacity(clearing_price)
    assert clearing_price == 52
    assert companies[0].units[0].exit_price == 65
