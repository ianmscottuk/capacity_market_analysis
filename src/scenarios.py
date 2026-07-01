from schemas import CapacityBuyer, CapacityMarketUnit


def baseline_scenario():
    buyer = CapacityBuyer(
        target_capacity_mw=5000.0,
        net_CONE=50,
    )

    units = [
        CapacityMarketUnit(
            cmu_id="CMU001",
            name="Drax Power Station",
            parent_company="Drax Group",
            capacity_mw=2600.0,
            min_acceptable_price=52.0,
            is_price_taker=False,
        ),
        CapacityMarketUnit(
            cmu_id="CMU002",
            name="Hornsea One",
            parent_company="Orsted",
            capacity_mw=1200.0,
            min_acceptable_price=10.0,
            is_price_taker=True,
        ),
        CapacityMarketUnit(
            cmu_id="CMU003",
            name="West Burton CCGT",
            parent_company="EDF Energy",
            capacity_mw=1300.0,
            min_acceptable_price=39.0,
            is_price_taker=False,
        ),
    ]

    return buyer, units
