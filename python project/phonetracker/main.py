import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

# Step 1: Input phone number (include country code)
number = "+919423043277"  # Example: Indian number
parsed_number = phonenumbers.parse(number)

# Step 2: Get location and carrier info
location = geocoder.description_for_number(parsed_number, "en")
sim_carrier = carrier.name_for_number(parsed_number, "en")

print("Location:", location)
print("Carrier:", sim_carrier)

# Step 3: Convert location to coordinates using OpenCage
key = "15d729b05c3a4873bf41074148e73b0d"  # Get free key at https://opencagedata.com
geocoder_service = OpenCageGeocode(key)
results = geocoder_service.geocode(location)

if results:
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(f"Latitude: {lat}, Longitude: {lng}")

    # Step 4: Generate map
    myMap = folium.Map(location=[lat, lng], zoom_start=10)
    folium.Marker([lat, lng], popup=location).add_to(myMap)

    # Step 5: Save map to HTML
    myMap.save("location.html")
    print("Map saved as location.html")
else:
    print("Location not found.")