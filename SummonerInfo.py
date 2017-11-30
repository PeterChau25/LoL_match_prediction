import requests
import urllib.parse
api_key = ''
#https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/peteleetzor?api_key=RGAPI-fcb7953a-74c7-4190-9a41-747445ccfd2b
while True:
    summoners = input('Enter Summoner name ')
    api_key = input('Enter API key: ')

    url = 'https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + summoners +'?'
    print(url)
    main_url = url + urllib.parse.urlencode({'api_key': api_key})

    json_data = requests.get(main_url).json()
    accountID = json_data['accountId']
    print(accountID)

    match_url = 'https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/' + str(accountID) + '?api_key=RGAPI-fcb7953a-74c7-4190-9a41-747445ccfd2b'

    match_data = requests.get(match_url).json()
    for i in range(0, 100):
        print(match_data['matches'][i])
