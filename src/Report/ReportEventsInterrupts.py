import requests
import json

"""query string to get events from given event"""
queryInterrupts = """query($code:String){
                reportData{
                    report(code:$code){
                        events(dataType: Interrupts, endTime:9999999999999){
                            data
                        }
                    }
                }
            }"""
#dataType is an enum. Here it is used to get all death events.

"""Gets the data 'events' from GraphQL api. Require response, auth-url and event string"""
def Get_Data_EventInterrupts(response, publicURL, **kwargs):
    data = {"query": queryInterrupts, "variables": kwargs}
    with requests.Session() as session:
        session.headers = response
        response = session.get(publicURL, json = data)
    return response.json()
