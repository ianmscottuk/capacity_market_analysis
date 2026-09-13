from src.company_strategy import get_remaining_units
from src.logger import get_logger
from src.schemas import AuctionRound
from src.utils import calc_clearing_price, capacity_met, get_capacity

logger = get_logger(__name__)


def run_auction(buyer, companies, price_step=-5):

    units = [unit for company in companies for unit in company.units]

    price = buyer.price_cap + price_step
    active_units = units.copy()
    round_number = 1
    rounds = []

    logger.info("Auction Started")

    while price > 0:
        active_units, auction_round = run_round(
            round_number=round_number,
            price=price,
            buyer=buyer,
            companies=companies,
            active_units=active_units,
        )

        rounds.append(auction_round)

        price += price_step
        round_number += 1


def run_round(round_number, price, buyer, companies, active_units):
    logger.info(
        "Round %s | price=%s | active_units=%s",
        round_number,
        price,
        len(active_units),
    )
    remaining_units, leaving_units = get_remaining_units(
        companies=companies, active_units=active_units, price=price
    )

    if leaving_units:
        logger.info("Someone wants to exit....")

        if not capacity_met(buyer.demand_capacity(price), remaining_units):
            logger.info("insufficient capacity")
            calc_clearing_price()  # calc profit of each company

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

    return remaining_units, auction_round
