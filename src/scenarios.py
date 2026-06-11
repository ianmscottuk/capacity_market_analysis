from schemas import CapacityBuyer, CapacityMarketUnit, AuctionRound


def baseline_scenario():
    buyer = CapacityBuyer(
        target_capacity_mw=5000.0,
        price_cap_per_kw_year=75.0,
    )

    units = [
        CapacityMarketUnit(
            cmu_id="CMU001",
            name="Drax Power Station",
            parent_company="Drax Group",
            capacity_mw=2600.0,
            min_acceptable_price=50.0,
            is_price_taker=False,
        ),
        CapacityMarketUnit(
            cmu_id="CMU002",
            name="Hornsea One",
            parent_company="Orsted",
            capacity_mw=1200.0,
            min_acceptable_price=0.0,
            is_price_taker=True,
        ),
        CapacityMarketUnit(
            cmu_id="CMU003",
            name="West Burton CCGT",
            parent_company="EDF Energy",
            capacity_mw=1300.0,
            min_acceptable_price=55.0,
            is_price_taker=False,
        ),
    ]

    rounds = [
        AuctionRound(
            round_number=1,
            price_cap=75.0,
            price_floor=0.0,
            active_capacity_mw=5100.0,
            exited_capacity_mw=0.0,
        ),
    ]

    return buyer, units, rounds
