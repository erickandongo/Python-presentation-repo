import datetime

agent_shifts =[
     {

  "agent_id": 1,
  "agent_shift": {
    "Monday": [
      "morning"
    ],
    "Tuesday": [
      "afternoon"
    ],
    "Wednesday": [
      "morning",
      "afternoon"
    ],
    "Thursday": [
      "afternoon"
    ],
    "Friday": [
      "morning",
      "afternoon"
    ],
    "Saturday": [
      "morning"
    ],
    "Sunday": []
  },
  "availability": True,
  "first_name": "Ericka",
  "last_name": "Ndongo",
  "location_information": {
    "address": [
      "yaoundé",
      "Cameroon",
      "Simbock"
    ],
    "location": {
      "latitude": 3.8384765,
      "longitude": 11.5006256
    },
    "quater": "Simbock"
  },
  "account_status": "active"
},
{

  "agent_id": 2,
  "agent_shift": {
    "Monday": [
      "morning"
    ],
    "Tuesday": [
      "afternoon"
    ],
    "Wednesday": [
      "morning",
      "afternoon"
    ],
    "Thursday": [
      "afternoon"
    ],
    "Friday": [
      "morning",
      "afternoon"
    ],
    "Saturday": [
      "morning"
    ],
    "Sunday": []
  },
  "availability": True,
  "first_name": "Ericka",
  "last_name": "Ndongo",
  "location_information": {
    "address": [
      "yaoundé",
      "Cameroon",
      "Simbock"
    ],
    "location": {
      "latitude": 13.8384765,
      "longitude": 117.5006256
    },
    "quater": "Simbock"
  },
  "account_status": "active"
}
]




bookings = [
    {
        'booking': '',
        'booking_start_at' : datetime.date(2023, 11, 24), 
        'booking_year': '',
        'cancel_by': '',
        'cancelation_date': datetime.date(2023, 11, 24), 
        'closest_landfill_location': '',
        'completion_date': '',
        'estimated_request_distance': '',
        'estimated_request_time': datetime.datetime(2023, 11, 24, 9, 0, 0),
        'time_arrived': datetime.datetime(2023, 11, 24, 9, 30, 0), 
        'final_price': '400',
        'rating': 5,
        'agent_id': 'a',
        'agent_pickup_end_at': datetime.date(2023, 11, 24),
        'agent_pickup_start_at': '',
        'booking_created_at': "2023-11-24T21:33:04.788453",
        'house_image_url': '',
        'owner_id': '',
        'request_status': 'Successful',
        'service_type': 'Pickup',
        'timestamp': '2023-11-24T21:33:10+0000',
        'trash_information_id': "6d307"
        
    }
]

class AgentPerformance:
    def __init__(self, start_date, end_date, agent_shift, booking):
        self.start_date = start_date
        self.end_date = end_date
        self.agent_shift =agent_shift
        self.booking = booking

    def newRequestList(self):
        # determine the request for the period choosen
        request = []

        for booking in self.booking:
        # # Convert the timestamp string to a datetime object
        #     timestamp_datetime =  datetime.datetime.strptime(booking['timestamp'], '%d-%B-%Y %A')  
        #     print(type(timestamp_datetime))
        #     print(timestamp_datetime)

            if self.start_date <= booking['booking_start_at'] <= self.end_date:
                request.append(booking)
            else:
                print("The timestamp does not fall between the start and end dates.")
        return request

    def hoursLaboured(self, id, request):

        ## determine the number of hours laboured 
        # Calculate the time difference between the two dates

        for booking in request:
            if booking['agent_id'] == id:
                change_time = booking['agent_pickup_end_at'] - booking['booking_start_at']
                
            else:
                pass

        # Extract the total number of hours from the time difference
        hours =  change_time.total_seconds() / 3600
        
        return hours

    def numberOfShifts(self):

        # number of shifts of the agent 
        morning_count = 0
        afternoon_count = 0
        for agent_shift in self.agent_shift:
            shifts = agent_shift["agent_shift"]

            for shift_list in shifts.values():
                morning_count += shift_list.count("morning")
                afternoon_count += shift_list.count("afternoon")

            total_shifts = morning_count + afternoon_count


        # Calculate the time difference between the two dates
        time_difference = self.end_date - self.start_date

        # Extract the total number of hours from the time difference
        weeks = time_difference.total_seconds() / 7
        number_of_shifts = weeks * total_shifts

        return number_of_shifts

    def numberOfBookings(self, id, request):

        # determine the total number of bookings 
        number_of_booking = 0
        for booking in request:
            if id ==  booking['agent_id']:
                number_of_booking += 1
        return number_of_booking
    
    def rating(self, request): 
        # determine the average rating 
        length = len(request)
        for booking in request:
            average = booking['rating'] //length
        return average
    
    def punctuality(self, request):
        # determine the punctuality of the agent in the given period
        for booking in request:
            late = booking['time_arrived'] - booking['estimated_request_time']
            hours_late =  late.total_seconds() / 3600

        return hours_late

    def performance(self, average, hours, number_of_booking, number_of_shifts, late):
        rating_weight = 0.3
        hours_weight = 0.2
        requests_weight = 0.2
        shifts_weight = 0.1 
        punctuality_weight = 0.2

        
        ratingScore = average * rating_weight
        hoursScore = hours * hours_weight
        requestsScore = number_of_booking * requests_weight
        shiftsScore = number_of_shifts * shifts_weight

        punctualityScore = late* punctuality_weight

        totalScore = ratingScore + hoursScore + requestsScore + shiftsScore + punctualityScore

        print(totalScore)
        return totalScore


performance1 = AgentPerformance(datetime.date(2023, 8, 24), datetime.date(2023, 12, 24), agent_shifts, bookings)

request_list = performance1.newRequestList()

total_hours_laboured = performance1.hoursLaboured('a', request_list)
total_number_of_shifts = performance1.numberOfShifts()
total_number_of_booking = performance1.numberOfBookings('a', request_list)
average_rating = performance1.rating(request_list)
hours_late = performance1.punctuality(request_list)

performance = performance1.performance(average_rating, total_hours_laboured, total_number_of_booking, total_number_of_shifts, hours_late)
