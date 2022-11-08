import requests
import json

"""query string to get events from given event"""
queryEvent = """query($code:String){
                reportData{
                    report(code:$code){
                        events(endTime:999999999, dataType: Deaths){
                            data
                        }
                    }
                }
            }"""
#dataType is an enum. Here it is used to get all death events.

"""Gets the data 'events' from GraphQL api. Require response, auth-url and event string"""
def Get_Data_EventDeath(response, publicURL, **kwargs):
    data = {"query": queryEvent, "variables": kwargs}
    with requests.Session() as session:
        session.headers = response
        response = session.get(publicURL, json= data)
    return response.json()
