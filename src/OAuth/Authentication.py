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
    data = {"grant_type":" client_credentials"} #Requered for curl
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
def Retrieve_Headers() -> dict[str, str]:
    Get_Token()
    return {"Authorization": f"Bearer {Read_Token()}"}
