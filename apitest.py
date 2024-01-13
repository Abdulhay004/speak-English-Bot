import requests
# import json
# app_id = "<your_app_id>"
# app_key = "<your_app_key>"
# language = "en-gb"
word_id = "apple"
url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word_id.lower()
response = requests.get(url).json()

# print(response)

audio = response[0].get('phonetics')[0].get('audio')
desc1 = response[0].get('meanings')[0].get('definitions')[0].get('definition')
desc2 = response[0].get('meanings')[0].get('definitions')[1].get('definition')

print(desc1)
print(desc2)
