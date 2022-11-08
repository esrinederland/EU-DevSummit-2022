import arcgis
from Settings import PortalUrl,ProfileName
import os

print("Getting GIS")
gis = arcgis.GIS(PortalUrl, profile=ProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username)) 

# ADD ITEM
fileFolder = r"D:\Data"
fileName = "earthquakes.csv"
fileType = "CSV"

filePath = os.path.join(fileFolder, fileName)
title = os.path.splitext(fileName)[0]
itemProperties={'type':fileType,
                'title':title,
                'description':'CSV file with earthquake information',
                'tags':'python, csv, earthquakes, DevSummit2022'}

addedItem = gis.content.add(item_properties=itemProperties, data=filePath)
print(f"The item '{fileName}' was added to your portal with itemID: '{addedItem.itemid}'")

# ADD THUMBNAIL 
thumbnailPath = r"D:\Data\EarthQuacke_image.png"
updatedItemSucceeded = addedItem.update(thumbnail=thumbnailPath)
print(f"Icon Update result: {updatedItemSucceeded}")


# SHARE WITH GROUP
groupsToShareWith = gis.groups.search(query='tags:DevSummit2022')

share = addedItem.share(groups=groupsToShareWith)
if share['results'][0]['success']:
    print(f"The item was successfully shared.")
else:
    print("Something went wrong while sharing the item.")


print("Script complete")