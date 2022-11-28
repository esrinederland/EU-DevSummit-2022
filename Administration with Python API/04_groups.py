import arcgis
from Settings import PortalUrl,ProfileName

print("Getting GIS")
gis = arcgis.GIS(PortalUrl, profile=ProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username)) 

# CREATE A NEW GROUP
GroupTitle = "Doomed To Stay"
GroupDescription = "This is a group created for the EU DevSummit 2022. The word is: BMW!!"
GroupTags = "DevSummit2022, Demo, NoLeaving"

foundGroups = gis.groups.search(f'title:{GroupTitle}')
if len(foundGroups) > 0:
    newGroup = foundGroups[0]
else:
    newGroup = gis.groups.create(title=GroupTitle, description=GroupDescription, tags=GroupTags, access='private', max_file_size=500000 , leaving_disallowed=True)
    print(f"Group '{newGroup.title}' created!")

# ADD USERS
groupUsers = ['mark_dev', 'maarten_dev','BerlinBear']
print("adding users to group")
usersAdded = newGroup.add_users(groupUsers)
if len(usersAdded['notAdded']) > 0:
    for i, notAddedUser in enumerate(usersAdded['notAdded']):
        print(f"{notAddedUser} was not added: ")#{usersAdded['notAddedDetails'][i]['error']['message']}")

for user in groupUsers:
    if user not in usersAdded['notAdded']:
        print(f"User '{user}' was successfully added to the group.")


# CHANGE DESCRIPTION
descriptionUpdated = newGroup.update(description='You are really not allowed to leave this group...')
print(f"Update result: {descriptionUpdated}")

# CHANGE ICON
groupIconPath = r"D:\Data\Group_Image.png"
iconUpdated = newGroup.update(thumbnail=groupIconPath)
print(f"Icon Update result: {iconUpdated}")

print("Script complete")