import arcgis
from Settings import PortalUrl,ProfileName

print("Getting GIS")
gis = arcgis.GIS(PortalUrl, profile=ProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username)) 

NewUsername = "BerlinBear"
PassWord = "5BC76C4C9865774F0B08ABE3AC8A4DD455234A8872AD2B5D0611467F8B536C59"
FirstName = "Berlin"
LastName = "Bear"
EmailAddress = "developers@esri.nl"
UserDesc = "This is a newly created user for the EU DevSummit 2022. The word is:"
UserType= "Viewer"
UserImage = r"D:\Data\User_Image.png"
roleId = "iAAAAAAAAAAAAAAA" #defaults to viewer role

print("Creating user")
newUser = gis.users.create(NewUsername, PassWord, FirstName, LastName, EmailAddress, UserDesc, role=roleId, user_type = UserType)
print(newUser)


print("Updating user thumbnail")
newUser.update(thumbnail = UserImage)


print("Script complete")