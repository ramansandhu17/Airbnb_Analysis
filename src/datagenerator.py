import pandas as pd
import random
from datetime import datetime, timedelta

num_of_days=6*30
end_date=datetime(2025,2,1)
start_date=end_date-timedelta(num_of_days)

#print(start_date)
#print(end_date)

#create a list to get the date range
date_range=pd.date_range(start=start_date,end=end_date,freq='D')

#convert to a dataframe for easy indexing
df_airbnb=pd.DataFrame(date_range,columns=["Date"])

#print(df_airbnb.head())

#Add Occupancy column
occupancy_list=[]

for date in df_airbnb["Date"]:
    #check if 90% probability of booking
    if random.random() <(27/30):
        occupancy=1
    else:
        occupancy=0

    occupancy_list.append(occupancy)

df_airbnb["Occupancy"]=occupancy_list

print(df_airbnb.head())

#we will set the pricing here 


price_list=[]

for date in df_airbnb["Date"]:
    if date.weekday() in [4,5,6]:
        price=random.randint(130,210)
    else:
        price=random.randint(70,170)
    
    price_list.append(price)

df_airbnb["Price Per Night"]=price_list

#print(df_airbnb.head())

#Calculating the Revenue
df_airbnb["Revenue"]=df_airbnb["Price Per Night"]*df_airbnb["Occupancy"]

print(df_airbnb.head())


#Adding the property id

df_airbnb["PropertyID"]='P001'

print(df_airbnb.head())
# Adding GuestID to track the guest booking separately and also find out which guests had a good experience
''' this guest id is setup such that when occupancy is 1 it can be the same guest staying multiple nights
or it can be different guests staying single nights'''

#initializing variables to store guest ids and checking if its the same guest or a new one

occupancy_map = df_airbnb["Occupancy"].to_dict()  

# Step 2: Initialize Variables
guest_id_counter = 100  # Start Guest IDs from 100
previous_occupancy = 0   # Track previous night's occupancy
current_guest_id = None  # Store the guest ID for multiple nights
guest_id_list = []       # Store generated Guest IDs

for i in range(len(df_airbnb)):  # Loop through all rows
    if occupancy_map[i] == 1: 
        if previous_occupancy == 0 or random.random() < 0.3:  
            # If previous night was empty OR 30% chance for a new guest
            guest_id_counter += 1  # Increment Guest ID counter
            current_guest_id = f"G{guest_id_counter}"  # Create a new Guest ID
        
        guest_id_list.append(current_guest_id)  # Assign the same or new Guest ID
    else:
        guest_id_list.append("G0")  # No guest for unoccupied nights

    # Update previous occupancy status
    previous_occupancy = occupancy_map[i]  # Using HashMap for better performance

# Step 4: Add Guest IDs to the DataFrame
df_airbnb["Guest ID"] = guest_id_list

def generate_review():
    positive_reviews = [
        "Amazing stay, very clean and comfortable!", 
        "Great experience, would book again!", 
        "Loved the location, very convenient!", 
        "Host was very responsive and helpful!", 
        "Super cozy, highly recommend!", 
        "A perfect stay, felt like home!", 
        "Excellent amenities, everything as described!",
        "Great value for the price!",
        "Clean and well-maintained, fantastic experience!",
        "Would definitely stay here again!"
    ]
    
    negative_reviews = [
        "Not as expected, had some issues.",
        "Too loud at night, difficult to sleep.",
        "Not perfect for the area, felt overpriced.",
        "The cleanliness could have been better.",
        "Amenities were lacking, expected more.",
        "Photos were misleading, room was smaller.",
        "Host was slow to respond, frustrating.",
        "Could have been a better experience.",
        "Uncomfortable stay, wouldn't recommend.",
        "Not worth the price, expected better."
    ]
    
    # 90% positive, 10% negative review probability
    return random.choice(positive_reviews) if random.random() < 0.9 else random.choice(negative_reviews)
guest_map=df_airbnb["Guest ID"].to_dict()
review_list=[]
for i in range(len(df_airbnb)):
    if occupancy_map[i] == 1 and guest_map[i] != "G0":
        review_list.append(generate_review())
    else:
        review_list.append("")

df_airbnb["Reviews"]=review_list

df_airbnb.rename(columns={"Price Per Night": "PricePerNight","Guest ID":"GuestID"}, inplace=True)


print(df_airbnb.head())

df_airbnb.to_csv("AirbnbP001",index=False)
