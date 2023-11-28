import math


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

class Closest_landfill:
    def __init__(self, request, landfills):
        self.request = request
        self.landfills = landfills

    def distance(self):
        # determine the distance between the place of request and the closest landfill using harversine
        request_landfill_distance = []

        for booking in self.request:
            for landfill in self.landfills:
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
    
landfill_found = Closest_landfill(requests, landfill)
landfill_found.distance()
    