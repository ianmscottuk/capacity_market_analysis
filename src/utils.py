from logger import get_logger
from schemas import CapacityMarketUnit


logger = get_logger(__name__)


def get_capacity(units):
    return sum(unit.capacity_mw for unit in units)


def log_exiting_units(exiting_units: list[tuple[CapacityMarketUnit, float]]) -> None:

    for unit, exit_bid in exiting_units:
        logger.info(
            "%s (%s) is exiting the auction at £%.2f/kW/year",
            unit.name,
            unit.cmu_id,
            exit_bid,
        )
