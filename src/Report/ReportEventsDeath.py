import requests
import json

"""query string to get events from given event"""
queryDeath = """query($code:String){
                reportData{
                    report(code:$code){
                        events(dataType: Deaths, endTime:9999999999999,  wipeCutoff: 3){
                            data
                        }
                    }
                }
            }"""
#dataType is an enum. Here it is used to get all death events.

"""Gets the data 'events' from GraphQL api. Require response, auth-url and event string"""
def Get_Data_EventDeath(response, publicURL, **kwargs):
    data = {"query": queryDeath, "variables": kwargs}
    with requests.Session() as session:
        session.headers = response
        response = session.get(publicURL, json= data)
    return response.json()
