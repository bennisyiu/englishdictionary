import requests
import json

word = input('Please input an English word: ')

url = "https://wordsapiv1.p.rapidapi.com/words/" + word

headers = {
    'x-rapidapi-key': "19bf38b831mshb20c520ea8969fdp1b943djsna0cd8874269a",
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

# print(response.status_code)
if response.status_code == 200:
    print(f"The word you input is {word}")
    json_response = json.loads(response.text)
    # print(json_response)
    results = json_response["results"]
    definition = results[0]["definition"]
    part_of_speech = results[0]["partOfSpeech"]
    print(f"Definition: {definition}")
    print(f"Part of Speech: {part_of_speech}")
else:
    print('Word not found')
