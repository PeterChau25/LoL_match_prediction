import requests
import urllib.parse
api_key = ''
#https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/peteleetzor?api_key=RGAPI-91df046a-259a-48a9-a093-b4f14b5e763d
while True:
    summoners = input('Enter Summoner name ')
    api_key = input('Enter API key: ')

    url = 'https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + summoners +'?'
    print(url)
    main_url = url + urllib.parse.urlencode({'api_key': api_key})

    json_data = requests.get(main_url).json()
    accountID = json_data['accountId']
    print(accountID)

    match_url = 'https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/' + str(accountID) + '?api_key=RGAPI-91df046a-259a-48a9-a093-b4f14b5e763d'

    match_data = requests.get(match_url).json()
    print(match_data['timestamp'])
