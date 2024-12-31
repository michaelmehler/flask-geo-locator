from flask import Flask, request, render_template  # Import necessary Flask modules
import requests  # Library for making HTTP requests

# Initializes the Flask application
app = Flask(__name__)

# Defines the API endpoint (the route that clients interact with to get the geolocation data and display it on a map) 
@app.route('/') 
# Function runs when '/' route is accessed
# Handles the the request, processing of the geolocation, and returning of the result
def home():
    # Retrieves the client's IP address from the incoming request 
    ip_address = request.remote_addr

    # For local testing (since `127.0.0.1` is localhost), creates a mock IP:
    if ip_address == "127.0.0.1":
        ip_address = "8.8.8.8"  # Example IP for testing

    # Constructs the URL for the external geolocation API (ipinfo.io) 
    geo_url = f"https://ipinfo.io/{ip_address}/json"
    # Makes a GET request to the geo_url using the request library 
    # geolocation API responds with geolocation data in JSON (JavaScript Object Notation) format
    response = requests.get(geo_url) 

    # Converts response into a Python dictionary (data structure) since response is a HTTP response object 
    geo_data = response.json()
    # Retrieves the 'loc' field from the geo_data (a Python dictionary) 
    # Where the singular string is split into two strings (longitude and latitude) and is returned as a list
    location = geo_data.get("loc", "0,0").split(",")  # Default to "0,0" if not available 
    # Extracts the latitude and longitude from the list, loction, and assigns them two their respective variables 
    latitude, longitude = location[0], location[1]
    # Retrieves the 'city' field from geo_data and defaults to 'Uknown' if not available 
    city = geo_data.get("city", "Unknown")

    # Constructs and returns a string with the longitude and latitude 
    return f"City: {city}; Location: Latitude={latitude}, Longitude={longitude}" # F-string formatting (allows for string to be created with variable data at runtime) 

    # Passes data to the map.html template
    # return render_template('map.html', latitude=latitude, longitude=longitude, city=city)

