"""Tests for Ridgeline Tool Rental business rules."""

from business_rules import (
    calculate_quote,
    calculate_rental_cost,
    format_rental_line,
    get_rental_discount,
    largest_rental,
    needs_inspection,
    requires_deposit,
    total_quoted,
)


def make_rental(customer, daily_rate, days, contractor=False):
    """Build one rental dict for a test."""
    return {
        "customer": customer,
        "daily_rate": daily_rate,
        "days": days,
        "contractor": contractor,
    }


# Rule 1: rental cost
def test_rental_cost_is_rate_times_days():
    assert round(calculate_rental_cost(60.0, 2), 2) == 120.00


# Rule 2: discount tiers (3 days and 7 days)
def test_no_discount_at_two_days():
    assert get_rental_discount(2) == 0.0


def test_ten_percent_discount_at_three_days():
    assert get_rental_discount(3) == 0.10


def test_ten_percent_discount_at_six_days():
    assert get_rental_discount(6) == 0.10


def test_twenty_percent_discount_at_seven_days():
    assert get_rental_discount(7) == 0.20


# Rule 3: contractor discount
def test_contractor_gets_ten_percent_at_two_days():
    assert get_rental_discount(2, contractor=True) == 0.10


def test_contractor_keeps_twenty_percent_at_seven_days():
    assert get_rental_discount(7, contractor=True) == 0.20


def test_contractor_flag_changes_the_quote():
    regular = calculate_quote(60.0, 2, contractor=False)
    contractor = calculate_quote(60.0, 2, contractor=True)
    assert round(regular, 2) == 145.00
    assert round(contractor, 2) == 133.00


# Rule 4: damage waiver (discounted cost below $150)
def test_waiver_added_just_below_150():
    assert round(calculate_quote(74.99, 2), 2) == 174.98


def test_no_waiver_at_exactly_150():
    assert round(calculate_quote(75.0, 2), 2) == 150.00


def test_waiver_uses_discounted_cost_not_original_cost():
    # original cost is 150, but the discounted cost is 135
    assert round(calculate_quote(50.0, 3), 2) == 160.00


def test_quote_with_discount_and_no_waiver():
    assert round(calculate_quote(200.0, 3), 2) == 540.00


# Rule 5: deposit (quote of $1,000 or more)
def test_deposit_required_at_exactly_1000():
    assert requires_deposit(1000.00) is True


def test_no_deposit_just_below_1000():
    assert requires_deposit(999.99) is False


# Rule 6: inspection (5 days or more AND quote over $800)
def test_inspection_at_exactly_five_days():
    assert needs_inspection(5, 900.00) is True


def test_no_inspection_at_four_days():
    assert needs_inspection(4, 900.00) is False


def test_inspection_when_quote_just_over_800():
    assert needs_inspection(5, 800.01) is True


def test_no_inspection_when_quote_exactly_800():
    assert needs_inspection(5, 800.00) is False


# total_quoted
def test_total_quoted_adds_every_quote():
    rentals = [make_rental("Alvarez", 60.0, 2), make_rental("Brennan", 60.0, 2, True)]
    assert round(total_quoted(rentals), 2) == 278.00


def test_total_quoted_empty_list_is_zero():
    assert round(total_quoted([]), 2) == 0.00


# largest_rental
def test_largest_rental_returns_biggest_quote_customer():
    rentals = [make_rental("Alvarez", 60.0, 2), make_rental("Brennan", 60.0, 2, True)]
    assert largest_rental(rentals) == "Alvarez"


def test_largest_rental_tie_returns_first_in_list():
    rentals = [make_rental("Alvarez", 60.0, 2), make_rental("Brennan", 60.0, 2)]
    assert largest_rental(rentals) == "Alvarez"


def test_largest_rental_empty_list_returns_empty_string():
    assert largest_rental([]) == ""


# format_rental_line
def test_format_line_shows_no_for_false_values():
    line = format_rental_line("Alvarez", 145.0, False, False)
    assert line == "Alvarez: $145.00 | deposit: no | inspection: no"


def test_format_line_shows_yes_for_true_values():
    line = format_rental_line("Eastman", 1344.0, True, True)
    assert line == "Eastman: $1344.00 | deposit: yes | inspection: yes"
