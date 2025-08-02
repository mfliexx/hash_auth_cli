# HASH AUTHENTIFICATION

A simple command-line Python application for user registration and login with password hashing. User data is stored in a `users.json` file using SHA-256 encryption

## Features
- Register new users
- User login system
- Check if user exists
- SHA-256 password hashing
- Store user data in a JSON file
- Colored console interface with ASCII banners

## Built With
- `hashlib` – for password hashing
- `json` – for saving user data
- `pyfiglet` – to display ASCII banners
- `colorama` – for colored terminal output

## How to Use
1. Install the required packages (if not installed):
   pip install pyfiglet colorama
2. Run the script:
   python autentification_sim.py
3. Choose one of the options: register, log in, or exit
