import requests
import json

tokenURL = "https://www.warcraftlogs.com/oauth/token"

def Get_Auth():
    f = open('data.json')
    data = json.load(f)
    auth = (data['client']['client_id'], data['client']['client_secret'])
    f.close()
    return(auth)

def Get_Token(store : bool = True):
    data = {"grant_type":" client_credentials"}
    auth = Get_Auth()
    
    with requests.Session() as session:
        response = session.post(tokenURL, 
            data = data, 
            auth = auth
        )
    
    if store and response.status_code == 200:
        Store_Token(response)

    return response

def Store_Token(response : requests.models.Response):
    try:
        with open(".credentials.json", mode = "w+", encoding= "utf-8") as f:
            json.dump(response.json(), f)
    except OSError as e:
        print(e)
        return None

def Read_Token():
    try:
        with open(".credentials.json", mode= "r+", encoding="utf-8") as f:
            access_token = json.load(f)    
        return access_token.get("access_token")
    except OSError as e:
        print(e)
        return None

def Retrieve_Headers() -> dict[str, str]:
    Get_Token()
    return {"Authorization": f"Bearer {Read_Token()}"}
