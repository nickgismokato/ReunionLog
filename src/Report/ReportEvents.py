import requests
import json

queryEvent = """query($code:String){
                reportData{
                    report(code:$code){
                        events(endTime:999999999, dataType: Deaths){
                            data
                        }
                    }
                }
            }"""

def Get_Data_Event(response, publicURL, **kwargs):
    data = {"query": queryEvent, "variables": kwargs}
    with requests.Session() as session:
        session.headers = response
        response = session.get(publicURL, json= data)
    return response.json()
