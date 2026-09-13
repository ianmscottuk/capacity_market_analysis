from src.auction import run_auction
from src.logger import get_logger
from src.scenarios import baseline_scenario

logger = get_logger(__name__)


if __name__ == "__main__":
    buyer, companies = baseline_scenario()

    run_auction(buyer, companies)
