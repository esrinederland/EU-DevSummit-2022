import arcgis
from Settings import PortalUrl,ProfileName

gis = arcgis.GIS(PortalUrl, profile=ProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username)) 

#Reset Look and Feel

#Remove created users
print("finding demo user")
DemoUser = gis.users.get("BerlinBear")

if not DemoUser is None:
    print(f"Deleting user: {DemoUser.username}")
    result = DemoUser.delete()
    print(f"Delete result: {result}")

#Remove Created Group
print("Searching for groups")
foundGroups = gis.groups.search(query='tags:"DevSummit2022"')
print(f"found: {len(foundGroups)}")
for demogroup in foundGroups:
    print(f"Deleting group: {demogroup.title}")
    result = demogroup.delete()
    print(f"Delete result: {result}")


#remove created items:
print("Searching for items")
itemsToRemove = gis.content.search(query='tags:"DevSummit2022"')
print(f"found: {len(itemsToRemove)}")
for item in itemsToRemove:
    print(f"Start deleting item: {item.title} , {item.type} ({item.id})")
    result = item.delete()
    print(f"deleteresult: {result}")


print("Script complete")
