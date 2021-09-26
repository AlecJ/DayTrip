"""
This will handle google places API calls


input = input string

locationbias=circle:2000@43.4100,-70.6700 # York Maine
locationbias=ipbias

"""

import requests

def test():
    url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
    fields = 'formatted_address,name,rating,opening_hours'
    params = {'key': 'AIzaSyBWpjOrljegFX1tFdWX2wwHeHOJXlWtI98',
              'input': 'food',
              'inputtype': 'textquery',
              'fields': fields,
              'locationbias': 'ipbias'}


    response = requests.get(url, params=params)

    print(response)
    if response.status_code == 200:
        print(response.json())
