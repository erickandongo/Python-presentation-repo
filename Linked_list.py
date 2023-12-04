import random
from datetime import datetime, timedelta

class Date:
    def __init__(self, date):
        self.date = date
        self.next = next 

class PickupList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

def pickup_days_in_month(subscribtion):
    # Get the current date
    current_date = datetime.now().date()

    # Convert current_date to a datetime object
    current_date = datetime(current_date.year, current_date.month, current_date.day)

    # Calculate the last day of the current month
    last_day_current_month = datetime(current_date.year, current_date.month, current_date.day) + timedelta(days=31)

    if subscribtion == 1: 
        # Generate random days for each week in the month
        #instead of creating a list it should create a linked list 
        random_days = []
        while current_date +timedelta(days = 7) <= last_day_current_month:
            random_day_index = random.randint(0, 6)
            random_date = current_date + timedelta(days=random_day_index)
            #this should be in a linked list not a list 
            random_days.append(random_date.strftime('%Y-%m-%d'))

            # Move to the next week
            current_date += timedelta(days=7)
        return random_days

    if subscribtion == 2:
        pass
    if subscribtion == 3:
        pass
    
    else:
        pass 
    
    

# Example usage:
random_days = random_days_in_month()

# Print the randomly chosen days
for idx, date in enumerate(random_days, start=1):
    print(f"Week {idx}: {date}")
