from hall import Hall


class Counter:
    def __init__(self):
        self._hall_list = []

    def add_hall(self, hall):
        self._hall_list.append(hall)

    def view_all_shows(self):
        for hall in self._hall_list:
            hall._view_show_list()

    def view_available_seats(self, hall_no, show_id):
        for hall in self._hall_list:
            if hall._hall_no == hall_no:
                hall._view_available_seats(show_id)

    def book_tickets(self, hall_no, show_id, seat_list):
        for hall in self._hall_list:
            if hall._hall_no == hall_no:
                hall._book_seats(show_id, seat_list)
