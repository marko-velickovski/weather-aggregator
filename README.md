# Weather Aggregation

## Setup

1. **Clone the repo**:

   ```bash
   git clone git@github.com:marko-velickovski/weather-aggregator.git
   cd weather-aggregator
   ```

2. **Install Poetry**:

   - Install Poetry `pipx install poetry`

3. **Install dpendencies**:

   ```bash
   poetry install
   ```

4. **Set the virtual env created by poetry as your project python interpreter**

   - the path should look like `/Users/<user>/Library/Caches/pypoetry/virtualenvs/weather-aggregator-NqLysaSe-py3.12`

5. **DB setup**:

   ```bash
   poetry run python3 manage.py makemigrations
   poetry run python3 manage.py migrate
   ```

6. **Run the Application**:

   ```bash
   poetry run python3 manage.py runserver
   ```

   The application will start at `http://127.0.0.1:8000/`.

## API Documentation

1. POST /bulgarian_meteo_pro – Add new data for BulgarianMeteoPro station

   - body JSON:
     ```json
     {
       "station_id": "BG-STATION-001",
       "city": "Sofia",
       "latitude": 42.6977,
       "longitude": 23.3219,
       "timestamp": "2024-09-24T10:15:30Z",
       "temperature_celsius": 22.5,
       "humidity_percent": 65.0,
       "wind_speed_kph": 14.3,
       "station_status": "active"
     }
     ```
   - response - BulgarianMeteoPro serializer object:
     ```json
     {
       "id": 1,
       "station_id": "BG-STATION-001",
       "city": "Sofia",
       "latitude": 42.6977,
       "longitude": 23.3219,
       "timestamp": "2024-09-24T10:15:30Z",
       "temperature_celsius": 22.5,
       "humidity_percent": 65.0,
       "wind_speed_kph": 14.3,
       "station_status": "active"
     }
     ```

2. GET /bulgarian_meteo_pro - Get all BulgarianMeteoPro stations data

   - response: List of BulgarianMeteoPro objects, list of all data for that type of station

3. POST /weather_master_x - Add new data for WeatherMasterX station

   - body JSON:
     ```json
     {
       "station_identifier": "WX-3456",
       "location": {
         "city_name": "Plovdiv",
         "coordinates": {
           "lat": 42.1354,
           "lon": 24.7453
         }
       },
       "recorded_at": "2024-09-24T10:20:45Z",
       "readings": {
         "temp_fahrenheit": 73.4,
         "humidity_percent": 58.0,
         "pressure_hpa": 1012.3,
         "uv_index": 5,
         "rain_mm": 0.0
       },
       "operational_status": "operational"
     }
     ```
   - response - WeatherMasterX serializer object:
     ```json
     {
       "id": 1,
       "station_identifier": "WX-3456",
       "location": {
         "city_name": "Plovdiv",
         "coordinates": {
           "lat": 42.1354,
           "lon": 24.7453
         }
       },
       "recorded_at": "2024-09-24T10:20:45Z",
       "readings": {
         "temp_fahrenheit": 73.4,
         "humidity_percent": 58.0,
         "pressure_hpa": 1012.3,
         "uv_index": 5,
         "rain_mm": 0.0
       },
       "operational_status": "operational"
     }
     ```

4. GET /weather_master_x - Get all WeatherMasterX stations data

   - response: List of WeatherMasterX objects, list of all data for that type of station

5. GET /stations/aggregate-city-weather/<city_name> - Aggregate data for all stations in a given city

   - response: A JSON with the aggregate data for all the weather stations in a city and a list of all of the stations. station_data is a list of BulgarianMeteoPro and WeatherMasterX serializer objects
     ```json
     {
       "city": "Plovdiv",
       "average_temperature_celsius": 12.3,
       "average_humidity_percent": 11.5,
       "average_wind_speed_kph": 3.5,
       "station_data": [
         ...
       ]
     }
     ```
