from django.shortcuts import render
import requests

# Create your views here.
def index (request):
    city = request.GET.get('city',"Mumbai")
    api_key = 'e413ec4788d4c9689d6106eefd2ad505'
    url =f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'

    weather_data ={}
    error_message = None

    try:
        response = requests.get(url).json()
        if response.get('cod') !=200:
            raise ValueError(f"City '{city}' not found")
    
        weather_data = {
            'city' : city,
            'temperature' : response['main']['temp'],
            'description' : response['weather'][0]['description'],
            'humidity' : response['main']['humidity'],
            'wind_speed' : response['wind']['speed']
    }
    except ValueError as e :
        error_message = str(e)



    return render (request, 'weather/index.html', {'weather_data' : weather_data, 'error_message' : error_message})