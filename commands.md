# Terminal record: Ridgeline Tool Rental

## 1. Building the project
# Terminal Record: Ridgeline Tool Rental
mkdir ism3232-midterm
cd ism3232-midterm
python3 -m venv .venv
source .venv/bin/activate
mkdir tests
touch business_rules.py main.py commands.md README.md requirements.txt .gitignore
touch tests/__init__.py tests/test_business_rules.py
printf ".venv/\n__pycache__/\n" > .gitignore
python -m pip freeze > requirements.txt
git init
git branch -M main
git add .
git commit -m "Midterm setup"
git remote add origin https://github.com/noahc207/ism3232-midterm.git
git push -u origin main
brew install gh
gh auth login
git push -u origin main
pip install ruff pytest

## 2 The virtual environment 
The response starts with (.venv) and the path /Users/noah/ism3232-midterm/.venv/bin/python3 goes through the .venv folder

## 3 The project structure
The pycache folder is on my computer but isn't present in the github repository because gitignore excludes it since python generates it automatically.

## 4 Every function and test

business_rules.py defines 8 functions, and tests/test_business_rules.py defines 25 tests (26 def lines, one of which is the make_rental helper and not a test)

business_rules.py
14:def calculate_rental_cost(daily_rate: float, days: int) -> float:
19:def get_rental_discount(days: int, contractor: bool = False) -> float:
32:def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
42:def requires_deposit(quote: float) -> bool:
47:def needs_inspection(days: int, quote: float) -> bool:
52:def total_quoted(rentals: list) -> float:
62:def largest_rental(rentals: list) -> str:
76:def format_rental_line(

tests/test_business_rules.py
15:def make_rental(customer, daily_rate, days, contractor=False):
26:def test_rental_cost_is_rate_times_days():
31:def test_no_discount_at_two_days():
35:def test_ten_percent_discount_at_three_days():
39:def test_ten_percent_discount_at_six_days():
43:def test_twenty_percent_discount_at_seven_days():
48:def test_contractor_gets_ten_percent_at_two_days():
52:def test_contractor_keeps_twenty_percent_at_seven_days():
56:def test_contractor_flag_changes_the_quote():
64:def test_waiver_added_just_below_150():
68:def test_no_waiver_at_exactly_150():
72:def test_waiver_uses_discounted_cost_not_original_cost():
77:def test_quote_with_discount_and_no_waiver():
82:def test_deposit_required_at_exactly_1000():
86:def test_no_deposit_just_below_1000():
91:def test_inspection_at_exactly_five_days():
95:def test_no_inspection_at_four_days():
99:def test_inspection_when_quote_just_over_800():
103:def test_no_inspection_when_quote_exactly_800():
108:def test_total_quoted_adds_every_quote():
113:def test_total_quoted_empty_list_is_zero():
118:def test_largest_rental_returns_biggest_quote_customer():
123:def test_largest_rental_tie_returns_first_in_list():
128:def test_largest_rental_empty_list_returns_empty_string():
133:def test_format_line_shows_no_for_false_values():
138:def test_format_line_shows_yes_for_true_values():
(.venv) noah@Noahs-MacBook-Air-5 ism3232-midterm % 

## 5 Which files print
main.py is the Python file that prints. Business_rules.py is not in the list because its functions only return values and main.py does all the printing.

## 6 The commit history
There have been 4 commits at this point.

8fcf1be (HEAD -> main, origin/main) Add pytest tests for business rules
0597c08 Created main report script
d0c6231 Added 8 business rules functions
99bc87a Midterm setup

