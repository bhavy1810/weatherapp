from django.shortcuts import render
import json
import urllib.request 

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        res = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=b2848897bf8549b89a80174b5e834dcb').read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(round(json_data['main']['temp'] - 273.15, 2)) + '°C',
            "pressure": str(json_data['main']['pressure']) + 'hPa',
            "humidity": str(json_data['main']['humidity']) + '%'
        }  
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city , 'data': data})