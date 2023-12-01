import requests
import uuid
import urllib
import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Spot:
    def __init__(self, cid, secret, redirect) -> None:
        self.CLIENT_ID = cid
        auth = cid + ":" + secret
        self.BASE64_AUTH_STR = base64.b64encode(auth.encode()).decode('utf-8')
        self.REDIRECT_URI = redirect

        options = Options()
        options.add_experimental_option("detach", True)
        self.BROWSER = webdriver.Chrome(options=options)

    ACCESS_TOKEN = ''
    USER_ID = ''


    def authorize(self, scope):
        auth_request_params = {
            'client_id': self.CLIENT_ID,
            'response_type': 'code',
            'redirect_uri': self.REDIRECT_URI,
            'state': str(uuid.uuid4()),
            'scope': scope,
            'show_dialog': 'true'
        }

        auth_url = 'https://accounts.spotify.com/authorize/?' + urllib.parse.urlencode(auth_request_params)

        self.BROWSER.get(auth_url)    

    def close_browser(self):
        self.BROWSER.quit()
        
    def get_token(self, code):
        endpoint = 'https://accounts.spotify.com/api/token/?'

        body = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': self.REDIRECT_URI
        } 

        header = {
            'Authorization': 'Basic ' + self.BASE64_AUTH_STR,
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response: requests.Response = requests.post(endpoint, data=body, headers=header)
        if response.status_code == 200:
            return response.json()
        
        raise Exception(f'Failed to obtain Access Token. Response: {response.text}')
    
    # returns response json for parsing
    # expects body parameters to be json
    def GET(self, endpoint, param):
        header = {
            'Authorization': f'Bearer {self.ACCESS_TOKEN}'
        }

        response: requests.Response = requests.get(endpoint, headers=header, params=param)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Failed to search. Response: {response.text}')

    # expects body parameters to be json   
    def POST(self, endpoint, param):
        header = {
            'Authorization': f'Bearer {self.ACCESS_TOKEN}',
            'Content-Type': 'application/json'
        }

        response: requests.Response = requests.post(endpoint, headers=header, params=param)
        if response.status_code == 200:
            print('Success!')
            return 200
        else:
            raise Exception(f'Failed to add to library. Response: {response.text}')