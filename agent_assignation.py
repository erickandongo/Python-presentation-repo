import math

trash_size = {'bucket': 10, 'trash_bag':27, 'wheelbarrow':80}

agents =[
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

# booking list
requests = [
    {
        "_id": {"$oid": "649b0a4d77cb44c555f672f9"},
        "size": "bucket",
        "quantity": 2,
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
        "size": "bucket",
        "quantity": 2,
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
        "size": "bucket",
        "quantity": 2,
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


class AgentAssign:
    def __init__(self, requests, agents):
        self.requests = requests
        self.agents = agents

    def distance(self):

   # make sure that the volume of the request can be managed by the agent

        request = [] 
        send_to_admin = []
        for i in self.requests:
            string = i["size"]
            if string in trash_size:
                volume = trash_size[string]
                if volume * i["quantity"] < 160:
                    request.append(i)
                else:
                    send_to_admin.append(i)
                    print("We don't have the capacity")
           

        # determine the distance between the agent and the request using harversine
        agent_request_distance = []

        for booking in request:
            for agent in self.agents:
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
    



agent_assign = AgentAssign(requests, agents)
agent_assign.distance()
