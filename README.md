# Vansh Bank - Bank Management System

A menu-driven banking simulation built with Python. Customers can create accounts, manage a simulated balance, transfer money to other registered customers, and view transaction history. A separate manager menu provides an overview of customers and bank balances.

This is a beginner learning project, not software for real banking or real money.

## Features

### Customer menu
- Sign up and log in with a username and password
- Choose a Saving or Current account
- View profile details and account balance
- Deposit and withdraw simulated money
- Transfer simulated money to another registered customer
- View transaction history
- Log out

### Manager menu
- Register and log in as a manager
- View all customers or search by username
- Delete a customer account
- View the total balance across customer accounts
- View customer transaction histories

### Input checks
- 10-digit phone number validation
- Duplicate username checks within customer and manager accounts
- Password confirmation during sign-up
- Positive amount and sufficient-balance checks
- Checks for missing transfer recipients and self-transfers

## Tech used

- Python 3
- Lists and dictionaries for in-memory records
- Loops and conditional statements for menu flow
- Standard console input and output

No third-party packages are required.

## How to run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder and run:

```bash
python 2-bank-management-system.py
```

On systems that use `python3`, run:

```bash
python3 2-bank-management-system.py
```

Create a customer account before logging in. To try a transfer, create two customer accounts in the same session, deposit a simulated amount into one, and transfer it to the other customer's username. Managers must register before logging in through the manager menu.

## Current limitations

- All records exist only in memory and are lost when the program closes.
- Passwords are stored as plain text in memory, and password input is visible in the terminal. Use only made-up demo details.
- Anyone can register as a manager; there is no restricted administrator approval.
- Non-numeric menu or amount inputs can stop the program.
- Amounts use floating-point numbers rather than a precise money representation.
- This is a CLI simulation with no database, real payment processing, or bank integration.

## Possible next steps

- Add file or database storage
- Handle invalid numeric inputs without exiting
- Add secure password handling and restricted manager access
- Use decimal arithmetic for amounts
- Add account IDs and structured transaction records
- Split the program into functions and add tests

## Learning focus

The project practices Python control flow, nested menus, lists, dictionaries, input validation, record lookup, and updates across customer accounts.
