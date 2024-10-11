from collections import deque

available_cars = [
    "Toyota Corolla", "Honda Civic", "Ford Focus", "Chevrolet Malibu", "Nissan Altima",
    "BMW 3 Series", "Mercedes-Benz C-Class", "Audi A4", "Volkswagen Jetta", "Hyundai Elantra",
    "Kia Optima", "Mazda 6", "Subaru Impreza", "Tesla Model 3", "Volvo S60",
    "Jaguar XE", "Lexus ES", "Acura TLX", "Infiniti Q50", "Lincoln MKZ",
    "Porsche 911", "Ferrari 488", "Lamborghini Huracan", "McLaren 720S", "Bugatti Chiron"
]

sales_stack = []

sales_requests_queue = deque()


def display_available_cars():
    print("\nAvailable Cars:")
    for index, car in enumerate(available_cars, 1):
        print(f"{index}. {car}")


def add_sales_request(car_number):
    if 1 <= car_number <= len(available_cars):
        car = available_cars[car_number - 1]
        sales_requests_queue.append(car)
        print(f"Sales request added: {car}")
    else:
        print(f"Invalid choice. Please choose a valid number from the available cars list.")


def process_sales_request():
    if sales_requests_queue:
        sold_car = sales_requests_queue.popleft()
        available_cars.remove(sold_car)
        sales_stack.append(sold_car)
        print(f"Car sold: {sold_car}")
    else:
        print("No sales requests to process.")


def undo_last_sale():
    if sales_stack:
        last_sold_car = sales_stack.pop()
        available_cars.append(last_sold_car)
        print(f"Sale undone: {last_sold_car} is back in inventory.")
    else:
        print("No sales to undo.")


def view_sales_requests():
    if sales_requests_queue:
        print("\nCurrent Sales Requests:")
        for car in sales_requests_queue:
            print(f"- {car}")
    else:
        print("No sales requests at the moment.")


def car_dealership_management():
    while True:
        print("\nOptions:")
        print("1. Display Available Cars")
        print("2. Add Sales Request")
        print("3. Process Sales Request")
        print("4. Undo Last Sale")
        print("5. View Sales Requests")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            display_available_cars()
        elif choice == '2':
            display_available_cars()
            try:
                car_number = int(input("Enter the number of the car for the sales request: "))
                add_sales_request(car_number)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '3':
            process_sales_request()
        elif choice == '4':
            undo_last_sale()
        elif choice == '5':
            view_sales_requests()
        elif choice == '6':
            print("Exiting car dealership management system.")
            break
        else:
            print("Invalid choice, please select a valid option.")


car_dealership_management()
