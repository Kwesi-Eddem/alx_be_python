from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()

    print(f"Current date: {current_date.strftime("%Y-%m-%d %H:%M:%S")}")

display_current_datetime()


def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    today = datetime.today()
    future_date = today + timedelta(days=number_of_days)

    print(f"{future_date.strftime("%Y-%m-%d")}")

calculate_future_date()