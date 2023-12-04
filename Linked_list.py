import random
from datetime import datetime, timedelta

subscription = {"standard": 1,"premium": 2,"VIP": 3}


class Date:
    def __init__(self, date):
        self.date = date
        self.next = None  # Initialize next as None

class PickupList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_date(self, date):
        new_date = Date(date)
        if not self.head:
            self.head = new_date
            self.tail = new_date
        else:
            self.tail.next = new_date
            self.tail = new_date
        self.length += 1

    def pickup_days_in_month(self, subscription):
        # Get the current date
        current_date = datetime.now().date()

        # Convert current_date to a datetime object
        current_date = datetime(current_date.year, current_date.month, current_date.day)

        # Calculate the last day of the current month
        last_day_current_month = datetime(current_date.year, current_date.month, current_date.day) + timedelta(days=31)

        if subscription == 1:
            # Generate random days for each week in the month
            while current_date + timedelta(days=7) <= last_day_current_month:
                random_day_index = random.randint(0, 6)
                random_date = current_date + timedelta(days=random_day_index)

                # Add the date to the linked list
                self.add_date(random_date.strftime('%Y-%m-%d'))

                # Move to the next week
                current_date += timedelta(days=7)

        if subscription == 2:
            # Generate 2 random days for each week in the month
            while current_date + timedelta(days=7) <= last_day_current_month:
                for _ in range(2):
                    random_day_index = random.randint(0, 6)
                    random_date = current_date + timedelta(days=random_day_index)

                    # Add the date to the linked list
                    self.add_date(random_date.strftime('%Y-%m-%d'))

                # Move to the next week
                current_date += timedelta(days=7)

        if subscription == 3:
            # Generate 3 random days for each week in the month
            while current_date + timedelta(days=7) <= last_day_current_month:
                for _ in range(3):
                    random_day_index = random.randint(0, 6)
                    random_date = current_date + timedelta(days=random_day_index)

                    # Add the date to the linked list
                    self.add_date(random_date.strftime('%Y-%m-%d'))

                # Move to the next week
                current_date += timedelta(days=7)



# Example usage:
pickup_list = PickupList()
pickup_list.pickup_days_in_month(subscription=1)

# Print the dates stored in the linked list
current_node = pickup_list.head
while current_node:
    print(current_node.date)
    current_node = current_node.next


    #     if subscription == 2:
    #         pass
    #     if subscription == 3:
    #         pass
        
    #     else:
    #         pass 
        
        

    # # Example usage:
    # random_days = pickup_days_in_month()

    # # Print the randomly chosen days
    # for idx, date in enumerate(random_days, start=1):
    #     print(f"Week {idx}: {date}")
