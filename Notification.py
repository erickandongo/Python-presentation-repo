import datetime
import math

agent = {

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
}


# booking list
bookings = [
    {
        "_id": {"$oid": "649b0a4d77cb44c555f672f9"},
        "owner_amount": 2000,
        "owner_id": "6495afc32937ad6e5d431c2f",
        "request_status": "Completed",
        "service_type": "pickup",
        "system_price": 1500,
        "description": "the second blue trash bin on the street",
        "localisation": {"latitude": 14.2437, "longitude": 118.2437},
        "trash_bin_image_url": "",
        "is_commercial": False,
        "booking_start_at": "November 14, 2023 at 17:23:33 UTC1:00:00.000000",
    },
    {
        "_id": {"$oid": "649b0a4d77cb44c555f672f9"},
        "owner_amount": 2000,
        "owner_id": "6495afc32937ad6e5d431c2f",
        "request_status": "Completed",
        "service_type": "pickup",
        "system_price": 1500,
        "description": "the second blue trash bin on the street",
        "localisation": {"latitude": 14.2437, "longitude": 118.2437},
        "trash_bin_image_url": "",
        "is_commercial": False,
        "booking_start_at": "November 13, 2023 at 17:23:33 UTC1:00:00.000000",
    },
    {
        "_id": {"$oid": "649b0a4d77cb44c555f672f9"},
        "owner_amount": 2000,
        "owner_id": "6495afc32937ad6e5d431c2f",
        "request_status": "Completed",
        "service_type": "pickup",
        "system_price": 1500,
        "description": "the second blue trash bin on the street",
        "localisation": {"latitude": 14.2437, "longitude": 118.2437},
        "trash_bin_image_url": "",
        "is_commercial": False,
        "booking_start_at": "June 13, 2023 at 17:23:33 UTC1:00:00.000000",
    },
    
]

class Notification:
    package = ['Pickup', 'Pickup and clean']
    trash_size = {'bucket': 10, 'trash_bag':27, 'wheelbarrow':80}
    completed_booking = [
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

    landfill = [
        {
            'city': 'Yaounde',
            'country': 'Cameroon',
            'state': 'Center',
            'street': 'Dallas',
            'zip': 7315,
            'description': 'The second blue trash bin on the street',
            'localisation': {'latitude': 14.2437, 'longitude': 118.2437},
            'trash_bin_id': '',
            "trash_bin_image_url": ""

        }
    ]

    service_to_redeem = {
        'voice_call': 100,
        'text_message': 50,
        'electricity': 1000,
        'data_bundle': 200
    }


    def __init__(self, booking, agent):
        self.booking = booking
        self.agent = agent
    
    def price_det(self, size, quantity, bid_price):
        #  determine trash's volume
        for key, value in self.trash_size:
            if key == size:
                trashsize = self.trash_size['key']
                volume = trashsize * quantity 

        # determine the price 
        price = volume * 100

        # determine the final price with biding
        if price <= bid_price:
            final_price = bid_price
        else:
            final_price = price




    def agent_assignment(self):
        # make sure that the volume of the request can be managed by the agent

        request = [] 
        send_to_admin = []
        for i in self.booking:
            string = i["size"]
            if string in self.trash_size:
                volume = self.trash_size[string]
                if volume * i["quantity"] < 160:
                    request.append(i)
                else:
                    send_to_admin.append(i)
                    print("We don't have the capacity")
           

        # determine the distance between the agent and the request using harversine
        agent_request_distance = []

        for booking in request:
            for agent in self.agent:
                lat1, lon1 = agent['location_information']["location"]["latitude"], agent['location_information']["location"]["longitude"]
                lat2, lon2 = booking["localisation"]["latitude"], booking["localisation"]["longitude"]
                radius = 6371  # km
            
                dlat = math.radians(lat2-lat1)
                dlon = math.radians(lon2-lon1)
                a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
                    * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
                c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
                d = radius * c
                # append to the dictionary the agent and it's distance from the request
                agent_request_distance.append(d)
            
        # determine the smallest distance between the agent and the request 
        assigned_agent = min(agent_request_distance)
        print(assigned_agent)

        return assigned_agent


    def closest_landfill(self, landfill):
        # determine the distance between the place of request and the closest landfill using harversine
        request_landfill_distance = []

        for booking in self.booking:
            for landfill in self.landfill:
                lat1, lon1 = landfill["localisation"]["latitude"], landfill["localisation"]["longitude"]
                lat2, lon2 = booking["localisation"]["latitude"], booking["localisation"]["longitude"]
                radius = 6371  # km
            
                dlat = math.radians(lat2-lat1)
                dlon = math.radians(lon2-lon1)
                a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
                    * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
                c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
                d = radius * c
                # append to the dictionary the agent and it's distance from the request
                request_landfill_distance.append(d)
            
        # determine the smallest distance between the agent and the request 
        closest = min(request_landfill_distance)
        print('The closest landfill is ', closest, 'KM aways.')

        return closest

    