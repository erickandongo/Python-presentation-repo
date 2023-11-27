import datetime

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

def current_bonus(bookings):
    current_month = datetime.datetime.now().strftime("%B")  # ---- O(1)       ____ O(n)
    current_bookings = []                                   # ---- O(1)   

    for booking in bookings:                                # -- O(n)
        if booking["booking_start_at"].find(current_month) != -1:  # ---O(1)
            current_bookings.append(booking)                        #----O(1)

    return current_bookings                                        # --- O(1)

def total_resident_bonus(current_bookings):            
    resident_current_bookings = []
    commercial_current_bookings = []

    for booking in current_bookings:
        if booking["is_commercial"] == False:
            resident_current_bookings.append(booking)
        else:
            commercial_current_bookings.append(booking)

    length_1 = len(resident_current_bookings)
    result1 = length_1 // 20
    remainder1 = length_1 % 20
    result2 = remainder1 // 10
    remainder2 = remainder1 % 10
    result3 = remainder2 // 5
    remainder3 = remainder2 % 5

    # Bonus for 20 pickups in a day is assumed to be 10,000 XAF
    bonus1 = (10000 * result1) + (5000 * result2) + (1000 * result3) + (50 * remainder3)

    length_2 = len(commercial_current_bookings)
    resulta = length_2 // 20
    remaindera = length_2 % 20
    resultb = remaindera // 10
    remainderb = remaindera % 10
    resultc = remainderb // 5
    remainderc = remainderb % 5

    # Bonus for 20 pickups in a day is assumed to be 10,000 XAF
    bonus2 = (10000 * resulta) + (5000 * resultb) + (1000 * resultc) + (50 * remainderc)

    total_bonus = bonus1 + bonus2

    return total_bonus

def N_shift(agent):  # ---O(n)
    morning_count = 0
    afternoon_count = 0

    shifts = agent["agent_shift"]

    for shift_list in shifts.values():
        morning_count += shift_list.count("morning")
        afternoon_count += shift_list.count("afternoon")

    total_shifts = morning_count + afternoon_count

    return total_shifts




current_bookings = current_bonus(bookings)
total_bonus = total_resident_bonus(current_bookings)
total_shifts = N_shift(agent)

# Calculate total salary
total_salary = (total_shifts * 500) + total_bonus

print("Total Salary:", total_salary)





    

    