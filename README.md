# SHPE Jr Conference CS Challenge
### Overview
You will be making a **Python** application that interacts with a **Spotify** account!

### The Goal
Create a program that creates a Spotify playlist for the user.

### Requirements
- Playlist is the result of some user input
    - Ex. name, # of songs, music genre, song/artist name, playlist cover
- At least 10 songs in the playlist
- At least 1 GET request to the Spotify Web API
- At least 1 POST request to the Spotify Web API

### Set-Up
You are provided with 2 template files to help you get started. One of these handles the authentication of the user account. You will notice that some variables need to be initialized \(there are comments to guide you!). The other file is a potential layout for your program with some Python syntax and Spotify Web API interaction examples.

Feel free to change these around as you see fit!

**Before you begin** you will need a few things...
- Navigate to the [Spotify for Developers](https://developer.spotify.com/) page and create an account
    - This allows you to interact with the API and create Spotify Apps
- Head over to your [Developer Dashboard](https://developer.spotify.com/dashboard) and click on "Create App"
- Give your app a cool name!
- In the Redirect URI field enter http://localhost:8080/callback
    - This is how the API knows where to send its information
- Check the Web API box
- Agree to the Terms of Service
- Save

**Now** that you've created the app...
- Go to your app settings
- Copy your Client ID and Client Secret to the corresponding placeholders in the auth.py file provided
    - These authenticate you to the API
    - Note: These should not be shared and are usually not stored in plaintext

### How it works
We are using a Python module called Spotipy that makes working with the Spotify Web API simpler. Once we authenticate a user, we can make requests to the API and get and manipulate data from their account. 

To **GET** information from the API, you make a request to an endpoint. An endpoint is where specific data is stored.

The reference section of the [Web API Documentation](https://developer.spotify.com/documentation/web-api) contains every endpoint you may need to develop your app. Take some time to understand the documentation and how to get different types of data.

Note: There are examples in the template files on the syntax of a request.

The API returns data formatted as [JSON](https://www.w3schools.com/python/python_json.asp). You will have to parse this data to work with it. Each endpoint response is documented and is different. You can see example responses and what each piece of data means under each references section.

You will need to **POST**, or send data to the API to create the playlist. Note that the API expects the same format it respons with, JSON. However, with the Spotipy module, you will not need to do this very often. Still, you can find some examples of "jsonifying" your data in the template files.

Below are some useful links for this activity, and your fellow SHPEitos are here to help you through your implementation. **Ask questions!**

### Links
- [Know the Basics](https://www.w3schools.com/python/)
- [Spotify for Developers](https://developer.spotify.com/)
- [Web API Documentation](https://developer.spotify.com/documentation/web-api)
- [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/)
- [HTTP Requests](https://www.w3schools.com/tags/ref_httpmethods.asp)
- [Python Requests](https://www.w3schools.com/python/module_requests.asp)
- [Python + JSON](https://www.w3schools.com/python/python_json.asp)
- [Python + Flask](https://flask.palletsprojects.com/en/3.0.x/quickstart/)