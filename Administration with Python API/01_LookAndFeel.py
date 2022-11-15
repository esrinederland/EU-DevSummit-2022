import arcgis
from Settings import PortalUrl,ProfileName,DataFolder
import datetime
import os

print("Getting GIS")
gis = arcgis.GIS(PortalUrl, profile=ProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username)) 

# CHANGE HOMEPAGE TITLE
homePageJson = gis._con.get(f"https://{gis.properties.portalHostname}/sharing/rest/portals/self/resources/home.page.json?f=json")
print(homePageJson)

newTitle = "EsriNL DevTeam ArcGIS Enterprise"
homePageJson["header"]["title"] = newTitle

updateHomePageUrl = f"https://{gis.properties.portalHostname}/sharing/rest/portals/self/addResource"
updateHomePageParams = {}
updateHomePageParams["key"] = "home.page.json"
updateHomePageParams["text"] = homePageJson
updateHomePageParams["f"] = "json"

updateHomePageJson = gis._con.post(updateHomePageUrl, params=updateHomePageParams)
print(f"Home page updated: {updateHomePageJson}")

# CHANGE PORTAL TITLE
# sign in to dashboard using incognito: https://devteam.esri.nl/portal/apps/dashboards/home

editDatTime = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
gis.admin.ux.name = f"Our Fabulous portal {editDatTime}"

# sign in to dashboard using incognito: https://devteam.esri.nl/portal/apps/dashboards/home

# CHANGE FEATURED ITEMS