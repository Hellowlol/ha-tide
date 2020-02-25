
import requests
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET
from collections import defaultdict

def to_data(data):
    root = ET.fromstring(data)
    data = defaultdict(dict)
    for el in root.iter('data'):
        for e in el:
            data[el.attrib.get('type')][e.attrib.get("time")] = e.attrib
    return data

def get_tide_xml(lat=58.974339, lon=5.730121, time_from=None, time_to=None, datatype="tab", interval=10):

    if time_from is None:
        time_from = datetime.utcnow().replace(second=0, microsecond=0)

    if time_to is None:
        time_to = time_from + timedelta(hours=24)
        time_to.replace(second=0, microsecond=0)


    url = f"http://api.sehavniva.no/tideapi.php?lat={lat}&lon={lon}&fromtime={time_from.isoformat()}&totime={time_to.isoformat()}&datatype={datatype}&refcode=cd&place=&file=&lang=en&interval={interval}&dst=0&tzone=0&tide_request=locationdata"

    response = requests.get(url)
    print(response.url)
    print(response.status_code)

    if response.ok:
        to_data(response.text)
    else:
        print("crap")




get_tide_xml()
#t = datetime.utcnow()
#print(t)

#r = t.strptime("yyyy-MM-ddTHH:MM")
#print(t.isoformat())
