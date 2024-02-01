# SHPE Jr Conference CS Challenge
This repository was created as part of the Engineering Challenge activity during the 2024 SHPE Jr Coference at the University of Florida. It's resources and materials were targetted toward high schools students interested in pursuing a career in Computer Science and Engineering.

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

### Computer Set-Up
**Make sure to follow one of these before moving on:**  
[Windows Setup](https://youtu.be/IBGMjyjzqR8)  
[Mac Setup](https://youtu.be/qhtK6n1YP4c)  

**Chromebook Users:**  
Follow [this guide](https://code.visualstudio.com/blogs/2020/12/03/chromebook-get-started) to set up VS Code on your chromebook.  
Follow [this video](https://youtu.be/h-B0r6ll40A?si=y19CY9viGP5Puvva) to ensure that everything necessary is set up properly.  
  
If you followed the steps above to enable and configure the Chromebook Linux environment, you should already have Python3, pip, and git installed and can follow the [Mac tutorial](https://youtu.be/qhtK6n1YP4c) to finish setting up this GitHub repository.  

### Challenge Set-Up
You are provided with 2 template files to help you get started. The file app.py handles the authentication of the user account. You will notice that some variables need to be initialized \(there are comments to guide you!). It also provides a potential layout for your program with some Python syntax and Spotify Web API interaction examples. The other file, spot.py, defines a class to help you interact with the API.

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
- Copy your Client ID and Client Secret to the corresponding placeholders in the app.py file provided
    - These authenticate you to the API
    - Note: These should not be shared and are usually not stored in plaintext

### How it works
You are provided with a Python class called Spot that makes working with the Spotify Web API simpler. Once we authenticate a user, we can make requests to the API and get and manipulate data from their account. 

We use **Flask** to host a server on the localhost, your computer's network, that the Spotify API will use to communicate with your app.

To **GET** information from the API, you make a request to an endpoint. An endpoint is where specific data is stored.

The reference section of the [Web API Documentation](https://developer.spotify.com/documentation/web-api) contains every endpoint you may need to develop your app. Take some time to understand the documentation and how to get different types of data.

Note: There are examples in the template files on the syntax of a request.

The API returns data formatted as [JSON](https://www.w3schools.com/python/python_json.asp). You will have to parse this data to work with it. Each endpoint response is documented and is different. You can see example responses and what each piece of data means under each references section.

You will need to **POST**, or send data to the API to create the playlist. Note that the API expects the same format it respons with, JSON. There is an example of this in the template files!

Below are some useful links for this activity, and your fellow SHPEitos are here to help you through your implementation. **Ask questions!**

***Some helpful endpoints...***  
- [Get current user](https://developer.spotify.com/documentation/web-api/reference/get-current-users-profile)  
- [Search for an item](https://developer.spotify.com/documentation/web-api/reference/search)  
- [Create a playlist](https://developer.spotify.com/documentation/web-api/reference/create-playlist)  
- [Add songs to a playlist](https://developer.spotify.com/documentation/web-api/reference/add-tracks-to-playlist)  

### Links
- [Know the Basics](https://www.w3schools.com/python/)
- [Spotify for Developers](https://developer.spotify.com/)
- [Web API Documentation](https://developer.spotify.com/documentation/web-api)
- [HTTP Requests](https://www.w3schools.com/tags/ref_httpmethods.asp)
- [Python Requests](https://www.w3schools.com/python/module_requests.asp)
- [Python + JSON](https://www.w3schools.com/python/python_json.asp)
- [Python + Flask](https://flask.palletsprojects.com/en/3.0.x/quickstart/)
