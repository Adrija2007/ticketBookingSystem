import sqlite3
import uuid

class HallTicketSystemDB:
    def __init__(self, db_name="cinema_booking.db"):
        self.db_name = db_name
        self.init_database()

    def get_connection(self):
        """Returns a secure connection instance to the SQLite state backend."""
        return sqlite3.connect(self.db_name)

    def init_database(self):
        """Creates physical schemas and populates authorization defaults."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # 1. Access Security Table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT NOT NULL
                )
            ''')
            
            # 2. Transactional Seating Registry Matrix Table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS bookings (
                    ticket_id TEXT PRIMARY KEY,
                    screen_id INTEGER NOT NULL,
                    seat_label TEXT NOT NULL,
                    customer_name TEXT NOT NULL,
                    price INTEGER NOT NULL,
                    checked_in INTEGER DEFAULT 0,
                    UNIQUE(screen_id, seat_label)
                )
            ''')
            
            # Injects standard operational administrative profiling vectors if empty
            cursor.execute("SELECT COUNT(*) FROM users")
            if cursor.fetchone()[0] == 0:
                cursor.execute("INSERT INTO users VALUES (?, ?)", ("admin", "admin123"))
                conn.commit()

    def authenticate(self, username, password):
        """Validates credentials against user tables safely."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
            return cursor.fetchone() is not None

    def get_booked_seats(self, screen_id):
        """Fetches a clean string dictionary of booked seats using explicit index extraction."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT seat_label FROM bookings WHERE screen_id = ?", (screen_id,))
            return {row[0]: True for row in cursor.fetchall()}

    def display_seating_chart(self, screen_id):
        """Renders the visual layout mapping out seats in rows of 15."""
        booked_seats = self.get_booked_seats(screen_id)
        price_a, price_b = 300, 450
        
        border = "=" * 85
        print(f"\n{border}")
        print(f"                                SCREEN {screen_id} MAP                                ")
        print(border)
        print("                               STAGE / SCREEN                                ")
        print(border)
        
        def print_zone(prefix):
            row_str = ""
            for i in range(1, 51):
                seat_label = f"{prefix}{i}"
                if seat_label in booked_seats:
                    row_str += "[XX ] "
                else:
                    row_str += f"[{seat_label:<3}] "
                    
                if i % 15 == 0 or i == 50:
                    print(row_str)
                    row_str = ""

        print(f"\n--- ZONE A (Price: Rs. {price_a}) ---")
        print_zone('a')
            
        print("\n" + "░" * 85 + "\n" + "░" * 85)
        
        print(f"\n--- ZONE B (Price: Rs. {price_b}) ---")
        print_zone('b')
        
        print(f"\nLegend: [a1]/[b1] = Available  |  [XX] = Booked  |  A: Rs. {price_a}  |  B: Rs. {price_b}")
        print(border)

    def book_ticket(self, screen_id, seat_label, customer_name):
        """Books a single seat in an independent transaction."""
        cleaned_seat = seat_label.strip().lower()
        
        if not cleaned_seat:
            print("\n❌ Error: Seat choice cannot be empty.")
            return None

        # 1. Validate single-seat layout bounds
        try:
            zone = cleaned_seat[0]  # Extracts character ('a' or 'b')
            num = int(cleaned_seat[1:])  # Extracts numeric portion
            
            if zone not in ['a', 'b'] or num < 1 or num > 50:
                raise ValueError
                
            price = 300 if zone == 'a' else 450
        except:
            print(f"\n❌ Error: Seat format error. '{cleaned_seat.upper()}' does not exist (Use a1-a50 or b1-b50).")
            return None

        # 2. Check availability before writing to DB
        booked_seats = self.get_booked_seats(screen_id)
        if cleaned_seat in booked_seats:
            print(f"\n❌ Error: Booking failed. Seat '{cleaned_seat.upper()}' is already taken!")
            return None

        unique_id = str(uuid.uuid4())[:8].upper()

        # 3. Direct single-row insertion
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """INSERT INTO bookings 
                       (ticket_id, screen_id, seat_label, customer_name, price) 
                       VALUES (?, ?, ?, ?, ?)""",
                    (unique_id, screen_id, cleaned_seat, customer_name, price)
                )
                conn.commit()
                
            print(f"\n🎉 Success! Seat {cleaned_seat.upper()} reserved in Screen {screen_id} for {customer_name}.")
            print("-" * 50)
            print(f"🎫 Gate Entry Pass Key ID   : {unique_id}")
            print(f"💵 Total Billing Amount    : Rs. {price}")
            print("-" * 50)
            return unique_id
            
        except sqlite3.IntegrityError:
            print(f"\n❌ Error: Database unique constraint conflict. This seat was just taken!")
            return None

    def gate_entry(self, unique_id):
        """Validates entry code vectors and outputs total receipt auditing flags."""
        unique_id = unique_id.upper().strip()
        
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT screen_id, seat_label, customer_name, checked_in, price FROM bookings WHERE ticket_id = ?", (unique_id,))
            record = cursor.fetchone()
            
            if not record:
                print("\n🛑 Gate Entry Denied: Ticket verification token mismatch.")
                return False
                
            screen_id, seat_label, customer_name, checked_in, price = record
            
            if checked_in == 1:
                print(f"\n🛑 Gate Entry Denied: Ticket '{unique_id}' was already checked in at security gates!")
                return False
                
            cursor.execute("UPDATE bookings SET checked_in = 1 WHERE ticket_id = ?", (unique_id,))
            conn.commit()
            
            print(f"\n🎫 Access Granted! Welcome to Screen {screen_id}, {customer_name}!")
            print(f"📍 Assigned Seat     : {seat_label.upper()}")
            print(f"💵 Verified Payment : Rs. {price}")
            return True
