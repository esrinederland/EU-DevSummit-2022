import arcgis
from Settings import PortalUrl,ProfileName

gis = arcgis.GIS(PortalUrl, profile=ProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username))

# GET THE USER THAT WAS PREVIOUSLY CREATED
newUser = gis.users.get("BerlinBear")

# SET A NEW LICENSE TYPE
print("Update license type:")
newUser.update_license_type("Creator")

# SET A NEW ROLE NAME
newRoleName = "DevSummit DemoRole"
print("Searching for role id")
for role in gis.users.roles.all():
    if role.name==newRoleName:
        roleId = role.role_id
        print("Updating role")
        newUser.update_role(roleId)
        break

# GET AN ARCGIS PRO LICENSE AND ASSING IT TO THE USER
print("Getting arcgis pro license")
license = gis.admin.license.get('ArcGIS Pro')

print(license.all()) # returns a list of all usernames and their entitlements for this license

print("Assigning a pro license to a user")
licenseAssigned = license.assign(username='BerlinBear', entitlements='desktopBasicN')
if licenseAssigned:
    print(f"The pro license was successfully added to the user.")
else:
    print("Something went wrong while adding the license.")

print("Script complete")