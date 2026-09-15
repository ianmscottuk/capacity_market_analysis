from src.company_strategy import get_remaining_units
from src.logger import get_logger
from src.schemas import AuctionRound
from src.utils import capacity_met, get_capacity

logger = get_logger(__name__)


def run_auction(buyer, companies, price_step=-1):

    units = [unit for company in companies for unit in company.units]

    price = buyer.price_cap + price_step
    active_units = units.copy()
    round_number = 1
    rounds = []

    logger.info("Auction Started")

    while price > 0:
        active_units, auction_round, clearing_price = run_round(
            round_number=round_number,
            price=price,
            buyer=buyer,
            companies=companies,
            active_units=active_units,
        )

        rounds.append(auction_round)

        price += price_step
        round_number += 1

        if clearing_price is not None:
            break

    # TODO: calc profit of each company
    print("endex!")


def run_round(round_number, price, buyer, companies, active_units):
    logger.info(
        "Round %s | price=%s | active_units=%s",
        round_number,
        price,
        len(active_units),
    )
    clearing_price = None
    remaining_units, leaving_units = get_remaining_units(
        companies=companies, active_units=active_units, price=price
    )

    if leaving_units:
        logger.info("Someone wants to exit....")

        if not capacity_met(buyer.demand_capacity(price), remaining_units):
            clearing_price = price
            logger.info(
                "Remaining capacity is now below demand.\n"
                "Auction cleared at £%.2f/kW/year.\n"
                "Some attempted exits must be retained to satisfy required capacity.",
                clearing_price,
            )

            keep = select_units_to_keep(
                leaving_units=leaving_units,
                remaining_capacity=get_capacity(remaining_units),
                required_capacity=buyer.demand_capacity(price),
            )
            remaining_units = remaining_units + keep
        set_exit_price(active_units, remaining_units, price)

    active_capacity = get_capacity(remaining_units)
    exited_capacity = get_capacity(leaving_units)
    spare_capacity = active_capacity - buyer.demand_capacity(price)

    auction_round = AuctionRound(
        round_number=round_number,
        price=price,
        active_capacity=active_capacity,
        exited_capacity=exited_capacity,
        spare_capacity=spare_capacity,
    )

    return remaining_units, auction_round, clearing_price


def select_units_to_keep(
    leaving_units,
    remaining_capacity,
    required_capacity,
):
    keep_units = []

    leaving_units_sorted = sorted(
        leaving_units,
        key=lambda unit: unit.min_acceptable_price,
    )

    for unit in leaving_units_sorted:
        if remaining_capacity + get_capacity(keep_units) >= required_capacity:
            logger.info("Capacity met")
            break
        keep_units.append(unit)

    return keep_units


def set_exit_price(active_units, remaining_units, price):
    for unit in active_units:
        if unit not in remaining_units:
            unit.exit_price = price
