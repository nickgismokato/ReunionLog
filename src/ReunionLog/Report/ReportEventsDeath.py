import requests
import json
from gql_query_builder import GqlQuery


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

"""query($code: String){
    reportData{
        report(code: $code){
            events(dataType: Deaths, endTime: 9999999999999, wipeCutoff: 3){
                data
            }
        }
    }
}
"""

#newQueryDeath
event_field = GqlQuery().fields(['data']).query('events', input={'dataType' : 'Deaths', 'endTime' : '9999999999999', 'wipeCutoff': '3'}).generate()
reportData_field = GqlQuery().fields([event_field]).query('report', input={'code' : '$code'}).operation('reportData').generate()
new_queryDeath = GqlQuery().fields([reportData_field]).query('query', input={'$code' : 'String'}).generate()

#operation('query')


#dataType is an enum. Here it is used to get all death events.

"""Gets the data 'events' from GraphQL api. Require response, auth-url and event string"""
def Get_Data_EventDeath(response, publicURL, **kwargs):
    print(new_queryDeath)
    data = {"query": queryDeath, "variables": kwargs}
    with requests.Session() as session:
        session.headers = response
        response = session.get(publicURL, json= data)
    return response.json()

