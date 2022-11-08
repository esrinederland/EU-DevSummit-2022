import arcgis
from Settings import PortalUrl, ProfileName

usr = input("Enter the username:")
pwd = input("Enter the password:")
print("Creating gis")
gis = arcgis.GIS(PortalUrl, username=usr, password=pwd, profile=ProfileName)

print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username)) 