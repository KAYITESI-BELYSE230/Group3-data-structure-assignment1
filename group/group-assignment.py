from collections import deque

movies = [
    {"MovieID": 201, "MovieName": "Inception", "Showtime": "7:00 PM", "SeatsAvailable": 20},
    {"MovieID": 202, "MovieName": "Avatar", "Showtime": "5:00 PM", "SeatsAvailable": 15},
    {"MovieID": 203, "MovieName": "Titanic", "Showtime": "6:00 PM", "SeatsAvailable": 18},
    {"MovieID": 204, "MovieName": "The Dark Knight", "Showtime": "8:00 PM", "SeatsAvailable": 22},
    {"MovieID": 205, "MovieName": "The Godfather", "Showtime": "9:00 PM", "SeatsAvailable": 10},
    {"MovieID": 206, "MovieName": "Pulp Fiction", "Showtime": "7:30 PM", "SeatsAvailable": 16},
    {"MovieID": 207, "MovieName": "The Shawshank Redemption", "Showtime": "4:00 PM", "SeatsAvailable": 25},
    {"MovieID": 208, "MovieName": "Forrest Gump", "Showtime": "3:00 PM", "SeatsAvailable": 12},
    {"MovieID": 209, "MovieName": "Gladiator", "Showtime": "5:15 PM", "SeatsAvailable": 14},
    {"MovieID": 210, "MovieName": "The Matrix", "Showtime": "8:45 PM", "SeatsAvailable": 8},
    {"MovieID": 211, "MovieName": "Interstellar", "Showtime": "9:30 PM", "SeatsAvailable": 20},
    {"MovieID": 212, "MovieName": "The Lord of the Rings: The Return of the King", "Showtime": "10:00 PM", "SeatsAvailable": 6},
    {"MovieID": 213, "MovieName": "The Lion King", "Showtime": "2:00 PM", "SeatsAvailable": 30},
    {"MovieID": 214, "MovieName": "Jurassic Park", "Showtime": "12:00 PM", "SeatsAvailable": 15},
    {"MovieID": 215, "MovieName": "Finding Nemo", "Showtime": "1:00 PM", "SeatsAvailable": 22},
    {"MovieID": 216, "MovieName": "Star Wars: A New Hope", "Showtime": "4:30 PM", "SeatsAvailable": 18},
    {"MovieID": 217, "MovieName": "Frozen", "Showtime": "11:00 AM", "SeatsAvailable": 25},
    {"MovieID": 218, "MovieName": "The Avengers", "Showtime": "6:30 PM", "SeatsAvailable": 10},
    {"MovieID": 219, "MovieName": "Harry Potter and the Sorcerer's Stone", "Showtime": "5:45 PM", "SeatsAvailable": 12},
    {"MovieID": 220, "MovieName": "Spider-Man: No Way Home", "Showtime": "8:15 PM", "SeatsAvailable": 17},
    {"MovieID": 221, "MovieName": "Black Panther", "Showtime": "7:15 PM", "SeatsAvailable": 5},
    {"MovieID": 222, "MovieName": "Deadpool", "Showtime": "9:00 PM", "SeatsAvailable": 9},
    {"MovieID": 223, "MovieName": "Coco", "Showtime": "3:30 PM", "SeatsAvailable": 14},
    {"MovieID": 224, "MovieName": "Inside Out", "Showtime": "1:45 PM", "SeatsAvailable": 13},
    {"MovieID": 225, "MovieName": "Zootopia", "Showtime": "4:00 PM", "SeatsAvailable": 15},
]

undo_stack = []

reservation_queue = deque()


def display_movies():
    print("\nAvailable Movies:")
    for movie in movies:
        print(
            f"ID: {movie['MovieID']}, Movie: {movie['MovieName']}, Showtime: {movie['Showtime']}, Seats Available: {movie['SeatsAvailable']}")


def add_reservation(movie_id, num_seats):
    for movie in movies:
        if movie["MovieID"] == movie_id:
            if movie["SeatsAvailable"] >= num_seats:
                reservation_queue.append({"MovieID": movie_id, "SeatsRequested": num_seats})
                print(
                    f"Reservation request added for {num_seats} seat{'s' if num_seats > 1 else ''} to '{movie['MovieName']}' at {movie['Showtime']}.")
            else:
                print(
                    f"Not enough seats available for '{movie['MovieName']}'. Only {movie['SeatsAvailable']} seats are left.")
            return
    print("Invalid Movie ID. Please choose a valid movie from the list.")


def process_reservation():
    if reservation_queue:
        next_reservation = reservation_queue.popleft()
        for movie in movies:
            if movie["MovieID"] == next_reservation["MovieID"]:
                movie["SeatsAvailable"] -= next_reservation["SeatsRequested"]
                undo_stack.append(next_reservation)
                print(
                    f"Reservation confirmed for {next_reservation['SeatsRequested']} seat{'s' if next_reservation['SeatsRequested'] > 1 else ''} to '{movie['MovieName']}' at {movie['Showtime']}.")
                return
    else:
        print("No reservations to process.")


def undo_last_booking():
    if undo_stack:
        last_booking = undo_stack.pop()
        for movie in movies:
            if movie["MovieID"] == last_booking["MovieID"]:
                movie["SeatsAvailable"] += last_booking["SeatsRequested"]
                print(
                    f"Undo successful: {last_booking['SeatsRequested']} seat{'s' if last_booking['SeatsRequested'] > 1 else ''} returned to '{movie['MovieName']}' at {movie['Showtime']}.")
                return
    else:
        print("No bookings to undo.")


def view_reservations():
    if reservation_queue:
        print("\nCurrent Reservations:")
        for reservation in reservation_queue:
            for movie in movies:
                if movie["MovieID"] == reservation["MovieID"]:
                    print(
                        f"{reservation['SeatsRequested']} seat{'s' if reservation['SeatsRequested'] > 1 else ''} for '{movie['MovieName']}' at {movie['Showtime']}.")
    else:
        print("No reservation requests at the moment.")


def cinema_ticket_reservation():
    while True:
        print("\nOptions:")
        print("1. Display Available Movies")
        print("2. Add Reservation Request")
        print("3. Process Reservation")
        print("4. Undo Last Booking")
        print("5. View Reservations")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            display_movies()
        elif choice == '2':
            display_movies()
            try:
                movie_id = int(input("Enter Movie ID for reservation: "))
                num_seats = int(input("Enter the number of seats to reserve: "))
                add_reservation(movie_id, num_seats)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '3':
            process_reservation()
        elif choice == '4':
            undo_last_booking()
        elif choice == '5':
            view_reservations()
        elif choice == '6':
            print("Exiting cinema ticket reservation system.")
            break
        else:
            print("Invalid choice, please select a valid option.")


cinema_ticket_reservation()
