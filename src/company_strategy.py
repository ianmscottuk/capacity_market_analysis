def get_remaining_units(companies, active_units, price):
    leaving_units = []
    remaining_units = []

    for unit in active_units:
        if unit.should_exit(price):
            leaving_units.append(unit)
        else:
            remaining_units.append(unit)

    return remaining_units, leaving_units
