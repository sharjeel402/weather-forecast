from bs4 import BeautifulSoup
from django.shortcuts import render
import requests

# Create your views here.

def index(request):

    url = "https://www.timeanddate.com/weather/pakistan/islamabad/ext"
    #city = input("enter the name of the city of pakistan that you want to find wheter: ")
    #page = url.format(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.select('tbody tr')
    #city=soup.select_one('header.pg-title h1.pg-title__title').text
    #print(city)
    whether_info = []
    for info in table:
        day = info.select_one('th').text.strip()
        whether = info.find('td', 'small').contents[0]
        temperature = info.select_one('td.sep').string
        wind = info.find('td', 'sep').find_next('td').text
        humidity = info.find('td', 'sep').find_next('td').find_next('td').find_next('td').text
        whether_info.append((day, whether, temperature, wind, humidity))
    
    return render(request, 'app/home.html', {'whether_info': whether_info})
