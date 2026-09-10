from logger import get_logger
from scenarios import baseline_scenario
from schemas import AuctionRound
from utils import capacity_met, get_capacity

logger = get_logger(__name__)


def run_auction(buyer, companies, price_step=-5):

    units = [unit for company in companies for unit in company.units]

    price = buyer.price_cap + price_step
    active_units = units.copy()
    round_number = 1
    rounds = []

    logger.info("Auction Started")

    while price > 0:
        logger.info(
            "Round %s | price=%s | active_units=%s",
            round_number,
            price,
            len(active_units),
        )

        remaining_units = [unit for unit in active_units if not unit.should_exit(price)]

        if len(remaining_units) < len(active_units):
            logger.info("Someone wants to exit....")

            if not capacity_met(
                buyer.demand_capacity(price), remaining_units
            ):  # these need to be the REMAING units
                logger.info("insufficient capacity")


        rounds.append(
            AuctionRound(
                round_number=round_number,
                price=price,
                active_capacity_mw=active_capacity,
                exited_capacity_mw=exited_capacity,
                spare_capacity_mw=spare_capacity,
            )
        )

        price += price_step
        round_number += 1


if __name__ == "__main__":
    buyer, companies = baseline_scenario()

    run_auction(buyer, companies)
