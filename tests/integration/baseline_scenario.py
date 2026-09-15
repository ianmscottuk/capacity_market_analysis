from src.schemas import CapacityBuyer, CapacityCompany, CapacityMarketUnit


def baseline_scenario_all():
    buyer = CapacityBuyer(
        target_capacity=5,
        net_CONE=50,
    )

    companies = [
        CapacityCompany(
            name="Drax Group",
            units=[
                CapacityMarketUnit(
                    cmu_id="CMU001",
                    name="Drax Power Station - clone",
                    capacity=1,
                    min_acceptable_price=51.0,
                ),
                CapacityMarketUnit(
                    cmu_id="CMU002",
                    name="Drax Power Station",
                    capacity=1,
                    min_acceptable_price=54.0,
                ),
                CapacityMarketUnit(
                    cmu_id="CMU003",
                    name="Drax Power Station - clone",
                    capacity=1,
                    min_acceptable_price=52.0,
                ),
            ],
        ),
        CapacityCompany(
            name="EDF Energy",
            units=[
                CapacityMarketUnit(
                    cmu_id="CMU004",
                    name="some small unit that exits early",
                    capacity=1,
                    min_acceptable_price=65.0,
                ),
            ],
        ),
        CapacityCompany(
            name="Orsted",
            units=[
                CapacityMarketUnit(
                    cmu_id="CMU005",
                    name="Hornsea One",
                    capacity=1,
                    min_acceptable_price=10.0,
                ),
            ],
        ),
    ]

    return buyer, companies


def baseline_scenario_some_leave():
    buyer = CapacityBuyer(
        target_capacity=5,
        net_CONE=50,
    )

    companies = [
        CapacityCompany(
            name="Drax Group",
            units=[
                CapacityMarketUnit(
                    cmu_id="CMU001",
                    name="Drax Power Station - clone",
                    capacity=1,
                    min_acceptable_price=65.0,
                ),
                CapacityMarketUnit(
                    cmu_id="CMU002",
                    name="Drax Power Station",
                    capacity=1,
                    min_acceptable_price=52.0,
                ),
                CapacityMarketUnit(
                    cmu_id="CMU003",
                    name="Drax Power Station - clone",
                    capacity=1,
                    min_acceptable_price=62.0,
                ),
            ],
        ),
        CapacityCompany(
            name="EDF Energy",
            units=[
                CapacityMarketUnit(
                    cmu_id="CMU004",
                    name="some small unit that exits early",
                    capacity=1,
                    min_acceptable_price=50.0,
                ),
            ],
        ),
        CapacityCompany(
            name="Orsted",
            units=[
                CapacityMarketUnit(
                    cmu_id="CMU005",
                    name="Hornsea One",
                    capacity=1,
                    min_acceptable_price=10.0,
                ),
                CapacityMarketUnit(
                    cmu_id="CMU005",
                    name="Hornsea One",
                    capacity=1,
                    min_acceptable_price=20.0,
                ),
                CapacityMarketUnit(
                    cmu_id="CMU005",
                    name="Hornsea One",
                    capacity=1,
                    min_acceptable_price=27.0,
                ),
                CapacityMarketUnit(
                    cmu_id="CMU005",
                    name="Hornsea One",
                    capacity=1,
                    min_acceptable_price=32.0,
                ),
            ],
        ),
    ]

    return buyer, companies


def baseline_scenario_kept():
    buyer = CapacityBuyer(
        target_capacity=5,
        net_CONE=50,
    )

    companies = [
        CapacityCompany(
            name="Drax Group",
            units=[
                CapacityMarketUnit(
                    cmu_id="CMU001",
                    name="Drax Power Station - clone",
                    capacity=1,
                    min_acceptable_price=65.0,
                ),
                CapacityMarketUnit(
                    cmu_id="CMU002",
                    name="Drax Power Station",
                    capacity=1,
                    min_acceptable_price=52.0,
                ),
                CapacityMarketUnit(
                    cmu_id="CMU003",
                    name="Drax Power Station - clone",
                    capacity=1,
                    min_acceptable_price=52.0,
                ),
                CapacityMarketUnit(
                    cmu_id="CMU004",
                    name="Drax Power Station - clone",
                    capacity=1,
                    min_acceptable_price=52.0,
                ),
                CapacityMarketUnit(
                    cmu_id="CMU005",
                    name="Drax Power Station - clone",
                    capacity=1,
                    min_acceptable_price=52.0,
                ),
                CapacityMarketUnit(
                    cmu_id="CMU006",
                    name="Drax Power Station - clone",
                    capacity=1,
                    min_acceptable_price=50.0,
                ),
            ],
        ),
    ]

    return buyer, companies
