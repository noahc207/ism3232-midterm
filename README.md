# ISM3232 Midterm: [the business name]

- **Name:** Noah Chavez
- **Version:** Alpha
- **Date:** 10/25/26

## What This Program Does
This program calculates the cost of renting tools from the company Ridgeline Tool Rental. It applies the company's discount, damage waiver, deposit, and inspection rules to a list of eight rentals, and then prints a report showing each customer's quote and a summary.
## Business Rules
- The rental cost is the daily rate times the number of days.
- Rentals of fewer than 3 days get no discount, 3 through 6 days get 10%, and 7 days or more gets 20%.
- Licensed contractors always get at least a 10% discount, even on rentals of fewer than 3 days.
- A $25 damage waiver is added when the discounted cost is below $150.
- A quote of $1,000 or more requires a deposit.
- A rental needs a pickup inspection when it runs 5 days or more and its quote is over $800.
## How to Run
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
## How to Test
ruff check .
ruff format .
pytest -v

I wrote 25 tests in tests/test_business_rules.py 
## Files in This Repository
- business_rules.py: The eight functions that apply the rental rules.
- main.py: The rental list and the code that prints the report.
- commands.md: the terminal record of how the project was built and checked.
- README.md: explains how to run and test the project.
- requirements.txt: the Python packages the project needs, made with pip freeze.
- .gitignore: keeps .venv/ and __pycache__/ out of the repository.
- tests/__init__.py: an empty file that makes tests a Python package.
- tests/test_business_rules.py: the pytest tests for the business rules.

## AI Use Statement
I did not use AI on this exam