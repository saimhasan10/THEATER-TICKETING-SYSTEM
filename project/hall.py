class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no

        # method to set up the seating arrangement.
        self._initialize_seats()

    def _initialize_seats(self):
        # Create a 2D list to represent seats, initially all free (0)
        seats_matrix = []
        for _ in range(self._rows):
            row = [0] * self._cols
            seats_matrix.append(row)

        # Assign the seats matrix to the dictionary with 'id' as the key
        self._seats[self._hall_no] = seats_matrix

    def entry_show(self, id, movie_name, time):
        # Create a tuple with the provided information
        show_info = (id, movie_name, time)

        # Append the tuple to the show_list
        self._show_list.append(show_info)

    # Booking seats
    def _book_seats(self, show_id, seat_list):
        seats_matrix = self._seats.get(self._hall_no)

        if seats_matrix is None:
            print("Hall not found.")
            return

        show_found = False
        for show in self._show_list:
            if show[0] == show_id:
                show_found = True
                break

        if show_found:
            for row, col in seat_list:
                if 0 <= row < self._rows and 0 <= col < self._cols:
                    if seats_matrix[row][col] == 0:
                        # Book the seat
                        seats_matrix[row][col] = 1
                    else:
                        print(f"Seat ({row}, {col}) is already booked.")
                else:
                    print(f"Seat ({row}, {col}) is invalid for this hall.")
        else:
            print(f"Show with ID {show_id} not found.")

    # view show list
    def _view_show_list(self):
        if self._show_list:
            for show in self._show_list:
                show_id, movie_name, time = show
                print(
                    f"Hall: {self._hall_no}, Show ID: {show_id}, Movie: {movie_name}, Time: {time}"
                )
        else:
            print(f"No shows are currently running in Hall {self._hall_no}.")

    def _view_available_seats(self, show_id):
        seats_matrix = self._seats.get(self._hall_no)

        if seats_matrix is None:
            print("Hall not found.")
            return

        show_found = False
        for show in self._show_list:
            if show[0] == show_id:
                show_found = True
                break

        if show_found:
            print(f"Available seats for Show ID {show_id}:")
            for row in range(self._rows):
                for col in range(self._cols):
                    if seats_matrix[row][col] == 0:
                        print(f"Row {row + 1}, Col {col + 1}")
        else:
            print(f"Show with ID {show_id} not found.")
