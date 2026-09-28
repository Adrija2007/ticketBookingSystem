import sys
from hall_ticket_system import HallTicketSystemDB

def main():
    db_system = HallTicketSystemDB()
    
    print("="*40)
    print("🔒 SYSTEM ACCESS SECURITY WALL 🔒")
    print("="*40)
    print("Hint: Default username is 'admin' and password is 'admin123'")
    
    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()
    
    if not db_system.authenticate(username, password):
        print("\n❌ Login Failed: Unauthorized Credentials. Shutting downstream workflows.")
        sys.exit()
        
    print("\n✅ Authentication Successful. Booting Seating Orchestrator Terminal Engine...")
    
    while True:
        print("\n" + "═"*40)
        print("🎬 REINFORCED SQL MOVIE SEATING PLATFORM 🎬")
        print("═"*40)
        print("1. View Seating Chart (Live Screen Map)")
        print("2. Book a Ticket")
        print("3. Gate Entry Check-In (Verify Pass)")
        print("4. Exit System")
        print("═"*40)
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            try:
                screen_input = input("Enter Screen identifier (1-5): ").strip()
                if not screen_input.isdigit():
                    print("❌ Error: Screen target must be a valid number between 1 and 5.")
                    continue
                screen = int(screen_input)
                if 1 <= screen <= 5:
                    db_system.display_seating_chart(screen)
                else:
                    print("❌ Error: Screen indicator boundary constraint exception (1-5 only).")
            except Exception as e:
                print(f"❌ Error: Value cannot be cast correctly. Details: {e}")
            
        elif choice == '2':
            try:
                screen_input = input("Select Screen Target (1-5): ").strip()
                if not screen_input.isdigit():
                    print("❌ Error: Screen target must be a single number (1 to 5).")
                    continue
                    
                screen = int(screen_input)
                if not (1 <= screen <= 5):
                    print("❌ Error: Targeted index falls outside screen capacities (1-5).")
                    continue
                
                seat_input = input("Enter Preferred Seat Label (e.g., a3, b20): ")
                name = input("Enter Customer Name: ").strip()
                
                if not name:
                    print("❌ Error: Customer name entry missing.")
                    continue
                    
                db_system.book_ticket(screen, seat_input, name)
            except Exception as e:
                print(f"❌ Error: System processing constraint initialization abort. Details: {e}")
            
        elif choice == '3':
            ticket_id = input("Scan / Enter Unique Gate Entry ID: ")
            db_system.gate_entry(ticket_id)
            
        elif choice == '4':
            print("\n👋 Deconstructing connection handlers. Database state written successfully. Goodbye!")
            break
        else:
            print("\n❌ Command vector syntax match failure. Provide options from 1 to 4.")

if __name__ == "__main__":
    main()
