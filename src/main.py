from src import tokens

import requests

debug = True

API_URL = "https://api.deutschebahn.com/1bahnql/v1"
STATION_NAME = "Berlin Hauptbahnhof"

if debug:
    key = tokens.DB_APP_KEY_SANDBOX
    secret = tokens.DB_APP_SECRET_SANDBOX
    token = tokens.DB_APP_TOKEN_SANDBOX
else:
    key = tokens.DB_APP_KEY_PRODUCTION
    secret = tokens.DB_APP_SECRET_PRODUCTION
    token = tokens.DB_APP_TOKEN_PRODUCTION


def search_station(station_name):
    search_string = f"""
    {{
        search(searchTerm: "{station_name}") {{
            stations {{
                name
                primaryEvaId
            }}
        }}
    }}
    """
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(API_URL, data=search_string, headers=headers)
    return response


def main():
    station = search_station(STATION_NAME)
    print(station)


main()
