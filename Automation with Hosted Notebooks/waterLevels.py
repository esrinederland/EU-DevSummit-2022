import datetime
import requests


def RunScript(locationSlug):
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    print(f"Getting water level for location: {locationSlug}")

    url = "https://waterinfo.rws.nl/api/detail"
    params = {}
    params["expertParameter"] = "Waterhoogte___20Oppervlaktewater___20t.o.v.___20Normaal___20Amsterdams___20Peil___20in___20cm"
    params["locationSlug"] = locationSlug
    params["user"] = "publiek"
    
    r = requests.get(url, params=params)
    if r.status_code == 200:
        response = r.json()
        print(f"Water level at {response['latest']['data']} cm NAP")
    else:
        print(f"Query was returned with status code {r.status_code}")
