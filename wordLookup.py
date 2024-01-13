import requests

def getDefinitions(word_id):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word_id
    response = requests.get(url).json()
    if 'error' in response[0].keys():
        return False
    output = {}
    senses = response[0].get('meanings')[0].get('definitions')
    definitions = []
    for sense in senses:
        definitions.append(f'👉 {sense.get("definition")}')

    output['definitions'] = "\n".join(definitions)

    if response[0].get('phonetics')[0].get('audio'):
        output['audio'] = response[0].get('phonetics')[0].get('audio')

    return output




