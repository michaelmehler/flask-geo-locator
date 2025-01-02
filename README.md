# Flask Geo Locator

This Flask web application extracts the client's IP address, performs geolocation lookup using the ipinfo.io API, and displays the location on an embedded Google Map.

---

## Features
- Extracts the client's IP address dynamically.
- Uses the ipinfo.io API to retrieve geolocation data (city, latitude, and longitude).
- Displays the geolocation on an interactive Google Map with a marker.
- Allows testing with custom IPs via a query parameter.

---

## Prerequisites
- Python 3.8 or higher

---

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/michaelmehler/flask-geo-locator.git
cd flask-geo-locator
```

### Step 2: Set Up a Virtual Environment 
```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

### Step 3: Install Dependencies
```bash
pip install flask requests
```

### Step 4: Set Up Your Google Maps API Key

To use the Google Maps JavaScript API, you need to generate an API key. Follow these steps:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create or select an existing project.
3. Navigate to **APIs & Services** > **Credentials**.
4. Click **+ CREATE CREDENTIALS** > **API key**.
5. Restrict your API key to improve security:
   - **Application Restrictions**: Set to `HTTP referrers (websites)` and add:
     ```
     http://127.0.0.1:5000/*
     ```
6. Copy your API key.
7. Open `templates/map.html` and replace `YOUR_GOOGLE_MAPS_API_KEY` with your actual API key:
   ```html
   <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_GOOGLE_MAPS_API_KEY"></script>
   ```
   
---

## Usage 
- Run flask app with bash flask run
- Accessing the application
  - Visit http://127.0.0.1:5000/ (the IP address will default to Google's public DNS, 8.8.8.8) 
  - Test with a custom IP address:
    - Use the query parameter ?ip=test_ip, where test_ip is the desired IP address.
    - Example: http://127.0.0.1:5000/?ip=1.1.1.1.
 
