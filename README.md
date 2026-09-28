# Cinema Ticket Booking System

A command-line cinema seat booking system in Python with an SQLite database.

## Features
- Login with username and password
- View live seating chart for 5 screens
- Book a seat (Zone A: Rs. 300, Zone B: Rs. 450)
- Gate entry check-in using a unique ticket ID

## Requirements
- Python 3.x
- No external libraries needed (sqlite3 and uuid come with Python)

## Setup
1. Install Python 3 from https://www.python.org/downloads/
2. Download both files into the same folder:
   - ticket_booking.py
   - hall_ticket_system.py
3. Open a terminal in that folder.

## Configuration
None needed. The database file (cinema_booking.db) is created automatically on first run.

## How to Run
python ticket_booking.py

## Login
- Username: admin
- Password: admin123

## Usage
1. View Seating Chart: enter screen number (1-5)
2. Book a Ticket: enter screen, seat (e.g. a3, b20), customer name. A Ticket ID is shown
3. Gate Entry Check-In: enter the Ticket ID
4. Exit System
