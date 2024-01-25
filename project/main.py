from hall import Hall
from counter import Counter


# Function to display the menu and get user choice
def display_menu():
    print("\nTicket Booking System Menu:")
    print("1. View all shows today")
    print("2. View available seats")
    print("3. Book a ticket")
    print("4. Exit")
    return input("Enter your choice: ")


# display a matrix of available seats
def display_seat_matrix(seats_matrix):
    for row in seats_matrix:
        for seat in row:
            if seat == 0:
                print("0", end=" ")
            else:
                print("1", end=" ")
        print()


# display the seat matrix
def display_available_seats(counter, hall_no, show_id):
    hall_found = False
    for hall in counter._hall_list:
        if hall._hall_no == hall_no:
            hall_found = True
            seats_matrix = hall._seats.get(hall_no)
            if seats_matrix is not None:
                print("\nSeat Display:\n")
                display_seat_matrix(seats_matrix)
                return

    if not hall_found:
        print(f"Hall with number {hall_no} not found.")
    else:
        print(f"Show with ID {show_id} not found for Hall {hall_no}.")


# Create halls and add them to the counter
hall1 = Hall(rows=5, cols=5, hall_no=1)
hall2 = Hall(rows=6, cols=6, hall_no=2)
counter = Counter()
counter.add_hall(hall1)
counter.add_hall(hall2)

# Add two shows initially
hall1.entry_show(11, "Jailer", "2:00 PM")
hall2.entry_show(22, "Top Gun", "4:30 PM")


while True:
    choice = display_menu()

    if choice == "1":
        counter.view_all_shows()

    elif choice == "2":
        hall_no = input("Enter the hall number: ")
        show_id = input("Enter the show ID: ")

        try:
            hall_no = int(hall_no)
            show_id = int(show_id)

            # Check if the provided hall number exists
            if any(hall._hall_no == hall_no for hall in counter._hall_list):
                # Check if the provided show ID exists for the given hall
                if any(
                    hall._hall_no == hall_no
                    and any(show[0] == show_id for show in hall._show_list)
                    for hall in counter._hall_list
                ):
                    display_available_seats(counter, hall_no, show_id)
                else:
                    print(f"Show with ID {show_id} not found for Hall {hall_no}.")
            else:
                print("Hall not found.")

        except ValueError:
            print("Invalid input!!!! Please enter valid hall number and show ID.")

    elif choice == "3":
        hall_no = input("Enter the hall number: ")
        show_id = input("Enter the show ID: ")

        try:
            hall_no = int(hall_no)
            show_id = int(show_id)

            # Check if the provided hall number and show ID exist
            if any(
                hall._hall_no == hall_no
                and (show[0] == show_id for show in hall._show_list)
                for hall in counter._hall_list
            ):
                seat_list = []
                while True:
                    # for the multiple seat booking
                    seat_input = input(
                        "Enter a seat (row, col) or type 'done' to finish: "
                    )
                    if seat_input.lower() == "done":
                        break
                    try:
                        row, col = map(int, seat_input.split(","))

                        # Adjust the user input to 0-based indexing for internal representation
                        row -= 1
                        col -= 1

                        # Check if the provided seat is within the valid range
                        if not (0 <= row < hall1._rows and 0 <= col < hall1._cols):
                            print("Invalid seat. Please enter a valid seat.")
                            continue

                        if hall1._seats[hall_no][row][col] == 1:
                            print(
                                "Sorry!! This seat is already booked. Please choose another seat."
                            )
                        else:
                            seat_list.append((row, col))
                    except ValueError:
                        print("Invalid input. Please enter seat as 'row, col'.")
                counter.book_tickets(hall_no, show_id, seat_list)
            else:
                print(f"Show with ID {show_id} not found for Hall {hall_no}.")

        except ValueError:
            print("Invalid input. Please enter valid hall number and show ID.")

    elif choice == "4":
        print("Thank you. Good Bye !!!")
        break
    else:
        print("Invalid choice. Please try again.")
