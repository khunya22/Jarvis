import requests

# API KEY = 0209778eaa6148d8b68b6484ff217a4f

BASE_URL = "http://api.football-data.org/v4/"
API_KEY = "NULL"
class Soccer():
    def __call__(self, jarvis, s):
        print('\nFeature powered by football-data.org APIs')
        if API_KEY == 'NULL':
            primn

    def get_competitions(self):
        headers = {
            'X-Auth-Token': API_KEY
        }
        response = requests.get(BASE_URL + 'competitions', headers=headers)
        if response.status_code == 200:
            payload = response.json()
            competitions = payload['competitions']
            for competition in competitions:
                print(f"{competition['name']:<30} (ID: {competition['id']})")


if __name__ == '__main__':
    main()