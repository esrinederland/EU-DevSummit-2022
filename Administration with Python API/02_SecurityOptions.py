import arcgis
from Settings import PortalUrl,ProfileName
import getpass

#anonymous
print("Create anonymous GIS")
gis = arcgis.GIS()
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.users.me)) 

#userpwd
print("")
print("Use login with username and password")
username = "maarten_dev"
pwd = getpass.getpass("Enter password")
gis2 = arcgis.GIS(PortalUrl,username,pwd)
print("Successfully logged into '{}' via the '{}' user".format(gis2.properties.portalHostname,gis2.properties.user.username)) 

#pro
print("")
print("Using ArcGIS Pro login")
gis3 = arcgis.GIS("PRO")
print("Successfully logged into '{}' via the '{}' user".format(gis3.properties.portalHostname,gis3.properties.user.username)) 

#home
print("")
print("Using HOME login")
gis4 = arcgis.GIS("HOME")
print("Successfully logged into '{}' via the '{}' user".format(gis4.properties.portalHostname,gis4.properties.user.username)) 

#Profile
print("")
print("Use profile to sign in")
gis5 = arcgis.GIS(PortalUrl, profile=ProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gis5.properties.portalHostname,gis5.properties.user.username)) 

print("Script complete")