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


def test_run_round_all_units_leave(buyer, units):
    remaining_units, auction_round = run_round(
        round_number=5,
        price=10,
        buyer=buyer,
        companies=[],
        active_units=units,
    )

    assert len(remaining_units) == 0
    assert auction_round.round_number == 5
    assert auction_round.price == 10
