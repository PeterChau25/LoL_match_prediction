import requests
import urllib.parse
main_api = 'https://maps.googleapis.com/maps/api/geocode/json?'
address = 'lhr'

while True:
    address = input('address: ')
    url = main_api + urllib.parse.urlencode({'address': address})

    json_data = requests.get(url).json()
    print(json_data)

    json_status = json_data['status']
    print('API Status: ' + json_status)

    if json_status == 'OK':

        formatted_address = json_data['results'][0]['formatted_address']
        print()
        print(formatted_address)