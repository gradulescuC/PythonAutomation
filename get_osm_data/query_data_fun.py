import requests
from selenium import webdriver

# bbox = bounding box
# https://overpass-turbo.eu/#
# https://wiki.openstreetmap.org/wiki/Key:amenity

def osm_data(amenity, bbox):
    url = "https://overpass.kumi.systems/api/interpreter"
    query = '[out:json];node [amenity='+ amenity+'] ('+bbox+'); out;'
    response = requests.get(url,params=
    {
        "data": query
    })
    return response.json()
    # return json.loads(str(response))

print("------------------------")
a = osm_data("nightclub","53.2987342,-6.3870259,53.4105416,-6.1148829")
# b = osm_data("teatru","53.2987342,-6.3870259,53.4105416,-6.1148829");
poa = a["elements"][0]["tags"]
adr = poa["addr:street"]
amn = poa["amenity"]
name = poa["name"]
ohr = poa["opening_hours"]
phn = poa["phone"]
web = poa["website"]
print(adr)
print(amn)
print(name)
print(ohr)
print(phn)
print(web)
driver = webdriver.Chrome("/Users/gradulescu/Desktop/Personal/Cursuri/ITF/Automation Course/Proiecte Python/RepositoryGithub/PythonAutomation/venv/04 - selenium_workshop_pom/resources/chromedriver")
driver.get(web)
driver.quit()

# TODO check if key in dict, if true select and open the website, else do not do anything
