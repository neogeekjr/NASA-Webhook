#!/usr/bin/env python
# -*- coding: utf-8 -*-
from requests import get,post
import json
with open("config.json",'r') as Config_File:
    Config_Data=json.loads(Config_File.read())
Config_File.close() 
# Access Config Information
NASA_API_Key=Config_Data['NASA_API_Key']
Version=Config_Data['Version']
Webhook_URL=Config_Data['Webhook_URL']
# Set base json data entry
JSON_Data={}
# Gets Space Station Location
ISS_Data=get('http://api.open-notify.org/iss-now.json').json() # Get ISS Data
Latitude=ISS_Data['iss_position']['latitude'] # Get ISS Latitude
Longitude=ISS_Data['iss_position']['longitude'] # Get ISS longitude
# Get NASA APOD Data 
NASA_Request=get(f'https://api.nasa.gov/planetary/apod?api_key={NASA_API_Key}') # Get NASA Data
if NASA_Request.status_code!=200:
    JSON_Data={"content":"API Key Invalid or API offline"}
else:
    NASA_Data=NASA_Request.json()
    # Check If Valid Response
    NASA_Photo_URL=NASA_Data['url'] # Get APOD url
    NASA_Title=NASA_Data['title'] # Get APOD title
    try:NASA_Artist=NASA_Data['copyright'] # Try to get APOD Artist
    except KeyError:NASA_Artist='Not Found';pass # If fail then say no artist found
    # If youtube in URL then get youtube thumbnail
    if 'https://www.youtube.com' in NASA_Photo_URL:NASA_Photo_URL="https://img.youtube.com/vi/"+NASA_Photo_URL.replace('https://www.youtube.com/','').replace('?rel=0','')+'/default.jpg' 
    else:NASA_Photo_URL=NASA_Photo_URL.replace(' ','%20') # Strip any spaces from photo to prevent bugs
    # JSON data for posting
    JSON_Data={"username":"Photo Of The Day","avatar_url":NASA_Photo_URL,"embeds":[{'title':NASA_Title,'color':5964804,"description":f"Photo By: {NASA_Artist}\nThe ISS is currently at:\n**{Latitude}**, **{Longitude}**","image":{"url": NASA_Photo_URL},"footer":{"text":f"Made by NeoGeekJr V{Version}","icon_url": "https://neogeekjr.com/src/pfp.png"}}]}
    # Check for update before posting
    if float(get('https://raw.githubusercontent.com/neogeekjr/NASA-Webhook/main/version.txt').text)>float(Version):JSON_Data['content']="New Version Out Please Update [here](https://github.com/neogeekjr/NASA-Webhook)"


post(Webhook_URL,json=JSON_Data)