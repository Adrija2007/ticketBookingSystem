# Cinema Ticket Booking System

A command-line Cinema seat booking system in Python with an SQLite database.

## Features
- You can login with username and password
- After that view live seating chart for 5 screens
- Now book a seat (Zone A: Rs. 300, Zone B: Rs. 450)
- Then gate entry check-in using a unique ticket ID

## Requirements
- Python 3.x
- No external libraries needed (sqlite3 and uuid come with Python)

## Setup
1. Install Python 3 from https://www.python.org/downloads/
2. Now download both files into the same folder:
   - ticket_booking.py
   - hall_ticket_system.py
3. Then open a terminal in that folder.

## Configuration
None needed. The database file (cinema_booking.db) is created automatically on first run.

## How to Run
python ticket_booking.py

## Login
- Username: admin
- Password: admin123

## Usage
1. For view Seating Chart: enter screen number (1-5)
2. Now book a Ticket: enter screen, seat (e.g. a3, b20), customer name. Now a Ticket ID is shown
3. Gate Entry Check-In: enter the Ticket ID
4. Exit System
