from src.schemas import CapacityBuyer, CapacityCompany, CapacityMarketUnit


def baseline_scenario():
    buyer = CapacityBuyer(
        target_capacity=5,
        net_CONE=50,
    )

    companies = [
        CapacityCompany(
            name="Drax Group",
            units=[
                CapacityMarketUnit(
                    cmu_id="CMU005",
                    name="Drax Power Station - clone",
                    capacity=0.1,
                    min_acceptable_price=51.0,
                ),
                CapacityMarketUnit(
                    cmu_id="CMU001",
                    name="Drax Power Station",
                    capacity=2.6,
                    min_acceptable_price=54.0,
                ),
                CapacityMarketUnit(
                    cmu_id="CMU004",
                    name="Drax Power Station - clone",
                    capacity=2.6,
                    min_acceptable_price=52.0,
                ),
            ],
        ),
        CapacityCompany(
            name="EDF Energy",
            units=[
                CapacityMarketUnit(
                    cmu_id="CMU006",
                    name="some small unit that exits early",
                    capacity=1.3,
                    min_acceptable_price=65.0,
                ),
            ],
        ),
        CapacityCompany(
            name="Orsted",
            units=[
                CapacityMarketUnit(
                    cmu_id="CMU002",
                    name="Hornsea One",
                    capacity=1.2,
                    min_acceptable_price=10.0,
                ),
            ],
        ),
    ]

    return buyer, companies
