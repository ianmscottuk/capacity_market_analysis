from src.auction import run_round


def test_run_round_no_units_leave(buyer, units):
    remaining_units, auction_round = run_round(
        round_number=1,
        price=buyer.price_cap,
        buyer=buyer,
        companies=[],
        active_units=units,
    )

    assert remaining_units == units
    assert auction_round.round_number == 1
    assert auction_round.price == buyer.price_cap
