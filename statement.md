*PROJECT NAME: Cinema Ticket Booking System*

*1. Problem Statement*
Normally in cinema halls, we have to go and ask for tickets. We don't know which seats are empty. Sometimes we get confused about seat numbers and at the gate staff also face problem to check tickets one by one manually. So it becomes very time consuming.

So we thought of making a small system to manage this. Our project is a Python based command line system. Here user can login first, then he can see all seats, book any free seat, and he will get a ticket ID. At the gate that ID can be checked. That's the main idea.

*2. Scope*
What our system can do is:

- Login for user with username and password
- Show seats of different screens, like which are booked and which are free
- Before booking it will check if seat is available or not
- While booking it will ask customer name and it will give price as per seat type, like front seats are cheaper
- After booking it will create one unique ticket ID
- That ticket ID can be used for verification at entry
- All data like users, seats, tickets will be saved in SQLite database
- Everything will run in command prompt, so no need for extra software

For now we are making it simple in CLI only, later we can make it as website or app.

*3. Who will use it*
- Normal customers who want to book tickets
- Staff who check tickets at gate
- Manager who wants to see booking records
- And for us students, we can learn how Python and database actually works in real project

*4. Features*

*Login System*
User has to give correct username and password to enter. Without login no one can book.

*Seat Display*
When user selects a screen number, it shows the full seating. We used O for free seats and X for booked seats so anyone can easily understand.

*Booking*
User just has to give screen no and seat no. If seat is free then system will ask his name and show the price and finally give a Ticket ID like TKT-1234 something.

*Verification*
At gate staff just needs to put that Ticket ID. System will tell if ticket is okay or wrong or already used.

*Database*
We used sqlite3 because its simple and comes with Python. First time when we run the code it will create the database automatically.

*Error Handling*
We also added some error checking. Like if user gives wrong screen number or seat number which is not there, or tries to book already booked seat, or types wrong password, it will show proper message.

*5. Technology We Used*
We used Python 3 for coding. For database we used SQLite. Interface is CLI (black window). And we used 3 modules - sqlite3 for database, uuid for generating ticket ID and sys for basic things.

*6. What will be the final output*
At the end our project will work as a small cinema booking counter. We can see seats, book seats, generate ticket and verify it. All data will be saved. It is not a big commercial app but it covers all the basic needs of a booking system and we can show how it works.
