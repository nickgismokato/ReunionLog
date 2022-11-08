import requests
import json

"""query string to get abilities from given event"""
queryAbilities = """query($code:String){
                reportData{
                    report(code:$code){
                        masterData(translate:false){
                            abilities{
                                gameID
                                name
                            }
                        }
                    }
                }
            }"""

"""Gets the data 'abilities' from GraphQL api. Require response, auth-url and event string"""
def Get_Data_Ability(response, publicURL, **kwargs):
    data = {"query": queryAbilities, "variables": kwargs}
    with requests.Session() as session:
        session.headers = response
        response = session.get(publicURL, json= data)
    return response.json()

"""Gets the data 'abilities' from GraphQL api as a list. Require response, auth-url and event string"""
def Get_AbilityList(response, publicURL, **kwargs):
    response = Get_Data_Ability(response, publicURL, **kwargs)['data']['reportData']['report']['masterData']
    returnList = []
    for plr in response['abilities']:
        returnList.append((plr['gameID'],plr['name']))
    return returnList
