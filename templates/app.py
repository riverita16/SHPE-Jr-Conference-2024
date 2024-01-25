from spot import Spot
from flask import Flask, request
from threading import Timer

HOST_IP_ADDRESS = 'localhost'
HOST_PORT = '8080'

# You may change this if you add other functiality
SCOPE = 'playlist-modify-private playlist-modify-public'

'''
Add yours here!
You can find these in your Developer Dashboard under your app's settings.
'''
CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = 'http://localhost:8080/callback'

# You use this object to make your requests to the API
spot = Spot(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)

app = Flask('NAME ME')

def start():
    spot.authorize(SCOPE)

# this is what will run when you authenticate the user
@app.route('/callback', methods=['POST', 'GET'])
def callback():
    code = request.args.get('code')
    credentials = spot.get_token(code)
    spot.ACCESS_TOKEN = credentials['access_token']

    print('\nAuthenticated and ready to go!\n')
    spot.close_browser()

    search_ex()

    return 'Success'

# Example: jsonifyng and search for a song id
def search_ex():
    endpoint = 'https://api.spotify.com/v1/search?'
    
    song = 'Titi Me Pregunto'
    artist = 'Bad Bunny'

    # check the api documentation for the expected parameters and what they mean
    params = {
        'q':f'{song} {artist}', 
        'type':'track', 
        'limit':1
    }

    response = spot.GET(endpoint, params)

    # check that we have data
    if len(response['tracks']['items']) == 0:
        print('Failed to fetch song')

    track = response['tracks']['items'][0]
    track_id = track['id']

    print(f'\nTrack ID is {track_id}\n')


'''
Define more functions to help your implementation!
'''

if __name__ == '__main__':
    Timer(1, start).start()
    app.run(host=HOST_IP_ADDRESS, port=HOST_PORT, use_reloader=True, debug=True)

    # search_ex()
