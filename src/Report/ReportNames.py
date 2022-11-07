import requests
import json

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

def Get_Data(response, publicURL, **kwargs):
    data = {"query": queryName, "variables": kwargs}
    with requests.Session() as session:
        session.headers = response
        response = session.get(publicURL, json= data)
    return response.json()

def Get_NameList(response,publicURL, **kwargs):
    response = Get_Data(response, publicURL, **kwargs)['data']['reportData']['report']['masterData']
    returnList = []
    for plr in response['actors']:
        returnList.append((plr['id'],plr['name']))
    return returnList
