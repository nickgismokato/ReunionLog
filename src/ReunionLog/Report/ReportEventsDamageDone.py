import requests
import json

"""query string to get events from given event"""
queryDamageDone = """query($code:String){
                reportData{
                    report(code:$code){
                        events(dataType: DamageDone, endTime:9999999999999){
                            data
                        }
                    }
                }
            }"""
#dataType is an enum. Here it is used to get all death events.

"""Gets the data 'events' from GraphQL api. Require response, auth-url and event string"""
def Get_Data_EventDamageDone(response, publicURL, **kwargs):
    data = {"query": queryDamageDone, "variables": kwargs}
    with requests.Session() as session:
        session.headers = response
        response = session.get(publicURL, json = data)
    return response.json()
