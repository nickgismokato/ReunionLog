import requests
import json

"""query string to get names from given event"""
queryName = """query($code:String){
                reportData{
                    report(code:$code){
                        masterData(translate:false){
                            actors(type:"Player"){
                                id
                                name
                            }
                        }
                    }
                }
            }"""

"""Gets the data 'actors' from GraphQL api. Require response, auth-url and event string"""
def Get_Data_Name(response, publicURL, **kwargs):
    data = {"query": queryName, "variables": kwargs}
    with requests.Session() as session:
        session.headers = response
        response = session.get(publicURL, json= data)
    return response.json()

"""Gets the data 'actors' from GraphQL api as a list. Require response, auth-url and event string"""
def Get_NameList(response,publicURL, **kwargs):
    response = Get_Data_Name(response, publicURL, **kwargs)['data']['reportData']['report']['masterData']
    returnList = []
    for plr in response['actors']:
        returnList.append((plr['id'],plr['name']))
    return returnList
