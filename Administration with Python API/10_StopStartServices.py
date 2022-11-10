import arcgis
from Settings import PortalUrl,ProfileName
import datetime

print("Getting GIS")
gis = arcgis.GIS(PortalUrl, profile=ProfileName,verify_cert=False)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username)) 

#Get GIS Server
print("Getting admin")
admin = gis.admin

print("Getting serverManager")
serverManager = admin.servers

print("getting hosting server")
gis_server = serverManager.get("HOSTING_SERVER")[0]

print("Getting services manager")
servicesManager = gis_server.services

print("Find service")

if servicesManager.exists(folder_name="/",name="SampleWorldCities",service_type="MapServer"):
    swcService = [serv for serv in servicesManager.list() if serv.properties.serviceName =="SampleWorldCities"][0]

    print(f"Service status: {swcService.status}")

    print("Stop Service")
    swcService.stop()

    print(f"Service status: {swcService.status}")
print("Script complete")