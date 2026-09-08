from logger import get_logger
from scenarios import baseline_scenario
from schemas import AuctionRound
from utils import get_capacity, log_exiting_units

logger = get_logger(__name__)


def run_auction(buyer, og_units, price_step=-5):

    price = buyer.price_cap_per_kw_year + price_step
    active_units = og_units.copy()
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

        if any([unit.exit_at_price(price) for unit in active_units]):
            logger.info("Someone wants to exit....")
            else:
                log_exiting_units(exiting_units_sorted)
                active_units = remaining_units

        spare_capacity = buyer.spare_capacity(active_capacity)

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
    buyer, units = baseline_scenario()

    run_auction(buyer, units)
