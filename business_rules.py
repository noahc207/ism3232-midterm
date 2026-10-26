NO_DISCOUNT = 0.0
MEDIUM_DISCOUNT = 0.10
LONG_DISCOUNT = 0.20
MEDIUM_DISCOUNT_DAYS = 3
LONG_DISCOUNT_DAYS = 7
CONTRACTOR_MIN_DISCOUNT = 0.10
WAIVER_FEE = 25.0
WAIVER_THRESHOLD = 150.0
DEPOSIT_THRESHOLD = 1000.0
INSPECTION_MIN_DAYS = 5
INSPECTION_QUOTE_THRESHOLD = 800.0


def calculate_rental_cost(daily_rate: float, days: int) -> float:
    """Return the rental cost before any discount."""
    return daily_rate * days

def get_rental_discount(days: int, contractor: bool = False) -> float:
    """Return the discount rate as a decimal."""
    if days >= LONG_DISCOUNT_DAYS:
        discount = LONG_DISCOUNT
    elif days >= MEDIUM_DISCOUNT_DAYS:
        discount = MEDIUM_DISCOUNT
    else:
        discount = NO_DISCOUNT
    if contractor and discount < CONTRACTOR_MIN_DISCOUNT:
        discount = CONTRACTOR_MIN_DISCOUNT
    return discount

def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
    """Return the quote: discounted cost plus the waiver when it applies."""
    cost = calculate_rental_cost(daily_rate, days)
    discount = get_rental_discount(days, contractor)
    discounted = cost * (1 - discount)
    if discounted < WAIVER_THRESHOLD:
        discounted += WAIVER_FEE
    return round(discounted, 2)

def requires_deposit(quote: float) -> bool:
    """Return True when the quote requires a deposit."""
    return quote >= DEPOSIT_THRESHOLD

def needs_inspection(days: int, quote: float) -> bool:
    """Return True when the rental needs a pickup inspection."""
    return days >= INSPECTION_MIN_DAYS and quote > INSPECTION_QUOTE_THRESHOLD

def total_quoted(rentals: list) -> float:
    """Return the sum of the quotes for every rental."""
    total = 0.0
    for rental in rentals:
        total += calculate_quote(
            rental["daily_rate"], rental["days"], rental["contractor"]
        )
    return total

def largest_rental(rentals: list) -> str:
    """Return the customer with the largest quote, or "" if empty."""
    best_customer = ""
    best_quote = 0.0
    for rental in rentals:
        quote = calculate_quote(
            rental["daily_rate"], rental["days"], rental["contractor"]
        )
        if best_customer == "" or quote > best_quote:
            best_customer = rental["customer"]
            best_quote = quote
    return best_customer

def format_rental_line(
    customer: str, quote: float, deposit: bool, inspection: bool
) -> str:
    """Return one report line for a rental."""
    deposit_text = "yes" if deposit else "no"
    inspection_text = "yes" if inspection else "no"
    return (
        f"{customer}: ${quote:.2f} | deposit: {deposit_text} "
        f"| inspection: {inspection_text}"
    )