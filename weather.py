import requests


API_KEY = "03690956978e4857acd163401222612"  # Replace with your WeatherAPI key




def get_weather(location):
   # Current Weather
    current_weather_url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={location}"
    current_weather_response = requests.get(current_weather_url)
    current_weather_data = current_weather_response.json()

    # # Weather Alerts
    # alerts_url = f"http://api.weatherapi.com/v1/alerts.json?key={API_KEY}&q={location}"
    # alerts_response = requests.get(alerts_url)
    # alerts_data = alerts_response.json()

    # # Air Quality
    # air_quality_url = f"http://api.weatherapi.com/v1/airquality.json?key={API_KEY}&q={location}"
    # air_quality_response = requests.get(air_quality_url)
    # air_quality_data = air_quality_response.json()

    # # Astronomy Data
    # astronomy_url = f"http://api.weatherapi.com/v1/astronomy.json?key={API_KEY}&q={location}"
    # astronomy_response = requests.get(astronomy_url)
    # astronomy_data = astronomy_response.json()

    # # 10-day Forecast
    # forecast_url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={location}&days=10"
    # forecast_response = requests.get(forecast_url)
    # forecast_data = forecast_response.json()
    

    return (current_weather_data)
        # "alerts": alerts_data,
        # "air_quality": air_quality_data,
        # "astronomy": astronomy_data,
        # "forecast": forecast_data
    