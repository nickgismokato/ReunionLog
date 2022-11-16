"""
MIT License

Copyright (c) 2022 Nickgismokato

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""


import requests
import json

tokenURL = "https://www.warcraftlogs.com/oauth/token"

"""Get client_id and client_secret from the data.json file"""
def Get_Auth():
    f = open('data.json')
    data = json.load(f)
    auth = (data['client']['client_id'], data['client']['client_secret'])
    f.close()
    return(auth) #Return str*str

"""Get token from OAuth. Can take optional input for storing the token."""
def Get_Token(store : bool = True):
    data = {"grant_type":" client_credentials"} #Required for curl
    auth = Get_Auth()
    
    #Get response from session grive tokenURL
    with requests.Session() as session:
        response = session.post(tokenURL, 
            data = data, 
            auth = auth
        )
    
    if store and response.status_code == 200:
        Store_Token(response)

    return response #Return json.

"""Store token from Get_Token. Require requests.models.Response type"""
def Store_Token(response : requests.models.Response):
    try:
        with open(".credentials.json", mode = "w+", encoding= "utf-8") as f:
            json.dump(response.json(), f)
    except OSError as e:
        print(e)
        return None

"""Read token from .credentials.json"""
def Read_Token():
    try:
        with open(".credentials.json", mode= "r+", encoding="utf-8") as f:
            access_token = json.load(f)    
        return access_token.get("access_token") #Return the response subfield "access_token"
    except OSError as e:
        print(e)
        return None

"""Return token. Is nesesary for all functions that require token."""
def Retrieve_Headers():
    Get_Token()
    return {"Authorization": f"Bearer {Read_Token()}"}
